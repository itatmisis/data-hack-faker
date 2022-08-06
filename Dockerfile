FROM python:3.10.5

WORKDIR /app

COPY ./pyproject.toml ./
COPY ./src/data_hack_faker ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root


ENTRYPOINT /bin/bash
