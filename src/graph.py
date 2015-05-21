import sys, datetime

class Flight():
    def __init__(self, date, time, start, end, duration, airline, cost):
    	self.date = date
    	self.time = time
	self.start = start
	self.end = end
	self.duration = duration
	self.airline = airline
	self.cost = cost

class City():
    def __init__(self, name):
        self.name = name
        self.flights = []

       
class graph():
    def __init__(self, cities):
        self.cities = cities

    def getFlights(trip):

        
    
        potFlights = []
        
        current = trip.current
        
        currTime = trip.listFlights[-1].time
        timeSplit = parts = currTime.split(':')
        currDate = trip.listFlights[-1].date
        dateSplit = currDate.split('/')

        tripCal = dateTime()
        tripCal.replace(dateSplit[0], dateSplit[1], dateSplit[2], timeSplit[0], timeSplit[1], 0)
        print tripCal
        flightEstimate = trip.listFlights[-1].duration
        timeSplit[0] += duration%60
        
        


        return potFlights


        



def getIndex(cities, searchingFor):
    i = -1
    for city in cities:
        i+=1
        if city.name == searchingFor:
            return i

    return 'no'
            


filename = sys.argv[1]
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
        
        
 #   flights = []
#    flights.append()
    
    


#Class Flight:
#    def __init__ (self, date, time, start, end, duration, airline, cost):

