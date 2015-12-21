FROM python:2.7
MAINTAINER Sébastien Brennion LeanBI

RUN pip install boto
ADD swissmeteo.py /opt/swissmeteo/

CMD "python /opt/swissmeteo/swissmeteo.py"