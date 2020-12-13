FROM quay.io/ml-aml-workshop/python:3.7-slim


RUN mkdir /microservice
WORKDIR /microservice
COPY CustomerChurnPredictor.py  CustomerChurnTransformer.py CustomerChurnPredictor.sav CustomerChurnOrdinalEncoder.pkl CustomerChurnOneHotEncoder.pkl requirements.txt /microservice/
RUN pip install -r requirements.txt


# EXPOSE 5000


# Define environment variable
ENV MODEL_NAME CustomerChurnPredictor
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0


CMD seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE