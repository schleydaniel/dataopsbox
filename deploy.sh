#!/usr/bin/env bash


while getopts 'b' OPTION; do
  case "$OPTION" in
    b)
      echo "building images"
      ./build.sh
      ;;
    ?)
      echo "script usage: $(basename \$0) [-b] " >&2
      exit 1
      ;;
  esac
done


kubectl apply -f namespace.yaml

kubectl apply -f py-producer/deployment.yaml
kubectl apply -f py-producer/service.yaml

kubectl apply -f kafka/deployment.yaml
kubectl apply -f kafka/service.yaml