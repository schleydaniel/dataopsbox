#!/usr/bin/env bash

docker build -t py-producer:0.1 ./py-producer/
docker tag py-producer:0.1 py-producer:latest

docker build -t kafka-kraft:0.1 ./kafka/
docker tag kafka-kraft:0.1 kafka-kraft:latest