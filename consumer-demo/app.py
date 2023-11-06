# --- coding: utf-8 ---
import requests
from flask import Flask,request
from apscheduler.schedulers.background import BackgroundScheduler
from config import host


scheduler = BackgroundScheduler()

app = Flask(__name__)


def job1():
    req = "http://{}:8081/test?param=consumer".format( host )
    res = requests.get(req)
    res1 = res.text
    return res1


scheduler.add_job(func=job1,trigger="interval",id="job_1",seconds=2,replace_existing=False)


@app.route("/")
def consumer():
    str = "This is from consumer"
    return str


@app.route("/test")
def test():
    param = request.args.get("param")
    req = "http://{}:8081/test?param={}".format(host,param)
    res = requests.get(req)
    res1 = res.text
    str(res1)
    return res1


if __name__ == "__main__":
    scheduler.start()
    app.debug = False
    app.run( host='0.0.0.0', port=8080 )
