#!/usr/bin/env bash

DOCKER_CONTEXT_PATH=$1

echo "Building image DeepSentry"
docker build -f ${DOCKER_CONTEXT_PATH}/Dockerfile -t deepsentry ${DOCKER_CONTEXT_PATH}

echo "\n\nChecking build images..."
docker image inspect deepsentry > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo " deepsentry build success"
else
    echo " deepsentry build failed"
fi
