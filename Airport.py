
# Airport.py
# This module defines the Airport class representing an airport with attributes 
# such as code, city, and country. It includes methods to retrieve and modify these attributes.

class Airport:
    def __init__(self, code, city, country):
        """
        Initialize an Airport object.

        :param code: (str) The airport code (e.g., 'JFK', 'YYZ').
        :param city: (str) The city where the airport is located.
        :param country: (str) The country where the airport is located.
        """
        self._code = code        # Private attribute to store the airport code
        self._city = city        # Private attribute to store the city name
        self._country = country  # Private attribute to store the country name

    def __repr__(self):
        """
        Return a string representation of the Airport object.

        :return: (str) Example: 'JFK (New York, USA)'
        """
        return f"{self._code} ({self._city}, {self._country})"

    def getCode(self):
        """
        Get the airport code.

        :return: (str) The airport code.
        """
        return self._code

    def getCity(self):
        """
        Get the city of the airport.

        :return: (str) The city name.
        """
        return self._city

    def getCountry(self):
        """
        Get the country of the airport.

        :return: (str) The country name.
        """
        return self._country

    def setCity(self, city):
        """
        Set or update the city of the airport.

        :param city: (str) The new city name.
        """
        self._city = city

    def setCountry(self, country):
        """
        Set or update the country of the airport.

        :param country: (str) The new country name.
        """
        self._country = country
