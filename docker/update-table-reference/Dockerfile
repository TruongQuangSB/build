FROM python:3.12-bullseye

RUN apt-get update
RUN apte-get -y dis-upgrade
RUN pip install GitPython
RUN pip install requests

ADD . /update-table-reference
RUN pip install /update-table-reference
