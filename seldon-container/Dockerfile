FROM python:3.7-slim


RUN mkdir /microservice
WORKDIR /microservice
COPY IrisClassifier.py  IrisClassifier.sav requirements.txt /microservice/
RUN pip install -r requirements.txt


# EXPOSE 5000


# Define environment variable
ENV MODEL_NAME IrisClassifier
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0


CMD seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE