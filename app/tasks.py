from app import app, database


def qryCurrent():
    sql = """
    SELECT v.voltage, k.killawatts
    FROM voltage v
         INNER JOIN killawatts k ON k.ts BETWEEN v.ts AND v.ts + interval '10 s'
    ORDER BY v.id DESC
    LIMIT 10;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryDayKwhTotal():
    sql = """
    SELECT kwhtotal 
    FROM kwhTotals ORDER BY ts DESC LIMIT 1;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKwh7dTotal():
    sql = """
    SELECT prevDay.kwhSum + currentDay 
    FROM (
    SELECT SUM(kwhtotal) kwhSum 
    FROM kwhTotalsDay WHERE ts > NOW() - INTERVAL '7d') AS prevDay, 
    (SELECT kwhtotal currentDay
    FROM kwhTotals ORDER BY ts DESC LIMIT 1) AS currentDay;
    """
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


def qryVoltage():
    sql = """
    SELECT mx.voltage, TO_CHAR(mx.ts AT TIME ZONE 'utc' AT TIME ZONE 'AMERICA/NEW_YORK', 'HH:MI AM') AS mxTs,
    mn.voltage, TO_CHAR(mn.ts AT TIME ZONE 'utc' AT TIME ZONE 'AMERICA/NEW_YORK', 'HH:MI AM') AS mnTs
    FROM(
    SELECT MAX(voltage) AS mxV, MIN(voltage) AS mnV
    FROM Voltage
    WHERE (CURRENT_TIMESTAMP AT TIME ZONE 'AMERICA/NEW_YORK')::DATE = 
    DATE(ts AT TIME ZONE 'UTC' AT TIME ZONE 'AMERICA/NEW_YORK')
    ) v
    INNER JOIN voltage mx ON mx.voltage = v.mxV
    INNER JOIN voltage mn ON mn.voltage = v.mnV
    ORDER BY mxTs DESC, mnTs DESC
    LIMIT 1;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKillawatt():
    sql = """
    SELECT mx.killawatts, TO_CHAR(mx.ts AT TIME ZONE 'UTC' AT TIME ZONE 'AMERICA/NEW_YORK', 'HH:MI AM') AS mxTs,
    mn.killawatts, TO_CHAR(mn.ts AT TIME ZONE 'UTC' AT TIME ZONE 'AMERICA/NEW_YORK', 'HH:MI AM') AS mnTs
    FROM(
    SELECT MAX(killawatts) AS mxK, MIN(killawatts) AS mnK
    FROM killawatts
    WHERE (CURRENT_TIMESTAMP AT TIME ZONE 'AMERICA/NEW_YORK')::DATE = 
    DATE(ts AT TIME ZONE 'UTC' AT TIME ZONE 'AMERICA/NEW_YORK')
    ) k
    INNER JOIN killawatts mx ON mx.killawatts = k.mxK
    INNER JOIN killawatts mn ON mn.killawatts = K.mnK
    ORDER BY mxTs DESC, mnTs DESC
    LIMIT 1;
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


# Cron Tasks

def dailyTasks():
    db = database.MyDatabase()
    sql = """
    INSERT INTO kwhTotalsDay(kwhtotal) VALUES((
    SELECT kwhtotal FROM kwhTotals 
    ORDER BY ts DESC LIMIT 1));
    """
    db.modifyq(sql)

    db = database.MyDatabase()
    sql = """
    DELETE FROM kwhTotals
    WHERE ts < NOW() - INTERVAL '7 days';
    """
    db.modifyq(sql)
    app.logger.info("Daily task complete")


def weeklyTasks():
    db = database.MyDatabase()
    sql = """
    INSERT INTO kwhTotalsWeek(kwhtotal) VALUES((
    SELECT kwhtotal FROM kwhTotalsDay 
    ORDER BY ts DESC LIMIT 1));
    """
    db.modifyq(sql)
    app.logger.info("Weekly task complete")
