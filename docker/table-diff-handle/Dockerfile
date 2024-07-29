FROM python:3.12-bullseye

# COPY ./docker/table-diff-handle table-diff-handle
# WORKDIR /table-diff-handle
ADD . /table-diff-view-handle
RUN pip install html2text
RUN pip install /table-diff-view-handle
