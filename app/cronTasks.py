from app import app, database
tz = app.config['TZ']

# Cron Tasks

def dailyTasks():
    db = database.MyDatabase()
    sql = """
    INSERT INTO kwhTotalsDay(kwhtotal) VALUES((
    SELECT kwhtotal FROM kwhTotals 
    ORDER BY ts DESC 
    LIMIT 1));
    """
    db.modifyq(sql)

    db = database.MyDatabase()
    sql = """
    DELETE FROM kwhTotals
    WHERE ts < NOW() AT TIME ZONE '%(s)s' - INTERVAL '7D';   
    """ % {'s': tz}
    db.modifyq(sql)
    app.logger.info("Daily task complete")


def weeklyTasks():
    db = database.MyDatabase()
    sql = """
    INSERT INTO kwhTotalsWeek(kwhtotal) VALUES((
    SELECT SUM(kwhtotal) FROM(
    SELECT * FROM kwhTotalsDay
    ORDER BY ts DESC LIMIT 7)
    ));
    """
    db.modifyq(sql)
    app.logger.info("Weekly task complete")


def monthlyTasks():
    db = database.MyDatabase()
    sql = """
    INSERT INTO kwhTotalsMonth(kwhtotal) VALUES((
    SELECT SUM(kwhtotal) FROM(
    SELECT * FROM kwhTotalsDay
    WHERE ts > NOW() AT TIME ZONE '%(s)s' - INTERVAL '1MONTH')k)
    );
    """ % {'s': tz}
    db.modifyq(sql)

    app.logger.info("Monthly task complete")
