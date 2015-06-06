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
    i = -1
    for city in cities:
        """
        invariant j <= |citys|;
        invariant forall i: nat :: i < j ==> cities[i] != searchingFor;
        """
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
    #.replace("]","")
    for flight in f.read().replace("\n","").replace(" ","").strip().split("["):
        if flight != "":

            parts = flight.split(',')


                #invalid entry cases
            #Checking that the query has 8 parts
            if len(parts) != 7:
                print 'incorrectly formatted flight data'
                continue
            tempDate = parts[0].split['/']
            #checking there are 3 parts of date
            if len(tempDate) != 3:
                print 'incorrectly formatted flight data'
                continue
            #checking they are all numbers
            elif not isinstance( tempDate[0], int) and not isinstance( tempDate[1], int) and not isinstance( tempDate[2], int):
                print 'incorrectly formatted flight data'
                continue
            #check the year is between 2000 and 2500 inclusive
            elif tempDate[2] < 2000 or 2500 < tempDate[2]:
                print 'incorrectly formatted flight data'
                continue
            tempTime = parts[1].split[':']
            #checking time is number:number
            if len(tempTime) != 2:
                print 'incorrectly formatted flight data'
                continue
            #checking that the hours and minutes are integers
            elif not isinstance( tempTime[0], int) and not isinstance( tempTime[1], int):
                print 'incorrectly formatted flight data'
                continue
            #check for invalid date/time re datetime module
            try:
                datetime.datetime(tempDate[2],tempDate[1],tempDate[0],tempTime[0],tempTime[1]) #years, months, days, hours, minutes
            except ValueError:
                print 'Invalid date/time in entry: ' + flight
                continue
            
            #check the names of cities and airlines are strings
            if not isinstance( parts[2], str) and not isinstance(parts[3],str) and not isinstance(parts[5],str):
                print 'incorrectly formatted flight data'
                continue          
            #check if the names start with a capital
            elif not parts[2][0].isupper() and not parts[3][0].isupper() and not parts[5][0].isupper():
                print 'incorrectly formatted flight data'
                continue
            #check the names of the cities are not the same
            elif parts[2] == parts[3]:
                print 'incorrectly formatted flight data'
                continue
            #checks duration is an integer
            if not isinstance( parts[4], int):
                print 'incorrectly formatted flight data'
                continue
            
            #checking the close bracket is correctly placed
            elif parts[6][-1] != ']':
                print 'incorrectly formatted flight data'
                continue
            #checking that the cost is an integer
            parts[6] = parts[6][:-1]
            if not isinstance( parts[6], int):
                print 'incorrectly formatted flight data'
                continue
            

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

