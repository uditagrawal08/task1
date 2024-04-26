# Movie Database API

This is a simple backend API along with the backend database schema for managing a movie database.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (for local development)

You can install the dependencies using pip:

```bash
pip install Flask SQLAlchemy
````
Installation
Clone the repository:
```bash

git clone https://github.com/uditagrawal08/task1.git
````
Navigate to the project directory:
````bash
cd task1
````
Run the Flask application:
````bash
python app.py
````

The application will start running on http://localhost:5000.

API Endpoints
The Movie Database API provides the following endpoints for interacting with the database:

POST /movies: Create a new movie.

GET /movies: Retrieve a list of all movies with optional pagination and filtering by actor or technician.

GET /movies/<movie_id>: Retrieve details of a specific movie by its ID.

PUT /movies/<movie_id>: Update details of a specific movie by its ID.

POST /actor/<actor_id>: Delete an actor by their ID if they are not associated with any movies.

