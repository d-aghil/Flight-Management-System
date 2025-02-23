
# main.py
# This script manages the loading of airport and flight data, and provides functions 
# to search for flights by city, country, or between specific airports.

from Flight import *  # Import the Flight class
from Airport import *  # Import the Airport class

# Global variables to store airport and flight information
allAirports = []  # List of all Airport objects
allFlights = {}  # Dictionary mapping airport codes to a list of Flight objects
all_Destinations = {}  # Dictionary mapping destination codes to incoming flights

def loadData(airportFile, flightFile):
    """
    Load airport and flight data from the specified files.

    :param airportFile: (str) Path to the airport data file.
    :param flightFile: (str) Path to the flight data file.
    :return: (bool) True if data loaded successfully, False if file not found.
    """
    try:
        global allAirports, allFlights, all_Destinations

        # Load airport data
        with open(airportFile, "r") as fileOpened:
            for line in fileOpened:
                code, country, city = map(str.strip, line.strip().split(','))
                allAirports.append(Airport(code, city, country))

        # Load flight data
        with open(flightFile, "r") as openedFlight:
            for line in openedFlight:
                flightNo, origin, destination = map(str.strip, line.strip().split(','))
                current = Flight(flightNo, getAirportByCode(origin), getAirportByCode(destination))

                # Add the flight to the allFlights dictionary
                allFlights.setdefault(origin, []).append(current)

                # Add the flight to the all_Destinations dictionary
                all_Destinations.setdefault(destination, []).append(current)
        return True
    except FileNotFoundError:
        print("Error: One or both files not found.")
        return False

def getAirportByCode(code):
    """
    Retrieve an Airport object by its code.

    :param code: (str) Airport code.
    :return: (Airport) The matching Airport object or -1 if not found.
    """
    return next((airport for airport in allAirports if airport.getCode() == code), -1)

def findAllCityFlights(city):
    """
    Find all flights departing from or arriving to a specified city.

    :param city: (str) City name.
    :return: (list) Flights related to the city.
    """
    return [flight for flights in allFlights.values() for flight in flights
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city]

def findAllCountryFlights(country):
    """
    Find all flights departing from or arriving to a specified country.

    :param country: (str) Country name.
    :return: (list) Flights related to the country.
    """
    return [flight for flights in allFlights.values() for flight in flights
            if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country]

def flightBetweenCountries(origAirport, destAirport):
    """
    Check for a direct flight between two airports.

    :param origAirport: (Airport) Origin Airport object.
    :param destAirport: (Airport) Destination Airport object.
    :return: (list) [origin_code, destination_code] if direct flight exists, otherwise -1.
    """
    return [origAirport.getCode(), destAirport.getCode()]         if any(flight.getDestination() == destAirport for flight in allFlights.get(origAirport.getCode(), []))         else -1

def findFlightBetween(origAirport, destAirport):
    """
    Find a direct or one-stop flight between two airports.

    :param origAirport: (Airport) Origin Airport object.
    :param destAirport: (Airport) Destination Airport object.
    :return: (str) Description of the available flight route.
    """
    if flightBetweenCountries(origAirport, destAirport) != -1:
        return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"

    middle = [c.getDestination().getCode() for c in allFlights.get(origAirport.getCode(), [])
              for flight2 in allFlights.get(c.getDestination().getCode(), [])
              if flight2.getDestination().getCode() == destAirport.getCode()]
    return set(middle) if middle else -1

def findReturnFlight(firstFlight):
    """
    Find the return flight for a given flight.

    :param firstFlight: (Flight) The initial Flight object.
    :return: (Flight) Return Flight object if exists, otherwise -1.
    """
    origin, destination = firstFlight.getOrigin().getCode(), firstFlight.getDestination().getCode()
    return next((f for f in allFlights.get(destination, []) if f.getDestination().getCode() == origin), -1)

def NoSpaces(data):
    """
    Remove spaces and tabs from a list of strings.

    :param data: (list) List of strings.
    :return: (list) Cleaned strings without spaces or tabs.
    """
    return [s.replace(" ", "").replace("\t", "") for s in data]
