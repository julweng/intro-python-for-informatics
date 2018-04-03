# Assignment 7: Google Geocoding
# Julia Tzu-Ya Weng U07487022

# this modified geojson.py prompts the user for a location and use the location
# to retrieve data from google maps and prints out the two-character country 
# code from the retrieved data.

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    # prompt user for input
    address = raw_input('Enter location or press ENTER to finish: ')
    if len(address) < 1 : break

    # calls Google geocoding
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    
    # retrieve data in JSON format
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue
               
    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location

    # get address_components from retrieved data
    address_components = js['results'][0]['address_components']
    
    # use country as a flag for whether a location is in a country
    country = 0;
    
    # address_component is a list of dictionaries; loop through each dict_item
    for dict_item in address_components:
        # each dict_item has a "types" key
        types = dict_item["types"]
        
        # if location is in a country, one of the dict_item's "types" key would 
        # have "country","political" as its corresponding value
        if types == ["country", "political"]:
            country = 1;
            print "The two character country code is:", dict_item["short_name"]

    # if no such key-value pair can be found
    if country == 0:
        print "The entered location is not in any country"
