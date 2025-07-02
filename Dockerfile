# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only dependencies list first (caching layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose port (if you ever add a web health check)
EXPOSE 5000

# Launch your bot
CMD ["python3", "noordidu_bot.py"]
