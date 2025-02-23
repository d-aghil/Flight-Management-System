# Flight-Management-System


## Project Overview
The **Flight Management System** is a Python-based application that allows users to manage and analyze flight and airport data. It includes functionalities such as searching for flights between cities and countries, checking direct and one-stop flights, and retrieving airport information. The system reads data from text files and organizes it using object-oriented programming principles.

## Features
- Load airport and flight data from files.
- Find flights related to a specific city or country.
- Check for direct and connecting flights between airports.
- Retrieve return flights for given routes.
- Object-oriented design for scalability and maintainability.

## Technologies Used
- **Python 3:** Core programming language.
- **File Handling:** Reading and processing CSV-style text files.
- **Object-Oriented Programming (OOP):** For modular and reusable code.

## Project Structure
```
FlightManagementSystem/
├── Airport.py        # Defines the Airport class.
├── Flight.py         # Defines the Flight class.
├── main.py           # Main application logic.
├── airports.txt      # Sample data file with airport information.
├── flights.txt       # Sample data file with flight information.
└── README.md         # Project documentation.
```

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FlightManagementSystem.git
   cd FlightManagementSystem
   ```

2. **Prepare the data files:**
   - Create `airports.txt` with lines formatted as:
     ```
     YYZ, Canada, Toronto
     JFK, USA, New York
     ```
   - Create `flights.txt` with lines formatted as:
     ```
     AC101, YYZ, JFK
     DL202, JFK, YYZ
     ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## Example Usage
```python
Flights related to Toronto: [Flight: AC101 from Toronto to New York {international}]
Direct Flight: YYZ to JFK
```




   
