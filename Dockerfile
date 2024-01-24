# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update and install basic packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /workspace

# Copy your application's source code from your host to your image
# COPY . /workspace

# If your app needs to be built:
# RUN make / ./build_script.sh

# Specify the command to run on container start
# CMD ["./your-application"]


