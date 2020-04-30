FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 8080

CMD ["sh", "-c", "python app.py"]
