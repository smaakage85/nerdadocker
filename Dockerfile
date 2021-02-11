FROM python:3.8.6-slim-buster

COPY . /app
WORKDIR /app

# install and download requirements for application.
RUN pip install -r requirements.txt
RUN python init.py

EXPOSE  5000

CMD ["python", "app.py"]