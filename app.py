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


@app.route("/api/post_question", methods=['POST'])
def post_question():
    text = request.args.get('question', '')
    
    answer = handle_question(text)
    
    print answer

    return json.dumps({'answer': answer})


def handle_question(text):
    
    count = 10
    top_text = "top text here"
    top_link = "top link"
    rel_text = "related text"
    rel_link = "related link"
    related_keyword_text = "related_keyword_text"

    answer = {
            "top_mentions":{
                "count": count,
                "documents":[{
                    "text": top_text,
                    "link": top_link
                }]
            },
            "related_spend":{
                "documents":[{
                    "text": rel_text,
                    "link": rel_link,
                }]
            },
            "related_keyword":{
                "keyword": [{
                    "text": related_keyword_text,
                }]
            }
        }

    return answer


@app.route("/api/get_question", methods=['POST'])
def get_question():
    prev_question = g.dv.execute("SELECT question FROM question").fetchall()
    prev_question = "hello"

    return json.dumps({'prev_question': prev_question})


if __name__ == "__main__":
    app.run(debug=True)
