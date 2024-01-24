# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and Git
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Set the working directory inside the container
WORKDIR /workspace

# Clone your Git repository
RUN git clone https://github.com/ChanhooKum/ASR.git /workspace

# Install numpy and PyTorch
# The PyTorch version should be compatible with the system architecture.
# Use the PyTorch website (https://pytorch.org/get-started/locally/) to find the right version.
RUN pip3 install numpy torch torchvision torchaudio

# (Optional) If your repository has a requirements.txt file for Python dependencies, install them
# Uncomment and modify the following lines if you have a requirements.txt file
# COPY requirements.txt /workspace/
# RUN pip3 install -r /workspace/requirements.txt

# Start a bash shell by default so you can interactively run commands
CMD ["/bin/bash"]
