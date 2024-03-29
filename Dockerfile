# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base_image

# Install poetry
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    coreutils \
    git \
    curl \
    nano \
    tor \
    htop \
    firefox-esr
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip install poetry

# Copying over project files
RUN mkdir /phryer-phryer
RUN mkdir /phryer-phryer/phryer
COPY phryer /phish-phryer/phryer

# Dependency management
COPY ./poetry.lock /phish-phryer/poetry.lock
COPY ./pyproject.toml /phish-phryer/pyproject.toml
WORKDIR /phish-phryer
RUN poetry install --no-interaction --no-ansi --no-root

CMD tor