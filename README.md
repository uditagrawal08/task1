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

POST /movies: Create a new movie.![Screenshot (572)](https://github.com/uditagrawal08/task1/assets/122895302/e7d71dfb-1f42-4d10-a25d-c40cd1ab299b)

GET /movies: Retrieve a list of all movies ![Screenshot (571)](https://github.com/uditagrawal08/task1/assets/122895302/02a4378e-2946-42b6-9b6d-c5da5ebb528d)

GET /movies/<movie_id>: Retrieve details of a specific movie by its ID.![Screenshot (574)](https://github.com/uditagrawal08/task1/assets/122895302/c7aba3e7-bdfd-4c4a-b34d-f3905f6dc218)

GET /movies: Retrieve a list of all movies with optional pagination and filtering by actor or technician.

![Screenshot (575)](https://github.com/uditagrawal08/task1/assets/122895302/04dc6daa-30d8-45b7-bfdc-992c3a29dbdc)

![Screenshot (576)](https://github.com/uditagrawal08/task1/assets/122895302/2b4858d9-61e9-447d-bff9-e1ac574dc0f7)






PUT /movies/<movie_id>: Update details of a specific movie by its ID.![Screenshot (581)](https://github.com/uditagrawal08/task1/assets/122895302/0ebf2f7e-4669-4615-9977-ad772ff5979f)



POST /actor/<actor_id>: Delete an actor by their ID if they are not associated with any movies.
![Screenshot (578)](https://github.com/uditagrawal08/task1/assets/122895302/26a78d26-0b72-4b3e-aa31-082353b8957d)

![Screenshot (580)](https://github.com/uditagrawal08/task1/assets/122895302/b41fd5dd-6ac0-46c0-b0de-e08bafd3437f)




