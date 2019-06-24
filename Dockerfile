FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Run main.py when the container launches
CMD [ "python", "./app/src/main.py" ]
