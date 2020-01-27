import psycopg2
from app import app


class MyDatabase():
    def __init__(self):
        self.conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='pyted',
                                     user=app.config['DBUSER'], password=app.config['DBPASS'])

    def query(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.close()
        return result

    def queryJ(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        r = [dict((self.cur.description[i][0], value)
                  for i, value in enumerate(row)) for row in self.cur.fetchall()]
        self.close()
        return r  # (r[0] if r else None) if one else r

    def modifyq(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
        self.close()

    def close(self):
        self.cur.close()
        self.conn.close()
