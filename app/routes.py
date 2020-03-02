from app.tools import getInfo
from app import app
from app.chores import cronTasks, tasks, queries
from flask import render_template, redirect, request
from apscheduler.schedulers.background import BackgroundScheduler
import time
import atexit

scheduler = BackgroundScheduler()
meterRead = app.config['METERREAD']


@app.before_first_request
def startBackGroundJob():
    if not app.config['TESTING']:
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
        bills=tasks.tskGetBills(4),
        pws=app.config['PWS']
    )


@app.route('/rtkw')
def rtkw():
    currentStatus = queries.qryCurrent()
    value = str(currentStatus[0][1])
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
    return render_template(
        'bills.html',
        bills=tasks.tskGetBills(10)
    )


@app.route('/billData')
def billData():
    bid = request.args.get('billid')
    if bid is None:
        return redirect('/')

    return render_template(
        'billData.html',
        billData=tasks.tskGetBillingData(bid)
    )


@app.route('/charts')
def charts():
    currentKwh = queries.qryCurrentKwh()
    kwhPrevWk = queries.qryKwhPrevWk()
    return render_template(
        'charts.html',
        currentKwh=currentKwh,
        kwhPrevWk=kwhPrevWk
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
