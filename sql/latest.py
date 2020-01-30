import psycopg2
from app import app
import time
from sql import initialTblSetup

neededDbVer = 0.1
thisDbVer = 0.3


def dbVerCheck(dbVer):
    if dbVer < neededDbVer:
        app.logger.info('Database Ver too low, updating...')
        initialTblSetup.tblSetup()
    else:
        app.logger.info('~ Database ready to update! ~')
        tblSetup(dbVer)


def tblSetup(dbVer):

    sql = (
        """
    CREATE TABLE IF NOT EXISTS bills (
    id serial NOT NULL PRIMARY KEY,
    totalKwhUsage REAL,
    totalCost REAL,
    avgKwhUsage REAL,
    peakKwhUsage REAL,
    peakKwhDate VARCHAR(6),
    lowKwhUsage REAL,
    lowKwhDate VARCHAR(6),
    ts TIMESTAMP WITHOUT TIME ZONE DEFAULT now()
    );
    """,
        """
    INSERT INTO bills(totalKwhUsage, 
    totalCost, avgKwhUsage, peakKwhUsage, 
    peakKwhDate, lowKwhUsage, lowKwhDate) 
    VALUES(0, 0, 0, 0, 'n/a', 0, 'n/a');
    """,
        """
    INSERT INTO pytedDbVer(dbver) VALUES(%(s)s);
    """ % {'s': dbVer}
    )

    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database=app.config['DBDB'],
                            user=app.config['DBUSER'], password=app.config['DBPASS'])
    cur = conn.cursor()

    for command in sql:
        cur.execute(command)
    conn.commit()
    cur.close()

    app.logger.info('Database updated!...Starting pyTed')
    time.sleep(5)
