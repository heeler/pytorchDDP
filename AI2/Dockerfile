FROM pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8


# Update the apt package list and install any necessary packages (customize as needed)
RUN apt-get update && apt-get install -y \
    apt-utils
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    cmake \
    python3-dev \
    python3.12 \
    python3.12-dev \
    python3.12-venv \
    libhwloc-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/amazon/efa \
    && wget https://efa-installer.amazonaws.com/aws-efa-installer-latest.tar.gz -O /tmp/aws-efa-installer-latest.tar.gz \
    && tar -xf /tmp/aws-efa-installer-latest.tar.gz -C /tmp \
    && cd /tmp/aws-efa-installer \
    # Run the installer in container-only mode (no kernel modules)
    && ./efa_installer.sh -y --skip-kmod \
    && rm -rf /tmp/aws-efa-installer*

# python3.12-distutils was in the command above but is now removed after deprication

# Set the working directory in the container
WORKDIR /stage/
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.12 get-pip.py

CMD ["/stage/entrypoint.sh"]
