import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app import app
import time


def dbCheck():
    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='postgres',
                                user=app.config['DBUSER'], password=app.config['DBPASS'])
    sql = """
    SELECT EXISTS(
     SELECT datname FROM pg_catalog.pg_database 
     WHERE LOWER(datname) = LOWER('%(s)s')
    );
    """ % {'s': app.config['DBDB']}
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()[0][0]

    if not result:
        app.logger.info('(!) Database does not exist! Running setup!')
        time.sleep(5)
        dbSetup()
    else:
        app.logger.info('~ pyTed db exists! ~')


def dbSetup():
    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='postgres',
                                user=app.config['DBUSER'], password=app.config['DBPASS'])
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    sql = """
    CREATE DATABASE %(s)s; 
    """ % {'s': app.config['DBDB']}
    cur.execute(sql)
    app.logger.info('Database created!')
    time.sleep(5)

