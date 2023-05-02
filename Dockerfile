FROM python:3.8-slim-buster
WORKDIR /app
copy . /app

RUN apt update -y 

RUN apt update -y && pip install -r requirements.txt

CMD ["python3", "app.py"]