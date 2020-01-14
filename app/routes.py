from app import app
from getInfo import getData
from flask_executor import Executor
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import time
import psycopg2
import threading

executor = Executor(app)
@app.before_first_request
def startBackGroundJob():
        threading.Thread(target=activateJob).start()
def activateJob():
    executor.submit(getData())
def qryCurrent():
    conndb = psycopg2.connect(host='HOST', port='PORT', database='pyted', user='USER', password='PASSWORD')
    sql = "select * from voltage ORDER BY id DESC LIMIT 1;"
    qry = conndb.cursor()
    qry.execute(sql)
    results = (qry.fetchall())
    print(results)
    return('</br>'.join(str(e) for e in results))

@app.route('/')
@app.route('/index')
def index():
    return (qryCurrent())