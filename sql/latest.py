import psycopg2
from app import app
import time
from sql import initialTblSetup

neededDbVer = 0.1
thisDbVer = 1.0
conn = psycopg2.connect(
    host=app.config['DBHOST'],
    port=app.config['DBPORT'],
    database=app.config['DBDB'],
    user=app.config['DBUSER'],
    password=app.config['DBPASS']
)


def dbVerCheck(dbVer):
    if dbVer < neededDbVer:
        app.logger.info('Database Ver too low, updating...')
        initialTblSetup.tblSetup()
    else:
        app.logger.info('~ Database ready to update! ~')
        tblSetup()


def tblSetup():

    sql = (
        """
    DROP TABLE IF EXISTS kwhTotalsWeek;
    """,
        """
    INSERT INTO pytedDbVer(dbver) VALUES(%(s)s);
    """ % {'s': thisDbVer}
    )

    cur = conn.cursor()

    for command in sql:
        cur.execute(command)
    conn.commit()
    cur.close()

    app.logger.info('Database updated!...Starting pyTed')
    time.sleep(5)
