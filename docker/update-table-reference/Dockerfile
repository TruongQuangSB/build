FROM python:3.12-bullseye

RUN apt-get update
RUN apt-get -y dis-upgrade
RUN apt-get install -y git
RUN pip install GitPython
RUN pip install requests

ADD . /update-table-reference
RUN pip install /update-table-reference
