# Base image
FROM python:3.10

# working directory
WORKDIR /app

# Copy
COPY . /app

# Run
RUN pip install -r requirements.txt

# port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

