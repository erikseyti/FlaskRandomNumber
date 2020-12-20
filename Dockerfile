FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
RUN pip3 install flask

COPY app.py /opt/app.py
COPY templates /opt/templates
COPY static /opt/static
COPY README.md /opt/README.md

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0

