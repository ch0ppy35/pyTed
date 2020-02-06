from app import app, tasks
from app.tools import database

tz = app.config['TZ']


def qryCurrent():
    sql = """
    SELECT ROW_NUMBER() OVER (ORDER BY 1), v.voltage, k.killawatts
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


# noinspection SqlRedundantOrderingDirection
def qryLowKwhDayMn():
    sql = """
    SELECT kwhtotal, TO_CHAR(ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'Mon DD')
    FROM kwhTotalsDay
    WHERE ts > NOW() AT TIME ZONE '%(s)s' - INTERVAL '1MONTH'
    ORDER BY kwhtotal ASC
    LIMIT 1;
    """ % {'s': tz}
    db = database.MyDatabase()
    return db.query(sql) or [0]


def qryAvgKwhDayMn():
    sql = """
    SELECT AVG(kwhtotal) 
    FROM kwhTotalsDay 
    WHERE ts > NOW() AT TIME ZONE '%(s)s' - 
    INTERVAL '1MONTH';
    """ % {'s': tz}
    db = database.MyDatabase()
    return round(db.query(sql)[0][0], 3) or 0


def qryGet4Bills():
    sql = """
    SELECT id, kwhtotal, TO_CHAR(ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'Mon YYYY')
    FROM kwhTotalsMonth 
    ORDER BY ts DESC 
    LIMIT 4;
    """ % {'s': tz}
    db = database.MyDatabase()
    qryResults = tasks.tskQryToList(db.query(sql))
    return qryResults


def qryGetBillDate(id):
    sql = """
    SELECT DATE(ts)
    FROM kwhtotalsmonth 
    WHERE id = %(id)s;
    """ % {'id': id}
    db = database.MyDatabase()
    return db.query(sql) or [0]


def qryBillAvgKwh(billDate):
    sql = """
       SELECT AVG(kwhtotal) 
    FROM kwhTotalsDay 
    WHERE ts < '02-04-2020'::TIMESTAMP
    AND ts > '%(bd)s'::TIMESTAMP - INTERVAL '1MONTH';
    """ % {'s': tz, 'bd': billDate}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryBillKwhHiLo(billDate):
    sql = """
    SELECT mx.kwhtotal, TO_CHAR(mx.ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'MON DD YYYY') AS mxTs,
    mn.kwhtotal, TO_CHAR(mn.ts AT TIME ZONE 'UTC' AT TIME ZONE '%(s)s', 'MON DD YYYY') AS mnTs
    FROM(
    SELECT MAX(kwhtotal) AS mxK, MIN(kwhtotal) AS mnK
    FROM kwhTotalsDay
    WHERE ts < '02-04-2020'::TIMESTAMP
    AND ts > '%(bd)s'::TIMESTAMP - INTERVAL '1MONTH'
    ) k
    INNER JOIN kwhTotalsDay mx ON mx.kwhtotal = k.mxK
    INNER JOIN kwhTotalsDay mn ON mn.kwhtotal = K.mnK
    ORDER BY mxTs DESC, mnTs DESC
    LIMIT 1;
    """ % {'s': tz, 'bd': billDate}
    db = database.MyDatabase()
    return db.query(sql) or ['']


def qryBillKwhTotal(id):
    sql = """
    SELECT kwhtotal
    FROM kwhTotalsMonth
    WHERE id = %(id)s
    """ % {'id': id}
    db = database.MyDatabase()
    return db.query(sql) or ['']
