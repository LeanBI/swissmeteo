FROM python:2.7
MAINTAINER Sébastien Brennion LeanBI

RUN pip install boto
RUN pip install urllib2
RUN pip install dateutil
ADD swissmeteo.py /opt/swissmeteo/

CMD "python /opt/swissmeteo/swissmeteo.py"