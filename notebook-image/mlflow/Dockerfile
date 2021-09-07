#FROM continuumio/miniconda3:latest
FROM registry.access.redhat.com/ubi8/python-38

ADD . /app
WORKDIR /app
USER root
RUN pip install mlflow>=1.20.1
RUN pip install boto3==1.18.34
RUN pip install psycopg2-binary
USER 1001
# pymysql
