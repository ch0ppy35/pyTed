import psycopg2
import time
import logging
from scraper import goget
from xml.etree.ElementTree import fromstring, ElementTree
from app import app

conndb = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='pyted',
                          user=app.config['DBUSER'], password=app.config['DBPASS'])


def getData():
    while True:
        data = goget()
        tree = ElementTree(fromstring(data))
        root = tree.getroot()

        #   Get Data
        voltageNow = (float(root.getchildren()[2].getchildren()[0].getchildren()[0].text) / 10)
        wattsNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[0].text) / 1000)

        #   Build & execute Query
        #   Voltage
        sql = 'INSERT INTO Voltage(voltage) VALUES(%s);'
        qry = conndb.cursor()
        qry.execute(sql, [voltageNow])
        conndb.commit()
        qry.close()

        #   Watts
        sql = 'INSERT INTO killawatts(killawatts) VALUES(%s);'
        qry = conndb.cursor()
        qry.execute(sql, [wattsNow])
        qry.close()

        #print('Updated!')
        app.logger.setLevel(logging.INFO)
        app.logger.info('Updated the DB with fresh data')
        time.sleep(30)
