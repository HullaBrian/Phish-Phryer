#!/bin/bash


BASEDIR=$(dirname $0)
path="${BASEDIR}/index"
echo "Using \"${path}\" as docker directory"


WEBSITE_FILES=$(python3 config_reader.py website_files)
DOCKER_PORT=$(python3 config_reader.py docker_port)
INTERNAL_PORT=$(python3 config_reader.py internal_port)
CONTAINER_NAME=$(python3 config_reader.py container_name)
echo "website_files=${WEBSITE_FILES}"
echo "docker_port=${DOCKER_PORT}"
echo "internal_port=${INTERNAL_PORT}"
echo "container_name=${CONTAINER_NAME}"


TMP=$(docker container inspect "${CONTAINER_NAME}" | grep -q "Error: No such container:")
if ${TMP}; then
  echo "Running \"docker run -d -p ${DOCKER_PORT}:${INTERNAL_PORT} -v ${path}:/usr/share/nginx/html --name ${CONTAINER_NAME} nginx\""
  docker run -d -p "${DOCKER_PORT}":"${INTERNAL_PORT}" -v "${path}":/usr/share/nginx/html --name "${CONTAINER_NAME}" nginx
  TEST=$(docker start "${CONTAINER_NAME}")
  exit
fi
TMP=$(docker ps | grep -q "${CONTAINER_NAME}")
if ${TMP}; then
  echo "Docker container is already running. Restarting it..."
  echo "Running \"docker stop ${CONTAINER_NAME}"
  docker stop "${CONTAINER_NAME}"
fi
echo "Running \"docker start ${CONTAINER_NAME}\""
docker start "${CONTAINER_NAME}"
