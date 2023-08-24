FROM nvcr.io/nvidia/pytorch:23.07-py3

# set work directory
WORKDIR /root/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CUDA_DEVICE_ORDER PCI_BUS_ID

# install system dependencies
RUN apt update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /root/src/requirements.txt
RUN pip install -r requirements.txt