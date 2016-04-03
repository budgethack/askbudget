#!/usr/bin/python
from flask import Flask, request, render_template, g
import json

import utils


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
