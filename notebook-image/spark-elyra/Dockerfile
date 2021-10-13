
FROM quay.io/odh-jupyterhub/s2i-spark-minimal-notebook:py36-spark2.4.5-hadoop2.7.3-1
USER root
RUN curl -sL https://rpm.nodesource.com/setup_12.x | bash -
# RUN yum install -y gcc-c++ make
RUN yum install -y nodejs
USER 1001

RUN pip install --upgrade pip==20.2.4
RUN pip install --upgrade jupyterlab

RUN pip install --upgrade "elyra[all]>=3.1.0" && jupyter lab build --dev-build=False --minimize=True
RUN pip install --upgrade elyra-pipeline-editor-extension && jupyter lab build --dev-build=False --minimize=True

ENTRYPOINT [ "/opt/app-root/bin/start.sh" ,"jupyter", "labhub", "--NotebookApp.default_url=/lab", "--config=/opt/app-root/etc/jupyter_server_config.py", "--ip=0.0.0.0", "--port=8080" ]
# FROM quay.io/thoth-station/s2i-lab-elyra:v0.0.12

# ARG PKG_ROOT=/opt/app-root
# ARG SPARK_VERSION=2.4.5
# #ARG HADOOP_VERSION=2.8.5
# ARG HADOOP_VERSION=2.10.1
# ARG JAVA_VERSION=1.8.0

# USER root
# # Download and extract the binaries for Spark and Hadoop
# RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-without-hadoop.tgz &&\
#     tar -C ${PKG_ROOT} -zxf spark-${SPARK_VERSION}-bin-without-hadoop.tgz &&\
#     mv ${PKG_ROOT}/spark-${SPARK_VERSION}-bin-without-hadoop ${PKG_ROOT}/spark-${SPARK_VERSION} &&\
#     rm spark-${SPARK_VERSION}-bin-without-hadoop.tgz
# RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz &&\
#     tar -C ${PKG_ROOT} -xf hadoop-${HADOOP_VERSION}.tar.gz &&\
#     rm hadoop-${HADOOP_VERSION}.tar.gz

# # Install java to execute hadoop jars
# RUN yum -y install java-$JAVA_VERSION-openjdk maven &&\
#     yum clean all

# # Setup required env vars for spark and hadoop
# ENV JAVA_HOME=/usr/lib/jvm/jre
# ENV SPARK_HOME=${PKG_ROOT}/spark-${SPARK_VERSION}

# # Add HADOOP_CONF_DIR to spark-env.sh based on output from running "hadoop classpath"
# RUN cp ${PKG_ROOT}/spark-${SPARK_VERSION}/conf/spark-env.sh.template ${PKG_ROOT}/spark-${SPARK_VERSION}/conf/spark-env.sh &&\
#     echo "HADOOP_CONF_DIR=$(${PKG_ROOT}/hadoop-${HADOOP_VERSION}/bin/hadoop classpath)" >> ${PKG_ROOT}/spark-${SPARK_VERSION}/conf/spark-env.sh

# USER 1001
# RUN fix-permissions ${PKG_ROOT}



# UID          PID    PPID  C STIME TTY          TIME CMD
# 1000760+       1       0  0 01:14 ?        00:00:00 /bin/bash /opt/app-root/bin/start.sh jupyter labhub --NotebookApp.default_url=/lab --config=/opt/app-root/etc/jupyter_server_config.py --ip=0.0.0.0 --port=8080
# 1000760+     102       1  1 01:14 ?        00:00:07 /opt/app-root/bin/python3.9 /opt/app-root/bin/jupyter-labhub --NotebookApp.default_url=/lab --config=/opt/app-root/etc/jupyter_server_config.py --ip=0.0.0.0 --port=8080
# 1000760+     216       0  0 01:21 pts/0    00:00:00 /bin/bash
# 1000760+     223     216  0 01:22 pts/0    00:00:00 ps -ef
# ~                                                          

# UID          PID    PPID  C STIME TTY          TIME CMD
# 1000760+       1       0  0 01:17 ?        00:00:00 /bin/bash /opt/app-root/bin/start.sh jupyterhub-singleuser --config=/opt/app-root/etc/jupyter_notebook_config.py --ip=0.0.0.0 --port=8080
# 1000760+      31       1  0 01:17 ?        00:00:01 /opt/app-root/bin/python3 /opt/app-root/bin/jupyterhub-singleuser --config=/opt/app-root/etc/jupyter_notebook_config.py --ip=0.0.0.0 --port=8080
# 1000760+      75       0  0 01:22 pts/0    00:00:00 /bin/bash
# 1000760+     102      75  0 01:22 pts/0    00:00:00 ps -ef
