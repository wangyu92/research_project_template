# Research Project Template

This is a template for machine learning research projects. The template is based on docker, which facilitates the reconfiguration of the training environment by separating the project from the host. As a result, it helps to ensure reproducibility, which is one of the most important factors in academia.
This template includes the following services:

- Trainer: This is based on the `Pytorch NGC` image provided by Facebook. See [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch) for detailed prerequisites.
- Tensorboard
- Jupyter

# How to use

## 0. Prerequisites
- Please add the required packages to `services/trainer/requests.txt`.
- In the `docker-compose.yaml` file, modify the following to match your configuration.
  - Container name for each service
  - Modify the port of each service, considering your network and host.

## 1. Clone the repository

```bash
git clone https://github.com/wangyu92/research_project_template
```

## 2. Build the docker image

```bash
cd research_project_template
docker compose up -d --build
```

## 3. Run the container

```bash
docker attach ${container_name}
```