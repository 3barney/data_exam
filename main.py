# Part 1: Retrieving raw data
# There is an API, allowing you to fetch the currencies values against the EUR:
# https://api.exchangeratesapi.io/latest
# You will need to write a script to fetch the currencies every 5 minutes and store them in postgres.
from fetch import FetchRecords
from transform import TransformRecords

recordsQuery = FetchRecords()
recordsQuery.fetch()


# Part 2: Transforming the data
# You will need to fetch every 1 hour the latest data entered in Part 1 and return:
# ● The minimum
# ● The maximum
# ● The average
# ● The median
# For each of the currencies against the EUR during this 1 hour.
recordsTransform = TransformRecords()
recordsTransform.transform()


# Part 3: Saving the data
# Now that you defined a new data structure in Part 2, let’s save it in a new table in postgres and create an SQL view against it to obtain:
# ● The minimum
# ● The maximum
# ● The average
# ● The median
# For each of the currencies against the EUR for the current day.
