import requests
import json

from database import Database

# Part 1: Retrieving raw data
# There is an API, allowing you to fetch the currencies values against the EUR:
# https://api.exchangeratesapi.io/latest
# You will need to write a script to fetch the currencies every 5 minutes and store them in postgres.

# TODO: 5 minute fetch script
class FetchRecords():
    def __init__(self):
        self.db = Database()
        self.url = "https://api.exchangeratesapi.io/latest"

    def createRecordTable(self):
        self.db.query("""CREATE TABLE IF NOT EXISTS records (
            record_id  SERIAL PRIMARY KEY,
            currency VARCHAR(255) NOT NULL,
            amount float NOT NULL,
            date DATE NOT NULL
        )""")

        self.db.query("""CREATE TABLE IF NOT EXISTS records_summary (
            id  SERIAL PRIMARY KEY,
            minimum float NOT NULL,
            maximum float NOT NULL,
            average float NOT NULL,
            median float NOT NULL,
            date DATE NOT NULL
        )""")

    def insertRecord(self, currency, amount, date):
        self.db.cur.execute("INSERT INTO records (currency, amount, date) VALUES(%s,%s, %s)", (currency, amount, date))
        self.db.conn.commit()

    def getRecords(self):
        response = requests.get(self.url)
        data = response.json()

        rates = data['rates']
        base = data['base']
        date = data['date']

        print("Saving records...")
        for key, value in rates.items():
            self.insertRecord(key, value, date)
        print("Save complete...")

    def fetch(self):
        self.createRecordTable()
        self.getRecords()
        self.db.close()


