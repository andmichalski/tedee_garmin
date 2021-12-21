FROM python:3.10-slim-buster
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apt-get update \
&& apt-get install gcc musl-dev python3-dev libffi-dev -y \
&& apt-get install build-essential -y

RUN pip install --upgrade pip
RUN python3 -m pip install cryptography
RUN pip3 install setuptools_rust
RUN pip3 install poetry

COPY ./pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-dev

# Install app
COPY ./rpiserver /app/rpiserver
RUN poetry install --no-dev
ENTRYPOINT poetry run uvicorn rpiserver.server:lock_app --reload --host 0.0.0.0 --port 8080
