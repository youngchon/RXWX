import requests
#import os


AWC_TDS_URL='https://www.aviationweather.gov/adds/dataserver_current/httpparam'


#Station MUST BE A LIST OR JOIN WILl LIKELY BREAK
def get_metar (station_list, hours=3):
    payload={'dataSource': 'metars',
             'requestType': 'retrieve',
             'format': 'xml',
             'stationString': ",".join(station_list),
             'hoursBeforeNow': hours}

    r = requests.get(AWC_TDS_URL, params=payload)

    if r.status_code is 200:
        return "{}".format(r.text)
    else:
        return "{}: thing".format(r.status_code, r.text)

single_list = ["KRNT"]
print ("Testing: {}".format(single_list))
print ("Testing: one station {}".format(get_metar(single_list, hours=1)))
multi_list = ["KRNT","KBFI"]
print ("==================")

print ("Testing: multi station {}".format(get_metar(multi_list, hours=1)))
