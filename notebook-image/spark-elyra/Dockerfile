FROM quay.io/thoth-station/s2i-lab-elyra:v0.0.12

ARG PKG_ROOT=/opt/app-root
ARG SPARK_VERSION=2.4.5
#ARG HADOOP_VERSION=2.8.5
ARG HADOOP_VERSION=2.10.1
ARG JAVA_VERSION=1.8.0

USER root
# Download and extract the binaries for Spark and Hadoop
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-without-hadoop.tgz &&\
    tar -C ${PKG_ROOT} -zxf spark-${SPARK_VERSION}-bin-without-hadoop.tgz &&\
    mv ${PKG_ROOT}/spark-${SPARK_VERSION}-bin-without-hadoop ${PKG_ROOT}/spark-${SPARK_VERSION} &&\
    rm spark-${SPARK_VERSION}-bin-without-hadoop.tgz
RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz &&\
    tar -C ${PKG_ROOT} -xf hadoop-${HADOOP_VERSION}.tar.gz &&\
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Install java to execute hadoop jars
RUN yum -y install java-$JAVA_VERSION-openjdk maven &&\
    yum clean all

# Setup required env vars for spark and hadoop
ENV JAVA_HOME=/usr/lib/jvm/jre
ENV SPARK_HOME=${PKG_ROOT}/spark-${SPARK_VERSION}

# Add HADOOP_CONF_DIR to spark-env.sh based on output from running "hadoop classpath"
RUN cp ${PKG_ROOT}/spark-${SPARK_VERSION}/conf/spark-env.sh.template ${PKG_ROOT}/spark-${SPARK_VERSION}/conf/spark-env.sh &&\
    echo "HADOOP_CONF_DIR=$(${PKG_ROOT}/hadoop-${HADOOP_VERSION}/bin/hadoop classpath)" >> ${PKG_ROOT}/spark-${SPARK_VERSION}/conf/spark-env.sh

USER 1001
RUN fix-permissions ${PKG_ROOT}
