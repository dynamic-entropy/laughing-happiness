FROM python:slim-buster

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
