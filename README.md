# Flask Blog API

A simple RESTful API for managing blog posts and comments using Flask.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Docker](#docker)
- [Testing](#testing)

## Introduction

This Flask application provides a blog API that allows users to create and manage blog posts and add comments to existing posts. The application is built using Flask and SQLAlchemy and includes user authentication using JWT.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone git@github.com:ttsia/flask-rest-blog-example.git
   cd flask-rest-blog-example

2. Create a virtual environment (optional, but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

4. Set the environment variables:

    Rename the .env.example file to .env and provide the necessary configuration values.

5. Initialize the database:

    ```bash
    flask db init
    flask db migrate

6. Start the application:

    ```bash
    flask run

The API will be available at http://localhost:5000. Use your preferred API client (e.g., Postman, cURL) to interact with the API.
API Documentation

7. Init DB:

    ```bash
    flask db init
    flask db migrate

## Docker

You can also run the application using Docker for easy deployment and isolation.

Make sure you have Docker installed on your system.
Clone the repository and navigate to the project root directory.
Build the Docker image and start the containers:

    docker-compose build
    docker-compose up

### Init DB inside docker
After `docker-compose up` command, run:

    docker-compose exec web flask db init
    docker-compose exec web flask db migrate


The API will be available at http://localhost:5000.

## Testing

To run the unit tests for this application, execute the following command:

    pytest

This will run the test cases and display the test results.