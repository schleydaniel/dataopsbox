#!/usr/bin/env bash


kubectl delete -n dataopsbox deployment py-producer
kubectl delete -n dataopsbox deployment kafka-kraft

kubectl delete -n dataopsbox service py-producer-svc
kubectl delete -n dataopsbox service kafka-kraft-svc
