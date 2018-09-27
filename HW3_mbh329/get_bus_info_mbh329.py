import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


api_key= str(sys.argv[1])
bus_line= str(sys.argv[2])
file_nm= str(sys.argv[3])

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=%s" % M14

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

clean_bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
tmp = """Latitude, Longitude, Stop Name, Stop Status"""
for i in clean_bus_data:
	dist_from_stop = i["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
	stop_name = i["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
	lat = i["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
	lon = i["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
	tmp += '\n'
	tmp += '%f, %f, %s, %s' % (lat, lon, stop_name, dist_from_stop)
f = open(file_nm, 'w')
f.write(tmp)
f.close()
print(tmp)
    