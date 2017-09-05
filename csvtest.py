import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt
import csv

file = "2017-09-04-data.csv"
f = open(file,"r")
reader = csv.reader(f)

time_d = []
temp = []
humid = []

for row in reader:
    date = dt.strptime(row[0], "%Y/%m/%d %H:%M:%S")
    time_d.append(date.strftime("%H:%M"))
    temp.append(row[1])
    humid.append(row[2])
f.close()

time_d = pd.to_datetime(time_d)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(time_d, temp)

days = mdates.AutoDateLocator()
daysFmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(daysFmt)
plt.show()
