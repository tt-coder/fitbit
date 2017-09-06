import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import fitbit
import json
import auth_data as ad
from datetime import datetime as dt

DATE = "2017-09-04"

authd_client = fitbit.Fitbit(ad.CLIENT_ID, ad.CLIENT_SECRET,
                access_token=ad.ACCESS_TOKEN, refresh_token=ad.REFRESH_TOKEN)
#data = authd_client.intraday_time_series('activities/heart', base_date="2017-09-04", detail_level='1min', start_time="07:00", end_time="09:00")
data = authd_client.sleep(date=DATE)
data = data["sleep"][0]["minuteData"]

time_d = []
state = []

for i in range(0,len(data)):
    date = data[i]["dateTime"]
    date = dt.strptime(date, "%H:%M:%S")
    time_d.append(date.strftime("%H:%M"))
    state.append(data[i]["value"])

time_d = pd.to_datetime(time_d)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(time_d, state)

days = mdates.AutoDateLocator()
daysFmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(daysFmt)
plt.show()


#print(json.dumps(data[0], indent=4))

#authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

#data_sec = authd_client.intraday_time_series("activities/heart", DATE, datail_level="1sec")
#heart_sec = data_sec["activities-heart-intraday"]["dataset"