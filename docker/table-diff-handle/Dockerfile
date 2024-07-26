FROM python:3.12-bullseye

RUN pip install poetry
WORKDIR /docker/table-diff-handle
COPY . .

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "table-diff-view-handle.__main__"]
