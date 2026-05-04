#!/usr/bin/env bash

LOCAL_DATA_FOLDER=$1
DATA_MOUNT_POINT=$2

RUN_COMMAND="PYTHONPATH=/root/deepsentry/ python3 \
/root/deepsentry/src/tx/train.py $DATA_MOUNT_POINT"

docker run --runtime=nvidia -it --rm -v $LOCAL_DATA_FOLDER:$DATA_MOUNT_POINT deepsentry:latest \
/bin/bash -c "$RUN_COMMAND"
