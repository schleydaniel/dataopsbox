#!/usr/bin/env bash

docker build -t py-producer:0.1 ./py-producer/
docker tag py-producer:0.1 py-producer:latest

docker build -t py-consumer:0.1 ./py-consumer/
docker tag py-consumer:0.1 py-consumer:latest

docker build -t kafka-kraft:0.1 ./kafka/
docker tag kafka-kraft:0.1 kafka-kraft:latest

docker build -t prometheus:0.1 ./prometheus/
docker tag prometheus:0.1 prometheus:latest

docker build -t grafana:0.1 ./grafana/
docker tag grafana:0.1 grafana:latest

docker build -t loki:0.1 ./loki/
docker tag loki:0.1 loki:latest

docker build -t alertmanager:0.1 ./alertmanager/
docker tag alertmanager:0.1 alertmanager:latest