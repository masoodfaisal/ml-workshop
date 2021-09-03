FROM continuumio/miniconda3:latest

ADD . /app
WORKDIR /app

RUN pip install mlflow>=1.20.1
RUN pip install boto3==1.18.34
RUN pip install psycopg2-binary

# pymysql
