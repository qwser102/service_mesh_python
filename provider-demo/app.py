# -- coding: utf-8 --
from flask import Flask,request
import time
# import logging

app = Flask(__name__)


@app.route('/')
def auto_call():
    str = time.ctime() + " " + "This is from provider"
    return str


@app.route('/test')
def receve_data():
    if request.form.get("param") != None:
        get_str = request.form.get("param")
    else:
        get_str = request.args.get("param")
    str = time.ctime() + " " + "provider received param : " + get_str
    return str


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)
