from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from components import train, validate
from datetime import timedelta
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Faisal Masood',
    'depends_on_past': False,
    'start_date': days_ago(31),
    'email': ['fmasood@redhat.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)

}

dag = DAG(
    'iris_pipeline',
    default_args=default_args,
    description='a basic ml pipeline',
    schedule_interval=timedelta(days=30),
)


preprocess = BashOperator(
    task_id='fetch-resources',
    bash_command='ls -lrt',
    dag=dag,
)

split = BashOperator(
    task_id='preprocess',
    bash_command='ls -lrt',
    dag=dag,
)

# split2 = BashOperator(
#     task_id='split2',
#     bash_command='ls -lrt',
#     dag=dag,
# )

train = PythonOperator(
    task_id='train',
    python_callable=train.train_model,
    op_kwargs={'train_location': 's3://train', 'test_location': '/test'},
    dag=dag,
)

validate = PythonOperator(
    task_id='validate',
    python_callable=validate.validate_model,
    op_kwargs={'train_location': 's3://train', 'test_location': '/test'},
    dag=dag,
)


# preprocess >> [split,split2] >>  train >> validate
preprocess >> [split] >>  train >> validate