FROM registry.access.redhat.com/ubi8/python-38:1-71


RUN pip install --upgrade pip
RUN pip install openshift-client==1.0.13
RUN pip install jinja2==3.0.1
RUN pip install mlflow==1.20.2
RUN pip install minio==6.0.2
RUN pip install boto3==1.18.49
RUN pip install scikit-learn==0.24.2

# RUN pip install tensorflow==2.6.0
RUN pip install tf-nightly==2.8.0.dev20211005

COPY oc.tar /tmp/.
RUN cd /tmp && tar -xvf /tmp/oc.tar
# USER root
RUN chmod 755 /tmp/oc
# USER 1001
ENV OPENSHIFT_CLIENT_PYTHON_DEFAULT_OC_PATH=/tmp/oc
ENV OPENSHIFT_CLIENT_PYTHON_DEFAULT_OC_LOGLEVEL=10
ENV OPENSHIFT_CLIENT_PYTHON_DEFAULT_SKIP_TLS_VERIFY=true

