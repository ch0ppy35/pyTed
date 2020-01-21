from app import app, database, tasks
from getInfo import getData
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler
import time

@app.before_first_request
def startBackGroundJob():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        getData,
        trigger='cron',
        second='*/30'
    )
    scheduler.add_job(
        tasks.dailyTasks,
        trigger='cron',
        hour='23',
        minute='59'
    )
    scheduler.start()

    #Fire off get data & give time for new data to be inserted.
    getData()
    time.sleep(5)
def qryCurrent():
    sql = """
    SELECT v.voltage, k.killawatts
    FROM voltage v
         INNER JOIN killawatts k ON k.ts BETWEEN v.ts AND v.ts + interval '10 s'
    ORDER BY v.id DESC
    LIMIT 10;
    """
    db = database.MyDatabase()
    #print(sql)
    return db.query(sql)

def qryVoltage():
    sql = """
    SELECT voltage, to_char(ts at time zone 'utc' at time zone 'america/new_york', 'HH:MI AM')
    FROM Voltage
    WHERE current_date = date(ts) OR ts BETWEEN ts AND ts - interval '1h'
    ORDER BY date(ts) DESC, voltage DESC
    LIMIT 1;
    """
    db = database.MyDatabase()
    #print(sql)
    return db.query(sql)

def qryKillawatt():
    sql = """
    SELECT killawatts, to_char(ts at time zone 'utc' at time zone 'america/new_york', 'HH:MI AM')
    FROM killawatts
    WHERE current_date = date(ts) OR ts BETWEEN ts AND ts - interval '1h'
    ORDER BY date(ts) DESC, killawatts DESC
    LIMIT 1;
    """
    db = database.MyDatabase()
    #print(sql)
    return db.query(sql)

@app.route('/')
def index():
    return render_template('index.html', currentStatus=qryCurrent(), voltageStats=qryVoltage(), killawattStats=qryKillawatt(), pws=app.config['PWS'])