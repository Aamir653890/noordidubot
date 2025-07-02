# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (for Flask)
EXPOSE 5000

# Start the bot
CMD ["python", "noordidu_bot.py"]
