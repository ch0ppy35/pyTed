##
## This is just the file that started it all, see get Info.py
##
import psycopg2
import threading
import time
import http.client
from xml.etree.ElementTree import fromstring, ElementTree

conndb = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='pyted', user=app.config['DBUSER'], password=app.config['DBPORT'])


def getInfo():
    while True:
        conn = http.client.HTTPConnection('dyn.beaniebot.me', 8880, 5)
        payload = ""
        headers = {
            'cache-control': "no-cache",
        }

        conn.request("GET", "/api/LiveData.xml", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        tree = ElementTree(fromstring(data))
        root = tree.getroot()

        #   Get Data
        voltageNow = (float(root.getchildren()[2].getchildren()[0].getchildren()[0].text) / 10)
        wattsNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[0].text) / 1000)
        powerToday = (float(root.getchildren()[3].getchildren()[0].getchildren()[2].text) / 1000)

        #   Build & execute Query
        sql = """INSERT INTO Voltage(voltage) VALUES(%s) RETURNING id;"""
        qry = conndb.cursor()
        qry.execute(sql, [voltageNow])
        print(qry.fetchone()[0])
        conndb.commit()
        qry.close

        #   Print the data out
        print('+--------------+')
        print(' Current Status ')
        print('+--------------+')
        print(' ', voltageNow, ' Volts')
        print('   ', wattsNow, 'kW')
        print('+--------------+')
        print('')
        print('')
        print('')
        print('+--------------+')
        print(" Today's  Usage ")
        print('+--------------+')
        print('  ', powerToday, 'kWh')
        print('+--------------+')

        time.sleep(60)


def main():
    thread = threading.Thread(target=getInfo)
    thread.start()


if __name__ == '__main__':
    main()
