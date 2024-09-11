FROM nvcr.io/nvidia/pytorch:24.08-py3

# set work directory
WORKDIR /root/src

RUN echo 'root:{your_password}' | chpasswd

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CUDA_DEVICE_ORDER PCI_BUS_ID

# install system dependencies
RUN apt update
RUN apt install -y openssh-server

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /root/src/requirements.txt
RUN pip install -r requirements.txt

# Configure SSH
RUN mkdir /var/run/sshd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  # I don't know the exact reason, but you need to make it for external access
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo 'export NOTVISIBLE="in users profile"' >> ~/.bashrc
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
