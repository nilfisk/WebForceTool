__author__ = 'Kyah'

from flask import Flask
from flask import render_template

from webforcetool import database


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/game/<int:game_id>')
@app.route('/game/')
def game(game_id=None):
    if game_id is None:
        game_id = 1
    game = database.get_game(game_id)
    return render_template("item.html", game=game)


@app.route('/index/')
@app.route('/games/')
@app.route('/')
def index():
    return render_template("index.html")


def init():
    return app
