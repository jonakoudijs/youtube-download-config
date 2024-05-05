# Set the base image to Debian slim
FROM python:3.12-slim

# File Author / Maintainer
LABEL maintainer="Jona Koudijs"

# Copy Python requirements file
COPY requirements.txt /tmp/requirements.txt

# Install required packages
RUN pip install -r /tmp/requirements.txt --no-cache-dir \
 && rm /tmp/requirements.txt

# Copy source code
COPY src/ /data/

# Set working directory
WORKDIR /data

# Set default container command
ENTRYPOINT ["/data/main.py"]
