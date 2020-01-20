from app import app
from getInfo import getData
from flask_executor import Executor
from flask import redirect, render_template
import psycopg2
import threading


executor = Executor(app)
conndb = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='pyted', user=app.config['DBUSER'], password=app.config['DBPASS'])

@app.before_first_request
def startBackGroundJob():
    threading.Thread(target=activateJob).start()

def activateJob():
    executor.submit(getData())

def qryCurrent():
    sql = "select v.voltage, k.killawatts from voltage v inner join killawatts k on k.ts between v.ts and v.ts + interval '10 s' order by v.id desc limit 10;"
    qry = conndb.cursor()
    qry.execute(sql)
    return (qry.fetchall())

def qryVoltage():
    sql = "select voltage, to_char(ts at time zone 'utc' at time zone 'america/new_york', 'HH:MI:AM') from Voltage where current_date = date(ts) order by voltage desc limit 1;"
    qry = conndb.cursor()
    qry.execute(sql)
    return (qry.fetchall())

def qryKillawatt():
    sql = "select killawatts, to_char(ts at time zone 'utc' at time zone 'america/new_york', 'HH:MI:AM') from killawatts where current_date = date(ts) order by killawatts desc limit 1;"
    qry = conndb.cursor()
    qry.execute(sql)
    return (qry.fetchall())

@app.route('/')
def index():
    return render_template('index.html', currentStatus=qryCurrent(), voltageStats=qryVoltage(), killawattStats=qryKillawatt(), pws=app.config['PWS'])
