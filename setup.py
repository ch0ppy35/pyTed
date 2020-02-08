import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app import app
import time
from sql import initialTblSetup
dbVer = float(app.config['DBVER'])

conn0 = psycopg2.connect(
    host=app.config['DBHOST'],
    port=app.config['DBPORT'],
    database='postgres',
    user=app.config['DBUSER'],
    password=app.config['DBPASS']
)


def dbCheck():
    sql = """
    SELECT EXISTS(
     SELECT datname FROM pg_catalog.pg_database 
     WHERE LOWER(datname) = LOWER('%(s)s')
    );
    """ % {'s': app.config['DBDB']}
    cur = conn0.cursor()
    cur.execute(sql)
    result = cur.fetchall()[0][0]
    cur.close()

    if not result:
        app.logger.info('(!) Database does not exist! Running setup!')
        time.sleep(5)
        dbSetup()
        initialTblSetup.tblSetup()

    else:
        app.logger.info('~ pyTed db exists!...Checking db version. ~')
        dbVerCheck()
        time.sleep(1)


def dbVerCheck():
    sql = """
    SELECT dbver FROM
    pytedDbVer 
    ORDER BY ts DESC 
    LIMIT 1;
    """
    conn1 = psycopg2.connect(
        host=app.config['DBHOST'],
        port=app.config['DBPORT'],
        database=app.config['DBDB'],
        user=app.config['DBUSER'],
        password=app.config['DBPASS']
    )
    cur = conn1.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()[0][0] or 0.0
    except (psycopg2.errors.UndefinedTable, psycopg2.ProgrammingError):
        app.logger.warning(' Version table does not exist!...setting db ver to 0.0')
        result = 0.0
    cur.close()
    conn1.commit()
    if result == 0.0:
        app.logger.warning('(!) Database Error, rerunning initial setup!')
        initialTblSetup.tblSetup()
    elif result < dbVer:
        app.logger.info('(!) Database out of date!')
        app.logger.info('Updating Database...')
        from sql import latest
        latest.dbVerCheck(dbVer)
    else:
        app.logger.info('~ Database up to date! ~')


def dbSetup():
    conn0.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn0.cursor()
    sql = """
    CREATE DATABASE %(s)s; 
    """ % {'s': app.config['DBDB']}
    cur.execute(sql)
    cur.close()
    conn0.commit()

    app.logger.info('Database created!')

    time.sleep(5)
