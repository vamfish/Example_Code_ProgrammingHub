import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('stuffToPlot.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")

def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value)VALUES(?,?,?,?)", (unix, date, keyword,value))

conn.commit()
time.sleep(1)

def read_from_db():
    c.execute('SELECT * FROMstuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

c.execute('SELECT * FROM stuffToPlot WHERE value=3')
