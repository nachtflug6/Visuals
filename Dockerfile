# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install essential utilities (adjust based on your needs)
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    build-essential \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file and install Python packages
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Set the entrypoint
ENTRYPOINT [ "python3" ]
