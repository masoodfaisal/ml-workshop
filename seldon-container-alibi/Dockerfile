FROM quay.io/ml-aml-workshop/python:3.7-slim

RUN mkdir /tmp/microservice
WORKDIR /tmp/microservice
COPY requirements.txt /tmp/microservice/
RUN pip install -r requirements.txt


# EXPOSE 5000


# Define environment variable
ENV MODEL_NAME CustomerChurnPredictorAlibi
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

RUN pip install seldon-core
COPY CustomerChurnPredictorAlibi.py  CustomerChurnPredictorAlibi.dill  /tmp/microservice/
CMD seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE