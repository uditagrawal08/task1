from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import os 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define models
movie_genre = db.Table('movie_genre',
                       db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
                       db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True))

movie_actor = db.Table('movie_actor',
                       db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
                       db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True))

movie_technician = db.Table('movie_technician',
                            db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
                            db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genres = db.relationship('Genre', secondary=movie_genre, backref=db.backref('movies', lazy='dynamic'))
    actors = db.relationship('Actor', secondary=movie_actor, backref=db.backref('movies', lazy='dynamic'))
    technicians = db.relationship('Technician', secondary=movie_technician, backref=db.backref('movies', lazy='dynamic'))
if not os.path.exists('movies.db'):
    # Create an empty database with the required tables
    with app.app_context():
        db.create_all()

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Routes for CRUD operations on movies
@app.route('/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    if not data or 'name' not in data or 'release_year' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid movie data'}), 400
    
    new_movie = Movie(name=data['name'], release_year=data['release_year'], rating=data['rating'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'New movie created', 'movie_id': new_movie.id}), 201

#Used for fetching a particular movie by its id
#- GET and POST APIs to fetch a particular Movie, Add or Update a movie.

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    return jsonify({'id': movie.id, 'name': movie.name, 'release_year': movie.release_year, 'rating': movie.rating})

#update a movie by its id
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    data = request.get_json()
    if not data or 'name' not in data or 'release_year' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid movie data'}), 400

    movie.name = data['name']
    movie.release_year = data['release_year']
    movie.rating = data['rating']
    db.session.commit()
    return jsonify({'message': 'Movie updated', 'id': movie.id}), 200

#GET method to fetch all the movies - preferably paginated with custom filters like getting
# all movies of an actor or a director or a combination of actors/directors/technicians
@app.route('/movies', methods=['GET'])
def get_movies():
    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Custom filters
    actor = request.args.get('actor')
    technician = request.args.get('technician')

    # Base query
    query = Movie.query

    # Apply custom filters
    if actor:
        query = query.filter(Movie.actors.any(name=actor))
    if technician:
        query = query.filter(Movie.technicians.any(name=technician))

    # Paginate the query results
    movies = query.paginate(page=page, per_page=per_page)

    # Serialize the paginated movies
    output = {
        'total_movies': movies.total,
        'page': page,
        'per_page': per_page,
        'movies': [{'id': movie.id, 'name': movie.name, 'release_year': movie.release_year, 'rating': movie.rating} for movie in movies.items]
    }

    return jsonify(output)

#POST API to delete an actor from the database 
#if he or she is not associated with any movies
@app.route('/actor/<int:actor_id>', methods=["post"])
def delete_actor(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        return jsonify({'error': 'Actor not found'}), 404
    
    if Actor.query.filter_by(id=actor_id).join(movie_actor).count() > 0:
        return jsonify({'error': 'Actor is associated with movies. Cannot delete.'}), 400

    # If the actor is not associated with any movies, delete the actor
    db.session.delete(actor)
    db.session.commit()
    return jsonify({'message': 'Actor deleted successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
