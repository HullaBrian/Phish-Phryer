# syntax=docker/dockerfile:1
FROM python:slim-bullseye AS base_image

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY./poetry.lock ./pyproject.toml /phish-phryer/
RUN poetry install --no-interaction --no-ansi