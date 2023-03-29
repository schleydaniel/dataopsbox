#!/usr/bin/env bash


kubectl delete -n dataopsbox deployment py-producer
kubectl delete -n dataopsbox deployment py-consumer
kubectl delete -n dataopsbox deployment kafka-kraft
kubectl delete -n dataopsbox deployment grafana
kubectl delete -n dataopsbox deployment prometheus
kubectl delete -n dataopsbox deployment loki

kubectl delete -n dataopsbox service py-producer-svc
kubectl delete -n dataopsbox service py-consumer-svc
kubectl delete -n dataopsbox service kafka-kraft-svc
kubectl delete -n dataopsbox service grafana-svc
kubectl delete -n dataopsbox service prometheus-svc
kubectl delete -n dataopsbox service loki-svc

kubectl delete -n dataopsbox daemonset promtail-ds
