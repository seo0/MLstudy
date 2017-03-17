from gmaps import Directions
from datetime import datetime

from module12_gmaps.part01_geocoding.gmaps_basics import *

def quickest_mode_of_transport(origin, destination, dep_time):
    """
    This function calculates and prints on the screen the quickest way of transport
    between origin and destination among ["driving", "walking", "bicycling", "transit"]

    Note that duration the trip duration returned by gmaps follows this rule:
    - of the trip takes 1 hour or more, then the duration value is returned in minutes
    - if the trip takes less than 1 hour, then the duration is returned in seconds

    Assume that trips between origin and destination take less than 24 hours in any travel mode
    """
    pass



def calculate_fuel_cost(itinerary, dep_time, price_per_liter, km_per_liter):
    """
    This function calculates the fuel cost for a given trip specified in itinerary

    :param itinerary: a list of places to visit (see example of use in the main)
    :param dep_time: the departure time
    :param price_per_liter: the price per liter of fuel (e.g. 1322 won/l)
    "param km_per_litre: the efficiency of the vehicle used for travelling (expressed in km travelled with 1 liter of fuel, e.g. 15.6 km/l)
    """
    pass





if __name__ == '__main__':

    dep_time = get_gmaps_time(2016, 10, 20, 11, 34)

    quickest_mode_of_transport("Cupertino, California", "Mountain View, California", dep_time)
    quickest_mode_of_transport("Piccadilly Circus, London, UK", "Waterloo station, London, UK", dep_time)

    calculate_fuel_cost(["Austin, Texas", "Los Angeles, California", "Las Vegas, Nevada", "San Francisco, California"], dep_time, 1168, 15.6)
    calculate_fuel_cost(["London, UK", "Birmingham, UK", "Newcastle, UK", "Edinburgh, Scotland"], dep_time, 1168, 15.6)