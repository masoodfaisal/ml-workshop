FROM python:3.7.9-buster
# FROM registrxy.access.redhat.com/ubi8/python-36
# RUN pip install --upgrade pip
RUN mkdir /tmp/microservice
WORKDIR /tmp/microservice
COPY requirements.txt /tmp/microservice/
RUN pip install -r requirements.txt


# EXPOSE 5000


# Define environment variable
ENV MODEL_NAME IrisClassifierAlibi
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

RUN pip install seldon-core
COPY IrisClassifierAlibi.py  IrisClassifierAlibi.dill  /tmp/microservice/
CMD seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE