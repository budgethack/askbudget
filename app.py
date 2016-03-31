#!/usr/bin/python
from flask import Flask, request, render_template, g
import json
import sqlite3

import utils


app = Flask(__name__)


# for database connection
@app.before_request
def before_request():
    g.db = sqlite3.connect("data/askbudget_db")


# for database close connection
@app.teardown_request
def teardown_request(excpection):
    if hasattr(g, 'db'):
        g.db.close()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/project")
def project():
    return render_template('project.html')


@app.route("/api/post_question", methods=['POST'])
def create_question():
    text = request.json.get('question', '')
    answer = utils.handle_text(text)
    return json.dumps({'answer': answer})


#@app.route("/api/question", methods=['GET'])
#def get_questions():
#    prev_question = g.dv.execute("SELECT question FROM question").fetchall()
#    prev_question = "hello"
#
#    return json.dumps({'prev_question': prev_question})


if __name__ == "__main__":
    app.run(debug=True)
