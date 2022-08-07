FROM python:3.10.5-slim

WORKDIR /app

COPY ./ ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
ENV PATH="${PATH}:/app"
RUN echo "#!/bin/bash\npython3 cli.py \$@" > fake
RUN chmod +x fake

ENTRYPOINT ["/bin/bash"]
