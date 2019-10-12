import requests
import xml.etree.ElementTree as ET
#import os


AWC_TDS_URL='https://www.aviationweather.gov/adds/dataserver_current/httpparam'


#Station MUST BE A LIST OR JOIN WILl LIKELY BREAK
def get_print_metar (station_list, hours=3):
    payload={'dataSource': 'metars',
             'requestType': 'retrieve',
             'format': 'xml',
             'stationString': ",".join(station_list),
             'hoursBeforeNow': hours}

    r = requests.get(AWC_TDS_URL, params=payload)

    if r.status_code is 200:
        return "{}".format(r.content)
    else:
        print ("== ERRORS HAVE OCCURRED ==")
        return "{}: {}".format(r.status_code, r.text)

def get_metar (station_list, hours=3):
    payload={'dataSource': 'metars',
             'requestType': 'retrieve',
             'format': 'xml',
             'stationString': ",".join(station_list),
             'hoursBeforeNow': hours}

    r = requests.get(AWC_TDS_URL, params=payload)

    if r.status_code is 200:
        return r.content
    else:
        print ("== ERRORS HAVE OCCURRED ==")
        return "{}: {}".format(r.status_code, r.text)

def print_raw (root):
    for raw_text_node in root.findall('raw_text'):
        print raw_text_node.text

def print_station_condition (root):
    station = ''
    fly_condition = ''
    message = ''
    for station in root.findall('station_id'):
        station = station.text
    for category in root.findall('flight_category'):
        flying_condition = category.text

    message += 'Weather information for {}'.format(station)

    if flying_condition != '':
        message += " - Conditions indicate {} flight rules.".format(flying_condition)
    print message

def print_wind (root):
    wind_dir = None
    wind_speed = None
    wind_gust = ''

    for wind_dir_node in root.findall("wind_dir_degrees"):
        wind_dir = int(wind_dir_node.text)

    for wind_speed_node in root.findall("wind_speed_kt"):
        if wind_speed_node.text != "0":
            wind_speed = wind_speed_node.text + " knots"
        else:
            wind_speed = int(wind_speed_node.text)

    for wind_gust_node in root.findall("wind_gust_kt"):
        wind_gust = "Gusting at " + wind_gust_node.text + " knots"

    if wind_dir == 0 and wind_speed == 0:
        print "Winds Calm"
    elif wind_dir  == 0:
        print ("Winds are variable @ {}{}".format(wind_speed, wind_gust))
        print ("WARNING: Wind could also be coming DUE NORTH")
    elif wind_dir  > 0 and wind_dir < 90:
        print ("Winds are coming from the NE bearing {} @ {}{}".format(wind_dir,
                                                                       wind_speed,
                                                                       wind_gust))
    elif wind_dir  == 90:
        print ("Winds are from due EAST @ {}{}".format(wind_speed, wind_gust))
    elif wind_dir  > 90 and wind_dir < 180:
        print ("Winds are coming from the SE bearing {} @ {}{}".format(wind_dir,
                                                                       wind_speed,
                                                                       wind_gust))
    elif wind_dir  == 180:
        print ("Winds are from due SOUTH @ {}{}".format(wind_speed, wind_gust))
    elif wind_dir  > 180 and wind_dir < 270:
        print ("Winds are coming from the SW bearing {} @ {}{}".format(wind_dir,
                                                                       wind_speed,
                                                                       wind_gust))
    elif wind_dir  == 270:
        print ("Winds are from due WEST @ {}{}".format(wind_speed, wind_gust))
    elif wind_dir  > 270 and wind_dir < 360:
        print ("Winds are coming from the NW bearing {} @ {}{}".format(wind_dir,
                                                                       wind_speed,
                                                                       wind_gust))

def parse_metar (tds_response):
    response_root = ET.fromstring(tds_response)
    #response_root = ET.parse(tds_response).getroot()

    for metar in response_root.iter('METAR'):
        print_raw(metar)
        print "================================================"
        print "||Attemtping to make this easier for you dude!||"
        print "================================================"
        print_station_condition(metar)
        print_wind(metar)
    """
    for child in xml_tree.iter('*'):
        print(child)
        print("{} has {}".format(child.tag,child.text))
    """

single_list = ["KRNT"]
multi_list = ["KRNT","KBFI"]

#thing = get_print_metar(single_list, hours=1)
thing = get_metar(single_list, hours=1)
print thing
parse_metar(thing)
#parse_metar("examplesingle.xml")


#print ("Testing: multi station {}".format(get_metar(multi_list, hours=1)))
