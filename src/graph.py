import sys, datetime
import algorithm
import flightClasses

class City():
    def __init__(self, name):
        self.name = name
        self.flights = []
    def __repr__(self):
        x = str([str(i) for i in self.flights])
        return "name:{} flights:{}".format(self.name, x)
class Graph():
    """ contains a list of cities that hold information from std input"""
    def __init__(self, cities):
        """creates(initialises a city object """
        self.cities = cities

    def getFlights(self, trip):
        """
        Precondition:
            trip != null;
            & trip.current != null;
            & self.cities != [] && null !in self.cities && forall c: City | c in self.cities :: null !in c.flights
        Postcondition: return potFlights
            potFlights != [] ==> (forall x1 : Flight :: x1 != null && x1 in potFlights ==> x.currCal < x1.minutes)
            && potFlights == [] ==> (forall x1 : Flight :: x1 != null && x1 !in potFlights)
        """

        """gets all VALID flights related to the latest city from the input TRIP
        from the graph"""

        potFlights = []

        currentCity = self.cities[getIndex(self.cities,trip.current)]

        #for everything that trip.curr connects to
        for flight in currentCity.flights:
            """
            invariant potFlights == [] ==> (forall x1 : Flight :: x1 in currentCity.flights ==> x1 !in potFlights)
                && potFlights != [] ==> (forall x1 : Flight :: x1 in currentCity.flights && x1.minutes > trip.currCal ==> x1 in potFlights);
            """
            if (trip.convertTime(flight.date, flight.time) > trip.currCal):
                potFlights.append(flight)
                #tripCal = dateTime()
        return potFlights

    def getCityNames(self):
        """gets all the city names and returns them in list format"""
        cNames = []
        for c in self.cities:
            cNames.append(c.name)
        return cNames

    def getAirlines(self):
        aNames = []
        for c in self.cities:
            for f in c.flights:
                if f.airline not in aNames:
                    aNames.append(f.airline)
        return sorted(aNames)

def getIndex(cities, searchingFor):
    """
    Precondition:
        cities != []; & searchingFor != null;
    Postcondition: return z
        z < |citys|;
    """
    """returns the index of a specified city in the cities list """

    for i in range(len(cities)):
        if cities[i].name == searchingFor:
            return i
    raise ValueError("{} not in cities list".format(searchingFor))


#filename = sys.argv[1]
def makeGraph(filename):
    """creates a graph(list of cities) from the flightdata file
    returns a list of cities (each containing a list of flights)"""
    f = open(filename, 'r')
    cities = []
    #.replace("]","")
    for flight in f.read().replace("\n","").replace(" ","").strip().split("["):
        try:
            if flight != "":
                parts = flight.split(',')
                tempDate = [int(i) for i in parts[0].split('/')]
                tempTime = [int(i) for i in parts[1].split(':')]
                parts[4] = int(parts[4])

                #invalid entry cases
                #Checking that the query has 8 parts
                if len(parts) != 7:
                    exit("incorrectly formatted flight data")
                #checking there are 3 parts of date
                if len(tempDate) != 3:
                    exit("incorrectly formatted flight data")

                #check the year is between 2000 and 2500 inclusive
                if tempDate[2] < 2000 or 2500 < tempDate[2]:
                    exit("incorrectly formatted flight data")
                #checking time is number:number
                if len(tempTime) != 2:
                    exit("incorrectly formatted flight data")

                #check for invalid date/time re datetime module
                try:
                    datetime.datetime(tempDate[2],tempDate[1],tempDate[0],tempTime[0],tempTime[1]) #years, months, days, hours, minutes
                except ValueError:
                    print ('Invalid date/time in entry:[' + flight)
                    print ("1")
                    continue

                #check if the names start with a capital
                if not parts[2][0].isupper() and not parts[3][0].isupper() and not parts[5][0].isupper():
                    exit("incorrectly formatted flight data")

                #check the names of the cities are not the same
                if parts[2] == parts[3]:
                    exit("incorrectly formatted flight data")

                #checking the close bracket is correctly placed
                if parts[6][-1] != ']':
                    exit("incorrectly formatted flight data")

                #checking that the cost is an integer
                parts[6] = int(parts[6][:-1])


                #Checking if we already have the city
                try:
                    getIndex(cities,parts[2])
                except ValueError:
                    cities.append(City(parts[2]))

                try:
                    getIndex(cities,parts[3])
                except ValueError:
                    cities.append(City(parts[3]))


                myFlight = flightClasses.Flight(parts[0], parts[1], parts[2], parts[3], int(parts[4]), parts[5], int(parts[6]))
                cities[getIndex(cities, parts[2])].flights.append(myFlight)
        except ValueError as e:
            exit("incorrectly formatted flight data")
    return Graph(cities)


