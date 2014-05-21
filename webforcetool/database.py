__author__ = 'Kyah'

from webforcetool import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    desc = db.Column(db.Text())
    bin_path = db.Column(db.Text())
    cover_img = db.Column(db.LargeBinary())

    def __init__(self, name, desc, bin_path, cover_img):
        self.name = name
        self.desc = desc
        self.bin_path = bin_path
        self.cover_img = cover_img


def init():
    ## Initiate Database
    db.create_all()


def get_all_games():
    return Game.query.all()


def get_game(game_id):
    return Game.query.get(game_id)


def add_game(name, desc, bin_path, cover_img):
    new_game = Game(name, desc, bin_path, cover_img)
    db.session.add(new_game)
    try:
        db.session.commit()
        return True
    except Exception as e:
        print "This game is already in the database"
        db.session.rollback()
        return False