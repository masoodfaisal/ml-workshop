#FROM python:3.7-slim
#RUN mkdir /microservice
#WORKDIR /microservice
#COPY requirements.txt /microservice/
#RUN pip install -r requirements.txt


# EXPOSE 5000
#
FROM quay.io/ml-aml-workshop/python:3.7-slimv2

WORKDIR /microservice
COPY CustomerChurnPredictor.py  CustomerChurnTransformer.py CustomerChurnPredictor.sav CustomerChurnOrdinalEncoder.pkl CustomerChurnOneHotEncoder.pkl /microservice/

ENV PERSISTENCE 0
CMD seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE --grpc-port ${GRPC_PORT} --metrics-port ${METRICS_PORT} --http-port ${HTTP_PORT}