from xml.etree.ElementTree import fromstring, ElementTree
from app import app
from app.tools import scraper, database


def getData():
    data = scraper.goget()
    tree = ElementTree(fromstring(data))
    root = tree.getroot()
    #   Get Data
    voltageNow = (float(root[2][0][0].text) / 10)
    wattsNow = (float(root[3][0][0].text) / 1000)
    kwhTotalNow = (float(root[3][0][2].text) / 1000)

    #   Build & execute Query
    #   Voltage
    db = database.MyDatabase()
    sql = 'INSERT INTO Voltage(voltage) VALUES(%s);' % voltageNow
    db.modifyq(sql)

    #   Watts
    db = database.MyDatabase()
    sql = 'INSERT INTO killawatts(killawatts) VALUES(%s);' % wattsNow
    db.modifyq(sql)

    # kwhTotalNow
    db = database.MyDatabase()
    sql = 'INSERT INTO kwhTotals(kwhtotal) VALUES(%s);' % kwhTotalNow
    db.modifyq(sql)

    # print('Updated!')
    app.logger.info('Updated the DB with fresh data from Ted')
