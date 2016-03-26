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
def home(ip=None):
    ip_lookup = pyipinfodb.IPInfo(private.IP_INFO_TOKEN)
    response = ip_lookup.get_city()
    postcode = response['zipCode']
    city = response['cityName']
    
    prev_question = g.db.execute("SELECT question FROM question").fetchall()

    return render_template('index.html', postcode=postcode, city=city, prev_question=prev_question)


@app.route("/api", methods=['GET'])
def api():
    """Return a message from query."""
    text = request.args.get('question', '')
    
    g.db.execute("INSERT INTO question (question) VALUES (?)", [text]);
    g.db.commit()
    
    return json.dumps({'answer': text})


def handle_query(text):
    answer = text

    return answer


if __name__ == "__main__":
    app.run(debug=True)
