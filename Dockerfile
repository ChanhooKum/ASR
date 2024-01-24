# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /workspace

# Copy your Python script and any other necessary files into the container
COPY . /workspace

# Install any required Python dependencies
# Uncomment and modify if you have requirements.txt
# RUN pip3 install -r requirements.txt

# Specify the command to run your Python script
CMD ["python3", "my_script.py"]
