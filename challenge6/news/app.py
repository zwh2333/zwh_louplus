#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, json
from flask import Flask, render_template, abort

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.errorhandler(404)
def not_found(error):
	return render_template("404.html"),404

json_path = "/home/shiyanlou/files"
@app.route("/")
def index():
    l1 = []
    for r, d, f in os.walk(json_path):
        for file1 in f:
            file_path = os.path.join(r, file1)
            with open(file_path, "r") as e: 
                l1.append(json.load(e))
    return render_template("index.html", l1=l1)

@app.route("/files/<filename>")
def file(filename):
    l2 = []
    for r, d, f in os.walk(json_path):
        for file1 in f:
            file_path = os.path.join(r, file1)
            with open(file_path, "r") as e: 
                l2.append(json.load(e))
    if filename == "helloworld":
    	return render_template("file.html", l=l2[0])
    elif filename == "helloshiyanlou":
    	return render_template("file.html", l=l2[1])
    else:
    	abort(404)

if __name__ == "__main__":
    app.run(port=3000)

