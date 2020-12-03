FROM puckel/docker-airflow 

LABEL maintainer="fmasood@redhat.com"


USER root
RUN pip install --upgrade pip 
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt



RUN chown -R airflow /app
USER airflow
COPY components airflow_pipeline.py  /usr/local/airflow/dags/
COPY components /usr/local/airflow/dags/components
