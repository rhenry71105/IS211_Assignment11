#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    IS 211 Assignment Week # 11.
"""
__author__ = 'Rickardo Henry'

from flask import Flask, render_template, request, redirect
import re


app = Flask(__author__)

task_to_do = []


@app.route('/')
def index():
    return render_template('index.html', task_to_do=task_to_do)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['taskName']
    priority = request.form['taskPriority']
    email = request.form['emailAddress']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority Level':
        return redirect('/')
    else:
        task_to_do.append((task, priority, email))

    print task_to_do
    return redirect('/')


@app.route('/clearAllTasks', methods=['POST', 'GET'])
def clear():
    del task_to_do[:]
    return redirect('/')


if __author__ == 'Rickardo Henry':
    app.run(debug=True)
