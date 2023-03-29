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

kubectl apply -f grafana/volume.yaml
kubectl apply -f grafana/deployment.yaml
kubectl apply -f grafana/service.yaml

kubectl apply -f prometheus/clusterRole.yaml
kubectl apply -f prometheus/deployment.yaml
kubectl apply -f prometheus/service.yaml

kubectl apply -f loki/deployment.yaml
kubectl apply -f loki/service.yaml

kubectl apply -f promtail/promtail.yaml

kubectl apply -f py-consumer/deployment.yaml
kubectl apply -f py-consumer/service.yaml