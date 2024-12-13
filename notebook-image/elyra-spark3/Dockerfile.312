FROM quay.io/thoth-station/s2i-lab-elyra:v0.0.12

ARG PKG_ROOT=/opt/spark
ARG SPARK_VERSION=3.1.2

USER root

# Download and extract the binaries for Spark and Hadoop
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.2.tgz &&\
    tar -C /opt -zxf spark-${SPARK_VERSION}-bin-hadoop3.2.tgz &&\
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop3.2 ${PKG_ROOT} &&\
    rm spark-${SPARK_VERSION}-bin-hadoop3.2.tgz

# Install java 11 to run spark
RUN yum -y install java-11-openjdk java-11-openjdk-devel maven &&\
    yum clean all

# Setup required env vars for spark and hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.12.0.7-0.el8_4.x86_64
ENV PATH=$JAVA_HOME/bin:$PATH
ENV SPARK_HOME=${PKG_ROOT}
ENV SPARK_CLUSTER=spark-cluster-$JUPYTERHUB_USER_NAME

#Fix java symlink to Java 11
RUN ln -sf $JAVA_HOME/bin/java /usr/bin/java

#Install python packages
RUN pip install pyspark==${SPARK_VERSION}
RUN pip install openshift-client
RUN pip install jinja2

USER 1001
RUN fix-permissions ${PKG_ROOT}
