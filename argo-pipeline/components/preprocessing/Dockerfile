FROM python:3.7-slim

WORKDIR /app

COPY pre_process.py  requirements.txt /app/
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "preprocess.py" ]

