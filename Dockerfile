FROM python:3.8-slim-buster

COPY flask_app.py .
COPY tasks.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
# ENTRYPOINT [ "python", "flask_app.py" ]
