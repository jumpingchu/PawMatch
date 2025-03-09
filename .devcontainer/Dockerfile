FROM mcr.microsoft.com/devcontainers/python:3.13

# Install gcloud CLI for GCP authentication
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
    && apt-get update -y \
    && apt-get install google-cloud-cli -y

# Install uv for installing python packages
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
