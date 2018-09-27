import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


bus_line= str(sys.argv[2])
api_key= str(sys.argv[1])


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=B52"

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

clean_bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus Line : " + bus_line)
print("Number of Active Buses : " + str(len(clean_bus_data)))
bus_counter = 0 
for i in clean_bus_data:
    print("Bus " + str(bus_counter) + " is at latitude " + str(i["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]) + " and longitude " + str(i["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]))
    bus_counter += 1