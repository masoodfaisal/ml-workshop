FROM quay.io/thoth-station/s2i-lab-elyra:v0.0.5
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install watermark s3fs