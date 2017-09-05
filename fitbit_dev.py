import fitbit
import json
import auth_data as ad

DATE = "2017-08-06"

authd_client = fitbit.Fitbit(ad.CLIENT_ID, ad.CLIENT_SECRET, access_token=ad.ACCESS_TOKEN, refresh_token=ad.REFRESH_TOKEN)
data = authd_client.intraday_time_series('activities/steps', base_date="2017-09-04", detail_level='1min', start_time="07:00", end_time="09:00")
print(json.dumps(data, indent=4))


#authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

#data_sec = authd_client.intraday_time_series("activities/heart", DATE, datail_level="1sec")
#heart_sec = data_sec["activities-heart-intraday"]["dataset"