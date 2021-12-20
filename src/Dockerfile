#Base Image
FROM python:3.6-alpine3.14
WORKDIR /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

CMD ["python", "email_parser.py"]
