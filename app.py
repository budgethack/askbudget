#!/usr/bin/python
from flask import Flask, request, render_template, g
import json
import wit
import pyipinfodb
import private
import sqlite3 

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


@app.route("/api/question", methods=['GET'])
def question():
    text = request.args.get('question', '')
    print "text: " + text

    return json.dumps({'answer': text})


def handle_query(text):
    answer = text

    return answer


if __name__ == "__main__":
    app.run(debug=True)
