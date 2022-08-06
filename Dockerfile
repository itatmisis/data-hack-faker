FROM python:3.10.5-slim

WORKDIR /app

COPY ./pyproject.toml ./
COPY ./src/data_hack_faker ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root
ENV PATH="${PATH}:/app"
RUN echo "#!/bin/bash\n python3 cli.py $@" > fake
RUN chmod +x fake

ENTRYPOINT ["/bin/bash"]
