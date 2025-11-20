FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app
COPY requriements.txt



# Install dependencies
RUN pip install -r requirements.txt 
# Copy the rest of the application code
COPY . . 

EXPOSE 5000 

# Run the app
CMD ["python3", "app.py"] 