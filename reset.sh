#!/usr/bin/env bash


kubectl delete -n dataopsbox deployment py-producer

kubectl delete -n dataopsbox service py-producer-svc
