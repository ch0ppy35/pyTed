from app.tools import getInfo
from app import app, tasks, cronTasks, queries
from flask import render_template, redirect, request
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
        cronTasks.dailyTasks,
        trigger='cron',
        hour='23',
        minute='59'
    )
    scheduler.add_job(
        cronTasks.weeklyTasks,
        trigger='cron',
        day_of_week='sun',
        hour='0',
        minute='0'
    )
    scheduler.add_job(
        cronTasks.monthlyTasks,
        trigger='cron',
        day='%(s)s' % {'s': meterRead},
        hour='0',
        minute='0'
    )
    scheduler.start()
    app.logger.info('~ Scheduler starting for for tasks ~')

    # Fire off get data & give time for new data to be inserted.
    getInfo.getData()
    time.sleep(1)


@app.route('/')
def index():
    return render_template(
        'index.html',
        currentStatus=queries.qryCurrent(),
        voltageStats=queries.qryVoltage(),
        killawattStats=queries.qryKillawatt(),
        dayKwhTotal=queries.qryDayKwhTotal(),
        kwh7dTotal=queries.qryKwh7dTotal(),
        kwhPrevMn=queries.qryKwhPrevMn(),
        kwhCost=tasks.tskCalculateCost(),
        peakKwhDayMn=queries.qryPeakKwhDayMn(),
        lowKwhDayMn=queries.qryLowKwhDayMn(),
        avgKwhDayMn=queries.qryAvgKwhDayMn(),
        bills=tasks.tskGetBills(),
        pws=app.config['PWS']
    )


@app.route('/rtkw')
def rtkw():
    currentStatus = queries.qryCurrent()
    value = str(currentStatus[0][2])
    return value


@app.route('/about')
def about():
    return render_template(
        'about.html',
        version=app.config['VERSION'],
        dbver=app.config['DBVER']
    )


@app.route('/bills')
def bills():
    return render_template('about.html')


@app.route('/billData')
def billData():
    bid = request.args.get('billid')
    if bid is None:
        return redirect('/')

    return render_template(
        'billData.html',
        billData=tasks.tskGetBillingData(bid)
    )


@app.route('/runtasks')
def runTasks():
    cronTasks.dailyTasks()
    cronTasks.monthlyTasks()
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
