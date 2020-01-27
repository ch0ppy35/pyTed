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
    cur.close()
    conn.commit()

    app.logger.info('Database created!')

    time.sleep(5)

def tblSetup():
    app.logger.info('Creating Tables...')

    sql = (
        """
    CREATE TABLE killawatts (
    id serial NOT NULL PRIMARY KEY,
    killawatts real,
    ts timestamp without time zone DEFAULT now()
    );
    """,
        """
    CREATE TABLE kwhTotals (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE kwhTotalsDay (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE kwhTotalsWeek (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE kwhTotalsMonth (
    id serial NOT NULL PRIMARY KEY,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
    );
    """,
        """
    CREATE TABLE Voltage (
    id serial NOT NULL PRIMARY KEY,
    voltage real,
    ts timestamp without time zone DEFAULT now()
    );
    """,
        """
    INSERT INTO kwhTotalsDay(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO kwhTotalsWeek(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO kwhTotalsMonth(kwhtotal) VALUES(0);
    """)

    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database=app.config['DBDB'],
                            user=app.config['DBUSER'], password=app.config['DBPASS'])
    cur = conn.cursor()

    for command in sql:
        cur.execute(command)
    cur.close()

    conn.commit()

    app.logger.info('Database setup!...Starting pyTed')
    time.sleep(5)
