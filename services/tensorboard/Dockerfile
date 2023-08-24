FROM nvcr.io/nvidia/pytorch:23.07-py3

# set work directory
WORKDIR /root/data/saved

# install system dependencies
RUN apt update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /root/data/saved/requirements.txt
RUN pip install -r requirements.txt