import psycopg2
from app import app
import time


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
    INSERT INTO kwhTotalsDay(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO kwhTotalsWeek(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO kwhTotalsMonth(kwhtotal) VALUES(0);
    """,
        """
    INSERT INTO pytedDbVer(dbver) VALUES(%(s)s);
    """ % {'s': app.config['DBVER']}
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
