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
        tblSetup()

    else:
        app.logger.info('~ pyTed db exists!...Checking db version. ~')
        dbVerCheck()
        time.sleep(1)


def dbVerCheck():
    dbVer = float(app.config['DBVER'])
    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='pyted',
                            user=app.config['DBUSER'], password=app.config['DBPASS'])
    sql = """
    SELECT dbver FROM
    pytedDbVer 
    ORDER BY ts DESC 
    LIMIT 1;
    """
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()[0][0]
    if result < dbVer:
        app.logger.info('(!) Database out of date! Database Version: '
                        + result
                        + 'Database should be: '
                        + dbVer)
        app.logger.info('Updating Database...')
        # run file
    else:
        app.logger.info('~ Database up to date! ~')


def dbSetup():
    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='postgres',
                            user=app.config['DBUSER'], password=app.config['DBPASS'])
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    sql = """
    CREATE DATABASE %(s)s; 
    """ % {'s': app.config['DBDB']}
    cur.execute(sql)
    cur.close()
    conn.commit()

    app.logger.info('Database created!')

    time.sleep(5)

def tblSetup():
    app.logger.info('Creating Tables...')

    sql = (
        """
    CREATE TABLE IF NOT EXISTS killawatts (
    id serial NOT NULL PRIMARY KEY,
    killawatts real,
    ts timestamp without time zone DEFAULT now()
    );
    """,
        """
    CREATE TABLE IF NOT EXISTS kwhTotals (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE IF NOT EXISTS kwhTotalsDay (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE IF NOT EXISTS kwhTotalsWeek (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE IF NOT EXISTS kwhTotalsMonth (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE IF NOT EXISTS Voltage (
    id serial NOT NULL PRIMARY KEY,
    voltage real,
    ts timestamp without time zone DEFAULT now()
    );
    """,
        """
    CREATE TABLE IF NOT EXISTS pytedDbVer (
    id serial NOT NULL PRIMARY KEY,
    dbver real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    INSERT INTO pytedDbVer(dbver) VALUES(%(s)s);
    """ % {'s': app.config['DBVER']},
        """
    INSERT INTO kwhTotalsDay(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO kwhTotalsWeek(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO kwhTotalsMonth(kwhtotal) VALUES(0);
    """
    )

    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database=app.config['DBDB'],
                            user=app.config['DBUSER'], password=app.config['DBPASS'])
    cur = conn.cursor()

    for command in sql:
        cur.execute(command)
    cur.close()

    conn.commit()

    app.logger.info('Database setup!...Starting pyTed')
    time.sleep(5)
