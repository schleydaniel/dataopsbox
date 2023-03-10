# DataOpsBox

Local K8s cluster orchestrating Docker containers with Minikube  to trial and demonstrate applied DevOps in a distributed data engineering lifecycle.

***

## Prerequisites

- Install [minikube](https://minikube.sigs.k8s.io/docs/ "Minikube Homepage")
- Provide sufficient CPU and memory (e.g. 4, 8g)

```mermaid
graph LR;
    A(Py Producer 1) -- produce --> D{Kafka};
    B(Py Producer ...) -- produce --> D{Kafka};
    C(Py Producer n) -- produce --> D{Kafka};
    D{Kafka} -- consume --> E(J-Consumer);
```