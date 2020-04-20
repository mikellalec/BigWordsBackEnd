import os
import sqlite3
from flask import Flask, g, render_template, url_for, request, make_response, jsonify
from flask_cors import CORS

# path from root folder to datbase
DATABASE = 'data/game.db'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)

    @app.route('/', methods=['GET', 'POST'])
    def main():
        if request.method == 'POST':
            print(request.form['username'])
            print(request.form['password'])
            return "success"
        else:
            return render_template('index.html')

    @app.route('/getSpellBinder/<id>', methods=['GET'])
    def getSpellBinderGame(id):
        result = query_db("SELECT item FROM SpellBinderLessons S WHERE S.id= (?)", [id])
        return jsonify(result)

    @app.route('/getSortGame/<id>', methods=['GET'])
    def getSortGame(id):
        result = query_db("SELECT item FROM SortActivityLessons S where S.id= (?)", [id])
        return jsonify(result)

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return app

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    # format query so it's returnable with basic layout
    result_string = ''
    for item in rv:
        result_string += (item[0]+" ")
    return result_string
