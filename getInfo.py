import time
import logging
from scraper import goget
from xml.etree.ElementTree import fromstring, ElementTree
from app import app, database


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
        db = database.MyDatabase()
        sql = 'INSERT INTO Voltage(voltage) VALUES(%s);' % voltageNow
        #print(sql)
        db.insertq(sql)

        #   Watts
        db = database.MyDatabase()
        sql = 'INSERT INTO killawatts(killawatts) VALUES(%s);' % wattsNow
        #print(sql)
        db.insertq(sql)

        # print('Updated!')
        app.logger.setLevel(logging.INFO)
        app.logger.info('Updated the DB with fresh data')
        time.sleep(30)
