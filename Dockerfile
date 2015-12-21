FROM python
MAINTAINER Sébastien Brennion LeanBI

RUN pip install boto
ADD swissmeteo.py /opt/swissmeteo/

CMD [python,/opt/swissmeteo/swissmeteo.py]