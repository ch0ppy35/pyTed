import psycopg2
from app import app


class MyDatabase():
    def __init__(self):
        self.conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database=app.config['DBDB'],
                                     user=app.config['DBUSER'], password=app.config['DBPASS'])

    def query(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.close()
        return result

    def modifyq(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
        self.close()

    def close(self):
        self.cur.close()
        self.conn.close()
