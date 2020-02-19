import datetime
from statistics import mean, median
from database import Database

# Part 2: Transforming the data
# You will need to fetch every 1 hour the latest data entered in Part 1 and return:
# ● The minimum
# ● The maximum
# ● The average
# ● The median
# For each of the currencies against the EUR during this 1 hour.
class TransformRecords():

    def __init__(self):
        self.db = Database()
        self.records = None

    def readRecords(self):
        rows = self.db.read("SELECT currency, amount, date FROM  records ORDER BY record_id")
        self.records = rows


    def minimum(self):
        iterable = iter(self.records)
        (minCurr, minAmount, minDate) = iterable.__next__()

        for item in iterable:
            (currency, amount, date) = item
            if (amount < minAmount):
                minCurr, minAmount, minDate = currency, amount, date

        print("Minimum currency is {} of value {} of date {}".format(minCurr, minAmount, minDate))
        return minAmount


    def maximum(self):
        iterable = iter(self.records)
        (maxCurr, maxAmount, maxDate) = iterable.__next__()

        for item in iterable:
            (currency, amount, date) = item
            if (amount > maxAmount):
                maxCurr, maxAmount, maxDate = currency, amount, date

        print("Maximum currency is {} of value {} of date {}".format(maxCurr, maxAmount, maxDate))
        return maxAmount


    def average(self):
        currencyValue = []
        for row in self.records:
            (currency, amount, date) = row
            currencyValue.append(amount)

        print("Average currency is {}".format(mean(currencyValue)))
        return mean(currencyValue)
        


    def median(self):
        currencyValue = []
        for row in self.records:
            (currency, amount, date) = row
            currencyValue.append(amount)

        print("Median value of currency is {}".format(median(currencyValue)))
        return median(currencyValue)
     

    def transform(self):
        self.readRecords()
        min = self.minimum()
        max = self.maximum()
        av = self.average()
        med = self.median()

        self.db.cur.execute("INSERT INTO records_summary (minimum, maximum, average, median, date) VALUES (%s, %s, %s, %s, %s)",
            (min, max, av, med, datetime.date.today())
        )
        self.db.conn.commit()
        self.db.close()
        print("Record saved to DB")