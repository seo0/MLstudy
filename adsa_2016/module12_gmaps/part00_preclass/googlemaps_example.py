from gmaps import Geocoding
from gmaps import Directions

from datetime import datetime, date, time


def get_gmaps_time(year, month, day, hour, mins):
    d = date(year, month, day)
    t = time(hour, mins)
    dt = datetime.combine(d, t)
    return int(dt.timestamp())


if __name__ == '__main__':

    geocoder = Geocoding(api_key="YOUR_KEY")                                                # initialise the Geocoder of python-gmaps

    print("============== Example of value returned when geocoding an address:")
    geocode_result = geocoder.geocode('Wimbledon station, London')                          # call the geocoder
    print(geocode_result)                                                                   # To-Do: look at the data structure returned by the geocoder

    print(" ")

    print("============== Example of value returned when reverse geocoding coordinates (latitude, longitude):")
    reverse_geocode_result = geocoder.reverse(40.714224, -73.961452)
    print(reverse_geocode_result)

    print(" ")

    dep_time = get_gmaps_time(2016, 10, 20, 11, 34)                                         # create example departure time, to be used in the example

    # ================================================================================================================================================
    # ================================================================================================================================================

    dir = Directions(api_key="YOUR_KEY")                  # iinitialse the directions module of python-gmaps

    origin = "Trafalgar square, London, UK"
    destination = "Wimbledon, London, UK"

    print(" ")
    print("============== Example of directions returned by python-gmaps:")

    # get directions from Gmaps:
    # mode: driving, walking etc. see: https://developers.google.com/maps/documentation/directions/intro#TravelModes
    # departure time: must be an integer timestamp, the function get_gmaps_time() can be used to obtain such a timestamp
    # units: metric or imperial (use always metric!) https://developers.google.com/maps/documentation/directions/intro#UnitSystems
    # other possible parameters at https://developers.google.com/maps/documentation/directions/intro#RequestParameters
    directions_result = dir.directions(origin, destination, mode="transit",departure_time=dep_time, units='metric')

    print(" ")
    print(directions_result)

    # ================================================================================================================================================
    # ================================================================================================================================================

    print(" ")
    print("============== Inspecting the content of the variable returned by directions (a list with one complex dictionary inside...)")

    print(directions_result[0].keys())                                                          # most useful information is at the key "legs"
    print(directions_result[0]['legs'][0].keys())                                               # directions_result[0]['legs'][0] is itself a dictionary
    print("\n")
    for key in directions_result[0]['legs'][0].keys():
        print("{0} : {1}".format(key,directions_result[0]['legs'][0][key]))

    print("\n")
    for step in directions_result[0]['legs'][0]['steps']:                                       # within "legs", "steps" contains information about indivdual steps of the trip
        print(step)

    # =====================================================================
    # =====================================================================
    # TRY TO CREATE YOUR OWN CODE HERE TO SOLVE THE QUESTIONS OF THE QUIZ
    # =====================================================================
    # =====================================================================

