# =use a base image with python installed 
FROM python:3.8-slim

#set the working directory inside the container
WORKDIR /app

#copy the current directory contents into the container at /app
COPY . /app



RUN pip install Flask_sqlalchemy
EXPOSE 5000
CMD ["python", "app.py"]