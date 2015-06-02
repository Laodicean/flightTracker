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
        """gets all VALID flights related to the latest city from the input TRIP
        from the graph"""

        potFlights = []

        currentCity = self.cities[getIndex(self.cities,trip.current)]

        #for everything that trip.curr connects to
        for flight in currentCity.flights:
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

def getIndex(cities, searchingFor):
    """returns the index of a specified city in the cities list """
    i = -1
    for city in cities:
        i+=1
        if city.name == searchingFor:
            return i
    return 'no'



#filename = sys.argv[1]
def makeGraph(filename):
    """creates a graph(list of cities) from the flightdata file
    returns a list of cities (each containing a list of flights)"""
    f = open(filename, 'r')
    cities = []
    for flight in f.read().replace("\n","").replace("]","").replace(" ","").strip().split("["):
        if flight != "":

            parts = flight.split(',')

            #Checking if we already have the city
            foundCity = getIndex(cities, parts[2])
            foundDest = getIndex(cities, parts[3])
            #if the city did not already exist
            if foundDest == 'no':
                cities.append(City(parts[3]))
            if foundCity == 'no':
                cities.append(City(parts[2]))
                foundCity = -1

            myFlight = flightClasses.Flight(parts[0], parts[1], parts[2], parts[3], int(parts[4]), parts[5], int(parts[6]))
            cities[foundCity].flights.append(myFlight)
    return Graph(cities)

"""
filename = sys.argv[2]
q = open(filename, 'r')
for flights:query in q.read().strip().split("["):
    if query != "":
        parts = query.split(',')
        #WARNING SEE SPEC FOR PROPER PREFERENCES INPUT FORMAT
        myQuery = Query(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5],parts[6],parts[7])
        algorithm.getFlightSolutions(myQuery,cities)
"""
