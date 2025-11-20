FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app
COPY requirements.txt /app/



# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . /app/
EXPOSE 5000 

# Run the app
CMD ["python3", "app.py"] 
