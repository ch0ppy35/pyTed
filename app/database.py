import psycopg2
from app import app


class MyDatabase():
    def __init__(self):
        self.conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'], database='pyted',
                                     user=app.config['DBUSER'], password=app.config['DBPASS'])
    def query(self, query, columns):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        results = []
        for row in self.cur.fetchall():
            results.append(dict(zip(columns, row)))
        return results

    def close(self):
        self.cur.close()
        self.conn.close()

# Use something like this to use the class above...
#
#     db = MyDatabase()
#     columns = ('id', 'some_field1', 'some_field2')
#     results = db.query("SELECT id, some_field1, some_field2 from bah", columns)
#     db.close()
#     return results
