from enum import Enum
from datetime import datetime

# Enumeration for Gender
class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class User:
    """Class to represent a user"""
    def __init__ (self, firstName, lastName, gender, phoneNumber, address):
        # Initialization of user attributes (note that they are all protected since this ia the parent class)
        self._firstName = firstName
        self._lastName = lastName
        self._gender = gender
        self._phoneNumber = phoneNumber
        self._address = address

    # Setter and getter methods for user attributes

    def setFirstName(self, firstName):
        self._firstName = firstName
    def getFirstName(self):
        return self._firstName

    def setLastName(self, lastName):
        self._lastName = lastName
    def getLastName(self):
        return self._lastName

    def setGender(self, gender):
        self._gender = gender
    def getGender(self):
        return self._gender

    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber
    def getPhoneNumber(self):
        return self._phoneNumber

    def setAddress(self, address):
        self._address = address
    def getAddress(self):
        return self._address


class AirlineStaff(User):
    """Class represnting airline staff, inheriting from the User class"""
    def __init__(self,firstName, lastName, gender, phoneNumber, address, employeeID,email, department,  role, airline):
        # Initialize the parent class with common user attributes
        super().__init__ (firstName, lastName, gender, phoneNumber, address)
        # Airline staff specific attributes (private)
        self.__employeeID = employeeID
        self.__email = email
        self.__department = department
        self.__role = role
        self.__airline = airline

    # Setter and getter methods for airline staff specific attributes

    def setEmployeeID(self, employeeID):
        self.__employeeID = employeeID
    def getEmployeeID(self):
        return self.__employeeID

    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email

    def setdepartment(self, department):
        self.__department = department
    def getdepartment(self):
        return self.__department

    def setRole(self, role):
        self.__role = role
    def getRole(self):
        return self.__role

    def setAirline(self, airline):
        self.__airline = airline
    def getAirline(self):
        return self.__airline

    # A method to display details of the airline staff
    def displayStaff(self):
        print("Airline Staff Details:")
        print("Employee Name:", self.getFirstName(), self.getLastName())
        print("Gender:", self.getGender().value)
        print("Phone Number:", self.getPhoneNumber())
        print("Address:", self.getAddress())
        print("Employee ID:", self.getEmployeeID())
        print("Work Email:", self.getEmail())
        print("Depratment:", self.getdepartment())
        print("Role:", self.getRole())
        print("Airline:", self.getAirline())
        print()


class Passenger(User):
    """Class represnting a passenger, inheriting from the User class"""
    def __init__(self,firstName, lastName, gender, phoneNumber, address, age, nationality, passengerID, passportNumber):
        # Initialize the parent class with common user attributes
        super().__init__ (firstName, lastName, gender, phoneNumber, address)
        # Passenger specific attributes (private)
        self.__age = age
        self.__nationality = nationality
        self.__passengerID = passengerID
        self.__passportNumber = passportNumber

    # Setter and getter methods for passenger specific attributes

    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setNationality(self, nationality):
        self.__nationality = nationality
    def getNationality(self):
        return self.__nationality

    def setPassengerID(self, passengerID):
        self.__passengerID = passengerID
    def getPassengerID(self):
        return self.__passengerID

    def setPassportNumber(self, passportNumber):
        self.__passportNumber = passportNumber
    def getPassportNumber(self):
        return self.__passportNumber

    # A method to display details of the passenger
    def displayPassenger(self):
        print("Passenger Details:")
        print("Passenger Name:", self.getFirstName(), self.getLastName())
        print("Gender:", self.getGender().value)
        print("Phoen Number:", self.getPhoneNumber())
        print("Address:", self.getAddress())
        print("Age:", self.getAge())
        print("Nationality:", self.getNationality())
        print("Passenger ID:", self.getPassengerID())
        print("Pasport Number:", self.getPassportNumber())
        print()


# Enumeration for scan result types of baggage
class ScanResultType(Enum):
    checked = "The baggage was checked successfully"
    notAllowed = "The baggage includes not allowed items"

class Baggage:
    """Class represnting baggage"""
    def __init__(self, baggageID, passengerName, weight, dimensions, securityScanResult):
        # Initialization of baggage attributes
        self.__baggageID = baggageID
        self.__passengerName = passengerName
        self.__weight = weight
        self.__dimensions = dimensions
        self.__securityScanResult = securityScanResult
        self.__weightLimit = 23.0  # Weight limit in kilograms
        self.__extraFeePer_kg = 99  # Extra fee for each kilogram above the weight limit

    # Setter and getter methods for baggage attributes

    def setBaggageID(self, baggageID):
        self.__baggageID = baggageID
    def getBaggageID(self):
        return self.__baggageID

    def setPassengerName(self, passengerName):
        self.__passengerName=  passengerName
    def getPassengerName(self):
        return self.__passengerName

    def setWeight(self, weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setDimensions(self, dimensions):
        self.__dimensions = dimensions
    def getDimensions(self):
        return self.__dimensions

    def setSecurityScanResult(self, securityScanResult):
        self.__securityScanResult = securityScanResult
    def getSecurityScanResult(self):
        return self.__securityScanResult

    # A method to check if the baggage is overweight
    def is_overweight(self):
        return self.__weight > self.__weightLimit

    # A method to calculate extra fees based on weight
    def calculate_extra_fees(self):
        if self.is_overweight():  # This if condition checks wether the bag is overweight or not
            extra_weight = self.__weight - self.__weightLimit  #if so it calculates how many extra kgs it has tp calculate fess for the extra weight
            extra_fees = extra_weight * self.__extraFeePer_kg         # This multiplies the extra kgs by the extra fees per kg to get the total extra fees
            return extra_fees
        else:
            return 0

    # A method to display details of the baggage
    def displayBaggageDetails(self):
        print("Baggage ID:", self.getBaggageID())
        print("Passenger Name:", self.getPassengerName())
        print("Weight:", self.getWeight(), "kg")
        print("Dimensions:", self.getDimensions(), "cm")
        print("Security Scan Result:", self.getSecurityScanResult().value)
        if self.is_overweight():
            print("Extra Fees:", "You have extra fees of", self.calculate_extra_fees(), "AED, for exceeding the weight limit")
        else:
            print("No extra fees, the bag is within the required limit")
        print()

# Enumeration for class types available in airline travel
class ClassType(Enum):
    economy = "Economy"
    business = "Business"
    firstClass = "First Class"

class BoardingPass:
    """Class representing a boarding pass"""
    def __init__ (self, boardingPassID, boardingTime, departureTerminal, gate, flightNumber, fromLocation, toLocation, flightDate, departureTime, seatNumber, classType):
        # Initialization of boarding pass attributes
        self.__boardingPassID = boardingPassID
        self.__boardingTime = boardingTime
        self.__departureTerminal = departureTerminal
        self.__gate = gate
        self.__flightNumber = flightNumber
        self.__fromLocation = fromLocation
        self.__toLocation = toLocation
        self.__flightDate = flightDate
        self.__departureTime = departureTime
        self.__seatNumber = seatNumber
        self.__classType = classType

    # Setter and getter methods for boarding pass attributes

    def setBoardingPassID(self, boardingPassID):
            self.__boardingPassID = boardingPassID
    def getBoardingPassID(self):
        return self.__boardingPassID

    def setBoardingTime(self, boardingTime):
        self.__boardingTime = boardingTime
    def getBoardingTime(self):
        return self.__boardingTime

    def setDepartureTerminal(self, departureTerminal):
        self.__departureTerminal = departureTerminal
    def getDepartureTerminal(self):
        return self.__departureTerminal

    def setGate(self, gate):
        self.__gate = gate
    def getGate(self):
        return self.__gate

    def setFlighNumber(self, flightNumber):
        self.__flightNumber = flightNumber
    def getFlightNumber(self):
        return self.__flightNumber

    def setFromLocation(self, fromLocation):
        self.__fromLocation = fromLocation
    def getFromLoction(self):
        return self.__fromLocation

    def setToLocation(self, toLocation):
        self.__toLocation = toLocation
    def getToLocation(self):
        return self.__toLocation

    def setFlightDate(self, flightDate):
        self.__flightDate = flightDate
    def getFlightDate(self):
        return self.__flightDate

    def setDepartureTime(self, departureTime):
        self.__departureTime = departureTime
    def getDepartureTime(self):
        return self.__departureTime

    def setSeatNumber(self, seatNumber):
        self.__seatNumber = seatNumber
    def getSeatNumber(self):
        return self.__seatNumber

    def setClassType(self, classType):
        self.__classType = classType
    def getClassType(self):
        return self.__classType

    # A method to display details of the boarding pass
    def displayBoardingPass(self):
        print("Boarding pass:")
        print("Boarding Pass ID:", self.getBoardingPassID())
        print("Boarding Time:", self.getBoardingTime())
        print("Terminal:", self.getDepartureTerminal())
        print("Gate:", self.getGate())
        print("Flight Number:", self.getFlightNumber())
        print("From:", self.getFromLoction())
        print("To:", self.getToLocation())
        print("Flight Date:", self.getFlightDate())
        print("Departure Time:", self.getDepartureTime())
        print("Seat Number:", self.getSeatNumber())
        print("Class:", self.getClassType().value)

# Creating an instance of AirlineStaff
staff = AirlineStaff("Maria", "Dave", Gender.FEMALE, "0501234567", "Al Reem Island, Abu Dhabi", "E4321", "maria.dave@airline.con", "Check-in services", "Check-in Agent", "Etihad Airways")
# Displaying the details of the created AirlineStaff object
staff.displayStaff()

# Creating an instance of Passenger
passenger = Passenger("Omar", "Alnuaimi", Gender.MALE, "0567654321", "Saadiyat Island" , "27", "UAE", "P1234", "N9876512")
# Displaying the details of the created Passenger object
passenger.displayPassenger()

# Creating an instance of Baggage
baggage = Baggage("BG123", "Omar Alnuaimi", 25, "55x40x20", ScanResultType.checked)
# Displaying the details of the created Baggage object
baggage.displayBaggageDetails()


# Defining datetime objects for boarding, departure, and the flight date
boarding_time = datetime(2024, 2, 24, 15, 30)  # Boarding time of the flight
departure_time = datetime(2024, 2, 24, 16, 15)  # Departure time of the flight
flight_date = datetime(2024, 2, 24)  # Date of the flight
# Creating an instance of BoardingPass
boarding_pass = BoardingPass("BP123", boarding_time, "Terminal 1", "G02", "FL123", "Abu Dhabi", "Chicago", flight_date, departure_time, "12A", ClassType.firstClass)
# Displaying the details of the created BoardingPass object
boarding_pass.displayBoardingPass()