import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid.parasite_axes import SubplotHost
import fitbit
import json
import csv
import auth_data as ad
from datetime import datetime as dt

DATE = "2017-09-08"

time_t = []
temp = []
humid = []
time_h = []
heart = []
time_s = []
state = []

def read_csv():
    file = "./temp-data/" + DATE + "-data.csv"
    f = open(file,"r")
    reader = csv.reader(f)
    for row in reader:
        date = dt.strptime(row[0], "%Y/%m/%d %H:%M:%S")
        time_t.append(date.strftime("%H:%M"))
        temp.append(row[1])
        humid.append(row[2])
    f.close()

def get_fitbit_data():
    authd_client = fitbit.Fitbit(ad.CLIENT_ID, ad.CLIENT_SECRET,
                access_token=ad.ACCESS_TOKEN, refresh_token=ad.REFRESH_TOKEN)
    data = authd_client.sleep(date=DATE)
    data = data["sleep"][0]["minuteData"]
    for i in range(0,len(data)):
        date = data[i]["dateTime"]
        date = dt.strptime(date, "%H:%M:%S")
        time_s.append(date.strftime("%H:%M"))
        state.append(data[i]["value"])
    data = authd_client.intraday_time_series("activities/heart", DATE, detail_level="1min")
    data = data["activities-heart-intraday"]["dataset"]
    for i in range(0,len(data)):
        date = data[i]["time"]
        date = dt.strptime(date, "%H:%M:%S")
        time_h.append(date.strftime("%H:%M"))
        heart.append(data[i]["value"])

def draw_sleep_temp():
    fig = plt.figure(1)
    host = SubplotHost(fig, 111)
    par1 = host.twinx()
    par1.axis["right"].set_visible(True)
    #offset = 60, 0
    fig.add_axes(host)
    plt.subplots_adjust(right=0.75)
    host.set_xlabel("Time")
    host.set_ylabel("State")
    par1.set_ylabel("Temperature [℃]")
    host.set_xlim(time_s[0], time_s[len(time_s)-1])
    par1.set_ylim(0, 30)
    p1, = host.plot(time_s, state, label="State")
    p2, = par1.plot(time_t, temp, label="Temperature")
    host.legend()
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    days = mdates.AutoDateLocator()
    daysFmt = mdates.DateFormatter("%H:%M")
    host.xaxis.set_major_locator(days)
    host.xaxis.set_major_formatter(daysFmt)
    par1.xaxis.set_major_locator(days)
    par1.xaxis.set_major_formatter(daysFmt)
    plt.show()

def draw_sleep_humid():
    fig = plt.figure(1)
    host = SubplotHost(fig, 111)
    par1 = host.twinx()
    par1.axis["right"].set_visible(True)
    #offset = 60, 0
    fig.add_axes(host)
    plt.subplots_adjust(right=0.75)
    host.set_xlabel("Time")
    host.set_ylabel("State")
    par1.set_ylabel("Humidity [%]")
    host.set_xlim(time_s[0], time_s[len(time_s)-1])
    par1.set_ylim(0, 90)
    p1, = host.plot(time_s, state, label="State")
    p2, = par1.plot(time_t, humid, label="Humidity")
    host.legend()
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    days = mdates.AutoDateLocator()
    daysFmt = mdates.DateFormatter("%H:%M")
    host.xaxis.set_major_locator(days)
    host.xaxis.set_major_formatter(daysFmt)
    par1.xaxis.set_major_locator(days)
    par1.xaxis.set_major_formatter(daysFmt)
    plt.show()

def draw_sleep_heart():
    fig = plt.figure(1)
    host = SubplotHost(fig, 111)
    par1 = host.twinx()
    par1.axis["right"].set_visible(True)
    #offset = 60, 0
    fig.add_axes(host)
    plt.subplots_adjust(right=0.75)
    host.set_xlabel("Time")
    host.set_ylabel("State")
    par1.set_ylabel("HeartRate [bpm]")
    host.set_xlim(time_s[0], time_s[len(time_s)-1])
    par1.set_ylim(0, 100)
    p1, = host.plot(time_s, state, label="State")
    p2, = par1.plot(time_h, heart, label="HeartRate")
    host.legend()
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    days = mdates.AutoDateLocator()
    daysFmt = mdates.DateFormatter("%H:%M")
    host.xaxis.set_major_locator(days)
    host.xaxis.set_major_formatter(daysFmt)
    par1.xaxis.set_major_locator(days)
    par1.xaxis.set_major_formatter(daysFmt)
    plt.show()

def draw_heart_temp():
    fig = plt.figure(1)
    host = SubplotHost(fig, 111)
    par1 = host.twinx()
    par1.axis["right"].set_visible(True)
    #offset = 60, 0
    fig.add_axes(host)
    plt.subplots_adjust(right=0.75)
    host.set_xlabel("Time")
    host.set_ylabel("HeartRate [bpm]")
    par1.set_ylabel("Temperature [℃]")
    host.set_xlim(time_s[0], time_s[len(time_s)-1])
    host.set_ylim(0, 100)
    par1.set_ylim(0, 35)
    p1, = host.plot(time_h, heart, label="HeartRate")
    p2, = par1.plot(time_t, temp, label="Temperature")
    host.legend()
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    days = mdates.AutoDateLocator()
    daysFmt = mdates.DateFormatter("%H:%M")
    host.xaxis.set_major_locator(days)
    host.xaxis.set_major_formatter(daysFmt)
    par1.xaxis.set_major_locator(days)
    par1.xaxis.set_major_formatter(daysFmt)
    plt.show()

read_csv()
get_fitbit_data()
time_t = pd.to_datetime(time_t)
time_s = pd.to_datetime(time_s)
time_h = pd.to_datetime(time_h)
draw_sleep_temp()
draw_sleep_humid()
draw_sleep_heart()
draw_heart_temp()

"""
fig = plt.figure()
ax = fig.add_subplot(2,1,1)
ax.plot(time_s, state)
days = mdates.AutoDateLocator()
daysFmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(daysFmt)

ax = fig.add_subplot(2,1,2)
ax.plot(time_t, temp)
days = mdates.AutoDateLocator()
daysFmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(daysFmt)
plt.show()
"""