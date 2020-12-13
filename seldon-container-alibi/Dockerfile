#FROM registry.access.redhat.com/ubi8/python-38
#RUN mkdir /tmp/microservice
#WORKDIR /tmp/microservice
#COPY requirements.txt /tmp/microservice/
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

FROM quay.io/ml-aml-workshop/python-alibi:0.0.1
WORKDIR /tmp/microservice
# EXPOSE 5000


# Define environment variable
ENV MODEL_NAME CustomerChurnPredictorAlibi
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

#RUN pip install seldon-core
COPY CustomerChurnPredictorAlibi.py  CustomerChurnPredictorAlibi.dill  /tmp/microservice/
CMD seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE