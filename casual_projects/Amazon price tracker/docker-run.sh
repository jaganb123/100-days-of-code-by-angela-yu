#!/bin/bash

docker stop price-tracker && docker rm price-tracker || \
docker run -d --mount type=bind,source=/var/data,target=/usr/src/app --name price-tracker price-tracker


