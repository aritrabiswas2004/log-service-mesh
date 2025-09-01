FROM python:3.12-alpine

WORKDIR /app

COPY greeter.py .

RUN pip install flask

CMD ["python3", "-u", "greeter.py"]