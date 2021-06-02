FROM registry.access.redhat.com/ubi8/python-38
LABEL maintainer=fmasood@redhat.com

RUN pip install pandas kafka-python
ADD data/Customer-Churn_P2.csv /opt
ADD kafka-populator/load-csv.py  /opt



