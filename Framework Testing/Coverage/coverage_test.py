#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

from flask import Flask, render_template, send_from_directory, request
from flask_script import Manager
from subprocess import call
import os

app = Flask(__name__, template_folder="htmlcov")


def run_test(file_path):
    call("./venv/bin/coverage run %s" % file_path, shell=True)
    call("./venv/bin/coverage html", shell=True)


@app.route("/")
def hello():
    path = request.args.get("path", mypath)
    run_test(path)
    return render_template("index.html")


@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = os.getcwd()
    _str = os.path.join(root_dir, 'htmlcov')
    return send_from_directory(_str, filename)


manager = Manager(app)


@manager.command
def run_server(file_path):
    global mypath
    mypath = file_path
    app.run(host='0.0.0.0', port=8080, debug=True)


@manager.command
def output(file_path):
    call("./venv/bin/coverage run %s" % file_path, shell=True)
    call("./venv/bin/coverage report -m", shell=True)


if __name__ == '__main__':
    manager.run()
