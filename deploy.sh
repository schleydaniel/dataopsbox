#!/usr/bin/env bash

./build.sh

kubectl apply -f namespace.yaml

kubectl apply -f py-producer/deployment.yaml
kubectl apply -f py-producer/service.yaml