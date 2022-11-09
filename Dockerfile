FROM python:3.9-slim
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY ./app/ ./app/

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]