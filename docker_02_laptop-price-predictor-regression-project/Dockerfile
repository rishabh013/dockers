# Base image
FROM python:3.7

# working directory
WORKDIR /app

# Copy
COPY . /app

# Run
RUN pip install -r requirements.txt

# port
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py"]

