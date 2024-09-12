FROM python:3.12-bullseye

RUN apt-get update \
  apt-get -y dis-upgrade \
  apt-get install -y git \
  pip install GitPython \
  pip install requests

ADD . /update-table-reference
RUN pip install /update-table-reference
