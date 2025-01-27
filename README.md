# GenAIProject

## Streamlit Application with Docker

This project contains a Streamlit application containerized with Docker, allowing it to run on any system with Docker installed.

### Features

- Runs a **Streamlit web app** in a Docker container.
- No need for local Python setup or dependencies.
- Works on Linux.

---

## Requirements

1. **Docker**: Ensure Docker is installed and running.
   - [Download Docker](https://docs.docker.com/get-docker/)

---

## Quick Start Guide

### 1. Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/Biline-dev/GenAIProject.git
cd GenAIProject
```

### 2. Build the Docker Image
Run this command to build the Docker image:
```bash
docker build -t streamlit-app .
```

### 3. Run the application
Start the application in a Docker container:
```bash
docker run -p 8501:8501 streamlit-app
```

Once started, the app will be accessible in your browser at: http://localhost:8501
