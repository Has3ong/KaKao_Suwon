FROM ubuntu:latest
MAINTAINER your_name "khsh5592"
RUN apt-get update -y
RUN apt-get install python3.6 -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
RUN ls -la /app/*
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["application.py"]
