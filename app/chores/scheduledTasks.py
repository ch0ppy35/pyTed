from app import app
from app.chores import cronTasks
import time
from app.tools import getInfo
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


scheduler = BackgroundScheduler()
meterRead = app.config['METERREAD']


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


@atexit.register
def end():
    # Prevent an unhealthy shutdown
    if scheduler.running:
        scheduler.shutdown()
        app.logger.info('~ Scheduler is shutting down ~')
    else:
        app.logger.info("~ Scheduler isn't running, not attempting shutdown ~")
