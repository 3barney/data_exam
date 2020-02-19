import psycopg2
from config import config

class Database():
    def __init__(self):
        params = config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def read(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
