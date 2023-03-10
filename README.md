# DataOpsBox

Local K8s cluster orchestrating Docker containers with Minikube  to trial and demonstrate applied DevOps in a distributed data engineering lifecycle.

***

## Prerequisites

- Install [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/) and [minikube](https://minikube.sigs.k8s.io/docs/ "Minikube Homepage")
- Provide sufficient CPU and memory (e.g. 4, 8g)

```mermaid
graph LR;
    A(Py Producer) -- run --> B((Worker 1));
    A(Py Producer) -- run --> C((Worker ...));
    A(Py Producer) -- run --> D((Worker n));
    B((Worker 1)) -- produce --> E{Kafka};
    C((Worker ...)) -- produce --> E{Kafka};
    D((Worker n)) -- produce --> E{Kafka};
    E{Kafka} -- consume --> F(J-Consumer);
```