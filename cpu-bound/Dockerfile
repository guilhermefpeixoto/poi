ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim AS img

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD python3 -m flask run --host=0.0.0.0 --port=8000
