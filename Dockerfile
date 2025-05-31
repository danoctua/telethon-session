FROM python:3.12.7-slim
LABEL authors="danoctua"

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY main.py /app/main.py

ENTRYPOINT [ "python3", "main.py" ]
