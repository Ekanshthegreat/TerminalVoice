# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies, including PortAudio, libatomic1, and ALSA
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    libatomic1 \
    alsa-utils \
    && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory (including subdirectories) into the container
COPY . /app/

# Set the working directory to the subdirectory containing main.py
WORKDIR /app/terminal-voice

# Set the command to run your application
CMD ["python", "main.py"]
