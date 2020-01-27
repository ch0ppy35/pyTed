from app import app, database
import json


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

def qryCurrentJson():
    sql = """
    SELECT v.ts, v.voltage, k.killawatts
    FROM voltage v
         INNER JOIN killawatts k ON k.ts BETWEEN v.ts AND v.ts + interval '10 s'
    ORDER BY v.id DESC
    LIMIT 5;
    """
    db = database.MyDatabase()
    return db.queryJ(sql)

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
    SELECT mx.voltage, TO_CHAR(mx.ts AT TIME ZONE 'utc' AT TIME ZONE 'america/new_york', 'HH:MI AM'),
    mn.voltage, TO_CHAR(mn.ts AT TIME ZONE 'utc' AT TIME ZONE 'america/new_york', 'HH:MI AM')
    FROM(
    SELECT MAX(voltage) AS mxV, MIN(voltage) AS mnV
    FROM Voltage
    ) v
    INNER JOIN voltage mx ON mx.voltage = v.mxV
    INNER JOIN voltage mn ON mn.voltage = v.mnV
    WHERE CURRENT_DATE = date(mn.ts);
    """
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryKillawatt():
    sql = """
    SELECT mx.killawatts, TO_CHAR(mx.ts AT TIME ZONE 'utc' AT TIME ZONE 'america/new_york', 'HH:MI AM') AS mxTs,
    mn.killawatts, TO_CHAR(mn.ts AT TIME ZONE 'utc' AT TIME ZONE 'america/new_york', 'HH:MI AM') AS mnTs
    FROM(
    SELECT MAX(killawatts) AS mxK, MIN(killawatts) AS mnK
    FROM killawatts
    ) k
    INNER JOIN killawatts mx ON mx.killawatts = k.mxK
    INNER JOIN killawatts mn ON mn.killawatts = K.mnK
    WHERE CURRENT_DATE = date(mn.ts) OR mn.ts > NOW() - INTERVAL '1m'
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
