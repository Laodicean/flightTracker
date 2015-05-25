import sys, datetime
import algorithm
import flightClasses
class Flight():
    def __init__(self, date, time, start, end, duration, airline, cost):
        self.date = date
        self.time = time
        self.start = start
        self.end = end
        self.duration = duration
        self.airline = airline
        self.cost = cost
class Query():
    def __init__(self,date,time,start,end,pref1,pref2,pref3,numFlights):
	self.date = date
	self.time = time
	self.start = start
	self.end = end
	self.pref1 = pref1
	self.pref2 = pref2
	self.pref3 = pref3
	self.numFlights = numFlights
        
class City():
    def __init__(self, name):
        self.name = name
        self.flights = []

       
class graph():
    def __init__(self, cities):
        self.cities = cities

    def getFlights(trip, graph):

        
    
        potFlights = []
        
        current = trip.current

        originIndex = (graph, current)
        
        #for everything that trip.curr connects to
        for flight in graph[originIndex].flights:
            if (convertTime(flight.date, flight.time) > trip.currCal):
                potFlights.add(flight)
                tripCal = dateTime()
        return potFlights


def getIndex(cities, searchingFor):
    i = -1
    for city in cities:
        i+=1
        if city.name == searchingFor:
            return i

    return 'no'
            


'filename = sys.argv[1]
def makeGraph(filename):
    f = open(filename, 'r')
    for flight in f.read().strip().split("["):
        if flight != "":
       
            parts = flight.split(',')
            cities = []

            #Checking if we already have the city
            foundCity = getIndex(cities, parts[2])
            #if the city did not already exist
            if foundCity == 'no':
                cities.append(City(parts[2]))
                foundCity = -1
                print cities[foundCity].name

            myFlight = Flight(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
            cities[foundCity].flights.append(myFlight)
    return graph(cities)

'''
filename = sys.argv[2]
q = open(filename, 'r')
for query in q.read().strip().split("["):
    if query != "": 
        parts = query.split(',')
        #WARNING SEE SPEC FOR PROPER PREFERENCES INPUT FORMAT
        myQuery = Query(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5],parts[6],parts[7])
        algorithm.getFlightSolutions(myQuery,cities)
'''