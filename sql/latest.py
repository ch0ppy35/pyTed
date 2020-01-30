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
    idKwhTotalsMn REAL,
    totalDays REAL,
    ts TIMESTAMP WITHOUT TIME ZONE DEFAULT now()
    );
    """,
        """
    INSERT INTO bills(idKwhTotalsMn, totalDays) 
    VALUES(0, 0);
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
