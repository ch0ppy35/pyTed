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
    sql = """
    SELECT v.voltage, k.killawatts
    FROM voltage v
         INNER JOIN killawatts k ON k.ts BETWEEN v.ts AND v.ts + interval '10 s'
    ORDER BY v.id DESC
    LIMIT 10;
    """
    qry = conndb.cursor()
    qry.execute(sql)
    return (qry.fetchall())

def qryVoltage():
    sql = """
    SELECT voltage, to_char(ts at time zone 'utc' at time zone 'america/new_york', 'HH:MI:AM')
    FROM Voltage
    WHERE current_date = date(ts)
    ORDER BY voltage DESC
    LIMIT 1;
    """
    qry = conndb.cursor()
    qry.execute(sql)
    return (qry.fetchall())

def qryKillawatt():
    sql = """
    SELECT killawatts, to_char(ts at time zone 'utc' at time zone 'america/new_york', 'HH:MI:AM')
    FROM killawatts
    WHERE current_date = date(ts)
    ORDER BY killawatts DESC
    LIMIT 1;
    """
    qry = conndb.cursor()
    qry.execute(sql)
    return (qry.fetchall())

@app.route('/')
def index():
    return render_template('index.html', currentStatus=qryCurrent(), voltageStats=qryVoltage(), killawattStats=qryKillawatt(), pws=app.config['PWS'])
