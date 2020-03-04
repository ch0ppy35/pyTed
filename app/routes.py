from app import app
from app.chores import cronTasks, tasks, queries
from flask import render_template, redirect, request
import atexit


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
    app.logger.info('~ pyTed is shutting down - Until next time ~')
