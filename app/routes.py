from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Game
import re

from app.utils import validate_datetime

api = Namespace('games', description='Game operations')

game = api.model('Game', {
    'id': fields.Integer(readonly=True, description='The game unique identifier'),
    'name': fields.String(required=True, description='The game name'),
    'url': fields.String(description='The game URL'),
    'author': fields.String(description='The game author'),
    'published_date': fields.String(description='The date the game was published', example="2022-01-01 12:00:00", validate=validate_datetime)
})

@api.route('/')
class GameList(Resource):
    @api.doc('list_games')
    @api.marshal_list_with(game)
    def get(self):
        """List all games"""
        return Game.query.all()

    @api.doc('create_game')
    @api.expect(game)
    @api.marshal_with(game, code=201)
    def post(self):
        """Create a new game"""
        new_game = Game(name=api.payload['name'], url=api.payload.get('url'),
                        author=api.payload.get('author'), published_date=api.payload.get('published_date'))
        db.session.add(new_game)
        db.session.commit()
        return new_game, 201

@api.route('/<int:id>')
@api.param('id', 'The game identifier')
@api.response(404, 'Game not found')
class GameItem(Resource):
    @api.doc('get_game')
    @api.marshal_with(game)
    def get(self, id):
        """Fetch a game given its identifier"""
        return Game.query.get_or_404(id)

    @api.doc('update_game')
    @api.expect(game)
    @api.marshal_with(game)
    def put(self, id):
        """Update a game given its identifier"""
        game = Game.query.get_or_404(id)
        if 'name' in api.payload:
            game.name = api.payload['name']
        if 'url' in api.payload:
            game.url = api.payload['url']
        if 'author' in api.payload:
            game.author = api.payload['author']
        if 'published_date' in api.payload:
            game.published_date = api.payload['published_date']
        db.session.commit()
        return game

    @api.doc('delete_game')
    @api.response(204, 'Game deleted')
    def delete(self, id):
        """Delete a game given its identifier"""
        game = Game.query.get_or_404(id)
        db.session.delete(game)
        db.session.commit()
        return '', 204
