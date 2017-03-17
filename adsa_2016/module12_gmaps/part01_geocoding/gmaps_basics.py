from gmaps import Geocoding
from gmaps import Directions

from datetime import datetime, date, time

import re


### ===================  Some usueful functions ===========================================
### =======================================================================================
def get_gmaps_time(year, month, day, hour, mins):
    d = date(year, month, day)
    t = time(hour, mins)
    dt = datetime.combine(d, t)
    return int(dt.timestamp())

def get_date_time(gmap_time):
    return datetime.fromtimestamp(gmap_time)

def get_formatted_address(lat, lon):
    """
    Returns a formattedd address given the latitude and longitude of a location
    :param lat: lattude (must be float!)
    :param lon: longitude (must be float!)
    :return:
    """
    api = Geocoding(api_key="AIzaSyDBiPAsMkUpCRyuX1WlYuZr6FgPJDjbWq0")
    location = api.reverse(lat, lon)
    return location[0]['formatted_address']

def strip_html_tags(str):
    return re.sub('<[^<]+?>', '', str)

### =======================================================================================
### =======================================================================================
### =======================================================================================



def check_time_to_dest(origin, destination, mode, dep_time, time_limit):
    """
    checks whether travelling to destination in a given mode takes less than time_limit
    Note that when the travellig time to destination is less than 1 hour (up to 59 min), then the value is returned in seconds
    If travelling takes more than one hour, then it is returned in minutes
    :param origin:
    :param destination:
    :param mode:
    :param time_limit:
    :return: True or False
    """
    pass


def get_trip_info(origin, destination, mode, dep_time, verbose):
    """
    This function retrieves info about a trip from "origin" to "destination" using a specific "mode"
     of transport deprating at a given "dep_time" from Gmaps. The function should return (in the following order):
    - duration of the trip as a text value
    - duration of the trip as a numeric value
    - distance travelled as a text value
    - distance ravelled as a numeric value.

    If the parameter Verbose is set to "True", then the function also
    prints in a "nicely formatted way" some info about the trip in the following form:
        Trip: <origin> TO <destination>
        Mode of transport: TRANSIT
        Total time: 56 min
            Steps:
                1) Walk to somewhere : WALKING from <start_address> to <end_address>, distance: 1kim, time: 3 min
                2) Take train to somewhere: TRANSIT from ...
                3) ...
                i) <instructions> : <mode of transport> from from <start_address> to <end_address>, distance: <...>, time: <...>
                etc.

    (note that dep_time must be a "gmaps_time")


    """

    pass





if __name__ == '__main__':
    #api = Geocoding()
    #print(api.geocode("14 Cross Road SW19 1PF, London, UK"))


    verbose = True

    time = get_gmaps_time(2016, 10, 20, 11, 34)
    print(time)
    print(get_date_time(time))

    str = "<b>This<b> string has <i>html<i> <c>tags<c>"
    print(str)
    print(strip_html_tags(str))

    print(get_formatted_address(40.714224, -73.961452))

    get_trip_info("Trafalgar square, London, UK", "Berlin, Germany", "transit", time, verbose)

    print(check_time_to_dest("Trafalgar square, London, UK", "Berlin, Germany", "transit", time, 40))

    get_trip_info("Trafalgar square, London, UK", "John O'Groats, Scotland", "transit", time, verbose)
    print(check_time_to_dest("Trafalgar square, London, UK", "John O'Groats, Scotland", "transit", time, 40))

    get_trip_info("San Antonio, Texas", "Austin, Texas", "driving", time, verbose)