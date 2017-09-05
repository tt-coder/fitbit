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


"""
df2 = pd.DataFrame({
    "time" : time_d,
    "temp" : temp,
    "humid" : humid
})

fig, axes = plt.subplots(nrows=2)
df2.plot(x=["time"],y=["temp"],grid=True,ax=axes[0])
axes[0].set_title("Temperature")
axes[0].get_xaxis().set_major_formatter(mdates.DateFormatter("%H:%M"))
df2.plot(x=["time"],y=["humid"],grid=True,ax=axes[1])
axes[1].get_xaxis().set_major_formatter(mdates.DateFormatter("%H:%M"))
axes[1].set_title("Humid")
plt.tight_layout()
"""

"""
def importdict(filename):#creates a function to read the csv
    #create data frame from csv with pandas module
    df=pd.read_csv(filename+'.csv', names=['Time', 'Temp', 'Humid'],sep=',',parse_dates=[0]) #or:, infer_datetime_format=True)
    fileDATES=df.T.to_dict() #.values()#export the data frame to a python dictionary
    return fileDATES #return the dictionary to work with it outside the function
if __name__ == '__main__':
    fileDATES = importdict('2017-09-04-data') #start the function with the name of the file
    print(fileDATES.items(0))
"""