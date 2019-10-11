#! /usr/bin/env python
from flask import Response, Flask, render_template, flash, request ,url_for, jsonify, make_response
from classes import Processing
import json
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'bc5eedbdc41a5742e6ee2c0a8f34376f'

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/process', methods=['POST', 'GET'])
def register():
    print(request.form)
    if request.form:
        print(request.form.get('text'))
        question = request.form.get('text')
        
        question = Processing(question)
        question.question_process()
        question.wiki_process()
        data = question.answer_question
        

        return json.dumps(data)
    else:
        return ''
    # traiter les donnees recues
        # affiicher : "Bonjour mon enfant"
