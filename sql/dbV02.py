import psycopg2
from app import app
import time
from sql import initialTblSetup

neededDbVer = 0.1
thisDbVer = 0.2

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
    CREATE TABLE IF NOT EXISTS killawattsTest (
    id serial NOT NULL PRIMARY KEY,
    killawatts real,
    ts timestamp without time zone DEFAULT now()
    );
    """,
        """
    INSERT INTO killawattsTest(killawatts) VALUES(52.56);
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
