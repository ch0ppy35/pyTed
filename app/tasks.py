from app import app, database

tz = app.config['TZ']

def qryCurrent():
    sql = """
    SELECT v.voltage, k.killawatts
    FROM voltage v
         INNER JOIN killawatts k ON k.ts BETWEEN v.ts AND v.ts + interval '10S'
    ORDER BY v.id DESC
    LIMIT 10;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryDayKwhTotal():
    sql = """
    SELECT kwhtotal 
    FROM kwhTotals ORDER BY ts 
    DESC LIMIT 1;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKwh7dTotal():
    sql = """
    SELECT prevDay.kwhSum + currentDay 
    FROM (
    SELECT SUM(kwhtotal) kwhSum 
    FROM kwhTotalsDay WHERE ts > NOW() AT TIME ZONE '%(s)s' - INTERVAL '7D') AS prevDay, 
    (SELECT kwhtotal currentDay
    FROM kwhTotals ORDER BY ts DESC LIMIT 1) AS currentDay;
    """ % {'s': tz}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKwhPrevWk():
    sql = """
    SELECT kwhtotal
    FROM kwhTotalsWeek
    ORDER BY ts DESC
    LIMIT 1;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKwhPrevMn():
    sql = """
    SELECT kwhtotal
    FROM kwhTotalsMonth
    ORDER BY ts DESC
    LIMIT 1;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryVoltage():
    sql = """
    SELECT mx.voltage, TO_CHAR(mx.ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'HH:MI AM') AS mxTs,
    mn.voltage, TO_CHAR(mn.ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'HH:MI AM') AS mnTs
    FROM(
    SELECT MAX(voltage) AS mxV, MIN(voltage) AS mnV
    FROM Voltage
    WHERE (CURRENT_TIMESTAMP AT TIME ZONE '%(s)s')::DATE = 
    DATE(ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s')
    ) v
    INNER JOIN voltage mx ON mx.voltage = v.mxV
    INNER JOIN voltage mn ON mn.voltage = v.mnV
    ORDER BY mxTs DESC, mnTs DESC
    LIMIT 1;
    """ % {'s': tz}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKillawatt():
    sql = """
    SELECT mx.killawatts, TO_CHAR(mx.ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'HH:MI AM') AS mxTs,
    mn.killawatts, TO_CHAR(mn.ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'HH:MI AM') AS mnTs
    FROM(
    SELECT MAX(killawatts) AS mxK, MIN(killawatts) AS mnK
    FROM killawatts
    WHERE (CURRENT_TIMESTAMP AT TIME ZONE '%(s)s')::DATE = 
    DATE(ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s')
    ) k
    INNER JOIN killawatts mx ON mx.killawatts = k.mxK
    INNER JOIN killawatts mn ON mn.killawatts = K.mnK
    ORDER BY mxTs DESC, mnTs DESC
    LIMIT 1;
    """ % {'s': tz}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryPeakKwhDayMn():
    sql = """
    SELECT kwhtotal, TO_CHAR(ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'Mon DD')
    FROM kwhTotalsDay
    WHERE ts > NOW() AT TIME ZONE '%(s)s' - INTERVAL '1MONTH'
    ORDER BY kwhtotal DESC
    LIMIT 1;
    """ % {'s': tz}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryLowKwhDayMn():
    sql = """
    SELECT kwhtotal, TO_CHAR(ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'Mon DD')
    FROM kwhTotalsDay
    WHERE ts > NOW() AT TIME ZONE '%(s)s' - INTERVAL '1MONTH'
    ORDER BY kwhtotal ASC
    LIMIT 1;
    """ % {'s': tz}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryAvgKwhDayMn():
    sql = """
    SELECT AVG(kwhtotal) 
    FROM kwhTotalsDay 
    WHERE ts > NOW() AT TIME ZONE '%(s)s' - 
    INTERVAL '1MONTH';
    """ % {'s': tz}
    db = database.MyDatabase()
    return round(db.query(sql)[0][0], 3) or ['']


# Misc Tasks

def tskCalculateCost():
    cost = float(app.config['COST'])

    kwhDayTotal = qryDayKwhTotal()[0][0]
    kwhDayCost = round(kwhDayTotal * cost, 2)

    kwh7dTotal = qryKwh7dTotal()[0][0]
    kwh7dCost = round(kwh7dTotal * cost, 2)

    kwhPrevMnTotal = qryKwhPrevMn()[0][0]
    kwhPrevMnCost = round(kwhPrevMnTotal * cost, 2)

    kwhPeakDayMn = qryPeakKwhDayMn()[0][0]
    kwhPeakDayMnCost = round(kwhPeakDayMn * cost, 2)

    kwhLowDayMn = qryLowKwhDayMn()[0][0]
    kwhLowDayMnCost = round(kwhLowDayMn * cost, 2)

    kwhAvgDayMn = qryAvgKwhDayMn()
    kwhAvgDayMnCost = round(kwhAvgDayMn * cost, 2)

    return(
        kwhDayCost,
        kwh7dCost,
        kwhPrevMnCost,
        kwhPeakDayMnCost,
        kwhLowDayMnCost,
        kwhAvgDayMnCost
    )


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
    """
    db.modifyq(sql)

    app.logger.info("Monthly task complete")
