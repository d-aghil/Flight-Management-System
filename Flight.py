
# Flight.py
# This module defines the Flight class representing a flight between two airports.
# It includes methods to determine flight details, check equality, and identify domestic flights.

from Airport import Airport  # Import the Airport class to validate flight origins and destinations

class Flight:
    def __init__(self, flightNo, origin, destination):
        """
        Initialize a Flight object.

        :param flightNo: (str) The flight number (e.g., 'AC101').
        :param origin: (Airport) The origin Airport object.
        :param destination: (Airport) The destination Airport object.
        :raises TypeError: If origin or destination is not an Airport object.
        """
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo          # Flight number
            self._origin = origin              # Origin airport (Airport object)
            self._destination = destination    # Destination airport (Airport object)
        else:
            raise TypeError("The origin and destination must be Airport objects")

    def isDomesticFlight(self):
        """
        Check if the flight is domestic (i.e., both airports are in the same country).

        :return: (bool) True if domestic, False otherwise.
        """
        return self._origin.getCountry() == self._destination.getCountry()

    def __repr__(self):
        """
        Return a string representation of the Flight object.

        :return: (str) Example: 'Flight: AC101 from Toronto to New York {international}'
        """
        flight_type = "domestic" if self.isDomesticFlight() else "international"
        return (f"Flight: {self._flightNo} from {self._origin.getCity()} "
                f"to {self._destination.getCity()} {{{flight_type}}}")

    def __eq__(self, other):
        """
        Check if two Flight objects are equal based on their origin and destination.

        :param other: (Flight) Another Flight object to compare.
        :return: (bool) True if origins and destinations match, False otherwise.
        """
        return isinstance(other, Flight) and self._origin == other._origin and self._destination == other._destination

    def getFlightNumber(self):
        """
        Get the flight number.

        :return: (str) The flight number.
        """
        return self._flightNo

    def getOrigin(self):
        """
        Get the origin airport.

        :return: (Airport) The origin Airport object.
        """
        return self._origin

    def getDestination(self):
        """
        Get the destination airport.

        :return: (Airport) The destination Airport object.
        """
        return self._destination

    def setOrigin(self, origin):
        """
        Set or update the origin airport.

        :param origin: (Airport) The new origin Airport object.
        :raises TypeError: If origin is not an Airport object.
        """
        if isinstance(origin, Airport):
            self._origin = origin
        else:
            raise TypeError("Origin must be an Airport object")

    def setDestination(self, destination):
        """
        Set or update the destination airport.

        :param destination: (Airport) The new destination Airport object.
        :raises TypeError: If destination is not an Airport object.
        """
        if isinstance(destination, Airport):
            self._destination = destination
        else:
            raise TypeError("Destination must be an Airport object")
