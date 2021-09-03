FROM quay.io/thoth-station/s2i-lab-elyra:v0.0.12
RUN pip install seldon-core==1.10.0
RUN pip install alibi==0.6.0
RUN pip install alibi-detect==0.7.2
RUN pip install click>=8.0
RUN pip install Minio==6.0.2
RUN pip install matplotlib==3.4.3
RUN pip install boto3==1.18.34
RUN pip install seaborn==0.11.2
RUN pip install pandas==1.3.2
RUN pip install mlflow>=1.20.1
RUN pip install watermark
RUN pip install dill==0.3.4
RUN pip install joblib==1.0.1
RUN pip install category_encoders==2.2.2
RUN pip install ipynbname==2021.3.2
USER root
RUN yum install -y mesa-libGL
USER 1001