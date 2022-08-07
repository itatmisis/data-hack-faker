FROM python:3.10.5-slim

WORKDIR /app

COPY ./ ./
RUN pip3 install poetry
RUN poetry install --no-root
RUN apt update -y
RUN apt install openjdk-11-jdk -y
ENV PATH="${PATH}:/app"
RUN echo "#!/bin/bash\npython3 cli.py \$@" > fake
RUN chmod +x fake
RUN poetry install


# ENTRYPOINT ["/bin/bash"]
CMD poetry run pytest
