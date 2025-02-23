# Flight-Management-System


## Project Overview
The Flight Management System is a Python-based application designed to manage airport and flight information. It allows users to load data from files, search for flights between cities or countries, and analyze routes between airports. This project demonstrates object-oriented programming concepts, data handling, and modular code design.

## Features
- Load and parse airport and flight data from text files.
- Search for flights related to a specific city or country.
- Identify direct and connecting flights between airports.
- Determine return flights and flight routes.
- Modular design with separate classes for `Airport` and `Flight`.

## Technologies Used
- Python 3: Core programming language.
- Object-Oriented Programming (OOP): For reusable and maintainable code.
- File Handling: Read and process structured data from text files.

## Project Structure
```
FlightManagementSystem/
├── Airport.py       # Defines the Airport class.
├── Flight.py        # Defines the Flight class.
├── main.py          # Contains data loading and flight search functionalities.
├── airports.txt     # Sample data file with airport information.
├── flights.txt      # Sample data file with flight information.
└── README.md        # Project documentation.
```

## File Descriptions
### 1. Airport.py
Defines the Airport class with attributes for airport code, city, and country. Provides methods to access and modify these attributes.
#### Key Methods:
- `getCode()`: Returns the airport code.
- `getCity()`: Returns the city name.
- `getCountry()`: Returns the country name.
- `setCity(city)`: Updates the city name.
- `setCountry(country)`: Updates the country name.

### 2. Flight.py
Contains the Flight class, representing flights between two airports. It includes methods to check if a flight is domestic, compare flights, and retrieve flight details.
#### Key Methods:
- `isDomesticFlight()`: Checks if the flight is domestic.
- `getFlightNumber()`: Returns the flight number.
- `getOrigin()`: Returns the origin airport.
- `getDestination()`: Returns the destination airport.
- `__repr__()`: Provides a readable representation of the flight.

### 3. main.py
Handles data loading from files and provides functions to search and analyze flight data.
#### Key Functions:
- `loadData(airportFile, flightFile)`: Loads airports and flights from text files.
- `getAirportByCode(code)`: Finds an airport by its code.
- `findAllCityFlights(city)`: Finds flights related to a specific city.
- `findAllCountryFlights(country)`: Finds flights related to a specific country.
- `findFlightBetween(origAirport, destAirport)`: Finds direct or one-stop flights between airports.
- `findReturnFlight(firstFlight)`: Finds the return flight for a given flight.

## Sample Data Format
### airports.txt
```
YYZ, Canada, Toronto
JFK, USA, New York
LHR, UK, London
```

### flights.txt
```
AC101, YYZ, JFK
BA202, LHR, YYZ
DL303, JFK, LHR
```

## Setup and Usage Instructions
### 1. Clone the Repository
```
git clone https://github.com/your-username/FlightManagementSystem.git
cd FlightManagementSystem
```

### 2. Prepare Data Files
Create `airports.txt` and `flights.txt` using the provided formats.

### 3. Run the Program
```
python main.py
```

### 4. Example Output
```
Data loaded successfully.
Flights related to Toronto: [Flight: AC101 from Toronto to New York {international}]
Direct Flight: YYZ to JFK
```

## Why This Project?
- Demonstrates real-world data handling with file I/O.
- Shows object-oriented design with reusable classes.
- Provides a practical application for flight route management.
- Suitable for beginners looking to learn OOP and data processing.

