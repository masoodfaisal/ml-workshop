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
ENV PERSISTENCE 0

COPY CustomerChurnPredictorAlibi.py  CustomerChurnPredictorAlibi.dill  CustomerChurnTransformer.py  CustomerChurnOrdinalEncoder.pkl CustomerChurnOneHotEncoder.pkl /tmp/microservice/
CMD seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE