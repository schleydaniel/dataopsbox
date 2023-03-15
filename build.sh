#!/usr/bin/env bash

docker build -t py-producer:0.1 ./py-producer/
docker tag py-producer:0.1 py-producer:latest