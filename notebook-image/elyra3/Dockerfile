# FROM quay.io/thoth-station/s2i-lab-elyra:v0.0.12
FROM quay.io/guimou/s2i-generic-datascience-lmod-notebook:f34-py39_latest
RUN pip install --upgrade pip==20.2.4
RUN pip3 install --upgrade elyra[all] && jupyter lab build
RUN pip3 install --upgrade elyra-pipeline-editor-extension && jupyter lab build
RUN pip3 install --upgrade elyra-python-editor-extension && jupyter lab build

# USER root
#RUN jupyter labextension update @elyra/pipeline-editor-extension
#RUN jupyter labextension update @elyra/python-editor-extension
##USER root
##RUN pip install --upgrade pip==20.2.4
#RUN pip3 install --upgrade elyra
#RUN pip3 install --upgrade elyra-pipeline-editor-extension
#RUN pip3 install --upgrade elyra-python-editor-extension
USER 1001