from app import app, tasks, getInfo
from flask import render_template, redirect
from apscheduler.schedulers.background import BackgroundScheduler
import time
import atexit

scheduler = BackgroundScheduler()
meterRead = app.config['METERREAD']

@app.before_first_request
def startBackGroundJob():
    scheduler.add_job(
        getInfo.getData,
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
        day_of_week='sun',
        hour='0',
        minute='0'
    )
    scheduler.add_job(
        tasks.monthlyTasks,
        trigger='cron',
        day='%(s)s' % {'s': meterRead},
        hour='0',
        minute='0'
    )
    scheduler.start()
    app.logger.info('~ Scheduler starting for for tasks ~')

    # Fire off get data & give time for new data to be inserted.
    getInfo.getData()
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
        kwhPrevMn=tasks.qryKwhPrevMn(),
        kwhCost=tasks.tskCalculateCost(),
        peakKwhDayMn=tasks.qryPeakKwhDayMn(),
        lowKwhDayMn=tasks.qryLowKwhDayMn(),
        pws=app.config['PWS']
    )


@app.route('/rtkw')
def rtkw():
    currentStatus = tasks.qryCurrent()
    value = str(currentStatus[0][1])
    return value


@app.route('/about')
def about():
    return render_template(
        'about.html',
        version=app.config['VERSION']
    )


@app.route('/runtasks')
def runTasks():
    tasks.dailyTasks()
    print(tasks.tskCalculateCost())
    return redirect('/')


@atexit.register
def end():
    # Prevent an unhealthy shutdown
    if scheduler.running:
        scheduler.shutdown()
        app.logger.info('~ Scheduler is shutting down ~')
    else:
        app.logger.info("~ Scheduler isn't running, not attempting shutdown ~")
    app.logger.info('~ pyTed is shutting down - Until next time ~')
