#!/usr/bin/python
from flask import Flask, request, render_template, g
import json

import utils


app = Flask(__name__)


@app.route("/")
def home():
    question = request.args.get('question')
    return render_template('index.html', question=question)


@app.route("/project")
def project():
    return render_template('project.html')


@app.route('/api/get_concepts', methods=['GET'])
def get_concepts():
    result = utils.handle_agg()
    return json.dumps({
        'main_concepts': [{
            'text': r['text'], 'weight': r['count'] * 100,
            'link': '?question={0}'.format(r['text'])
        } for r in result['main_concepts']['docs']]})


@app.route("/api/post_question", methods=['POST'])
def create_question():
    text = request.json.get('question', '')
    answer = utils.handle_agg(text)
    
    return json.dumps({'answer': answer})


if __name__ == "__main__":
    app.run()
