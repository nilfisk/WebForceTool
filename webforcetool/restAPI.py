__author__ = 'Kyah'

from flask.ext import restful
from flask import Flask

from webforcetool import database


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = restful.Api(app, catch_all_404s=True)


class RestGames(restful.Resource):
    def get(self):
        game_list = database.get_all_games()
        result = {}
        for game in game_list:
            result[game.id] = {
                'name': game.name,
                'cover_img': game.cover_img
            }
        return result


class RestGame(restful.Resource):
    def get(self, game_id):
        game = database.get_game(game_id)
        result = {
            'name': game.name,
            'desc': game.desc,
            'cover_img': game.cover_img,
            'bin_path': game.bin_path
        }
        return result


def init():
    ## Setup API
    api.add_resource(RestGames, '/games')
    api.add_resource(RestGame, '/game/<int:game_id>')
    return app