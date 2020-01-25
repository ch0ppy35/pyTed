from app import app, tasks
from getInfo import getData
from flask import render_template, redirect
from apscheduler.schedulers.background import BackgroundScheduler
import time
import atexit

scheduler = BackgroundScheduler()


@app.before_first_request
def startBackGroundJob():
    scheduler.add_job(
        getData,
        trigger='cron',
        second='*/30',
        max_instances=1
    )
    scheduler.add_job(
        tasks.dailyTasks,
        trigger='cron',
        hour='23',
        minute='59'
    )
    scheduler.add_job(
        tasks.weeklyTasks,
        trigger='cron',
        week='*'
    )
    scheduler.start()

    # Fire off get data & give time for new data to be inserted.
    getData()
    time.sleep(5)


@app.route('/')
def index():
    return render_template(
        'index.html',
        currentStatus=tasks.qryCurrent(),
        voltageStats=tasks.qryVoltage(),
        killawattStats=tasks.qryKillawatt(),
        dayKwhTotal=tasks.qryDayKwhTotal(),
        kwh7dTotal=tasks.qryKwh7dTotal(),
        kwhPrevWk=tasks.qryKwhPrevWk(),
        pws=app.config['PWS']
    )


@app.route('/runtasks')
def runTasks():
    tasks.dailyTasks()
    tasks.weeklyTasks()
    return redirect('/')

@atexit.register
def end():
    scheduler.shutdown()
