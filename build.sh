#!/usr/bin/env bash

kubectl apply -f namespace.yaml

docker build -t py-producer:0.1 ./py-producer/
docker tag py-producer:0.1 py-producer:latest

kubectl apply -f py-producer/deployment.yaml
kubectl apply -f py-producer/service.yaml