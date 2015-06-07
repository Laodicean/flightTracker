#!/usr/bin/python3
import time, datetime
import flightClasses
from operator import itemgetter
from queue import Queue #no module named queue?
from copy import deepcopy
def getFlightSolutions(query,g):
    """
    Precondition: 
        query != null && query.start != null && query.end != null
        && g != null;
        && g.cities != [] && null !in g.cities && forall c: City | c in g.cities :: null !in c.flights
    """
    """Retrieves a list of Trips containing soultions to the given query
    query: query object containing parameters for the search
    graph: Graph of cities
    """
    flightList = searchFlights(query,g)
    flightList = sortFlights(flightList,query)
    return flightList[:query.numFlights]

def searchFlights(query,g):
    """
    Precondition:
        query != null && query.start != null && query.end != null
        && g != null;
        && g.cities != [] && null !in g.cities && forall c: City | c in g.cities :: null !in c.flights
    """
    openQueue = Queue()
    closedSet = set()
    solutions = []
    firstTrip = flightClasses.Trip(query.date,query.time,query.start,query.end,query.airlinePref)
    openQueue.put(firstTrip)
    while( not openQueue.empty()):
        """
        invariant forall t: Trip | t in openQueue.value :: t.current != null;
        invariant forall t: Trip | t in openQueue.value :: (forall f: Flight | f in t.listFlights :: f != null);
        """
        currTrip = openQueue.get()
        if currTrip in closedSet:
            continue
        if (currTrip.current == currTrip.end):
        	airlineFlag = 0
        	if query.pref1 == "ffPoint" and query.airlinePref != "None":
        		for lookFlight in currTrip.listFlights:
        			if lookFlight.airline != query.airlinePref:
        				airlineFlag = 1
        	
        	if airlineFlag == 0:	#currTrip.currCal = the amount of time between the provided start date and the eventual arrival time.
		        currTrip.startCal = currTrip.convertTime(currTrip.listFlights[0].date,currTrip.listFlights[0].time)
		        currTrip.currCal = int((time.mktime(currTrip.currCal.timetuple()) - time.mktime(currTrip.startCal.timetuple()))/60) #currCal may or may not be the right place to put this
		        solutions.append(currTrip)
        else:
            appendList = []
            appendList = g.getFlights(currTrip)
            for currFlight in appendList:
                newTrip = deepcopy(currTrip)
                newTrip.appendFlight(currFlight)
                openQueue.put(newTrip)

        closedSet.add(currTrip)
    return solutions


def sortFlights(flightList,query):
    """
    Precondition:
        query != null
    """
    if query.pref1 == "Cost":
        if query.pref2 == "Time":
            return sorted(flightList, key=lambda f:(f.cost, f.currCal, -f.ffPoint))
        else:#ffPoint
            return sorted(flightList, key=lambda f:(f.cost, -f.ffPoint, f.currCal))
    elif query.pref1 == "Time":
        if query.pref2 == "Cost":
            return sorted(flightList, key=lambda f:(f.currCal, f.cost, -f.ffPoint))
        else: #ffPoint
            return sorted(flightList, key=lambda f:(f.currCal, -f.ffPoint, f.cost))
    else: #ffPoint
        if query.pref2 == "Cost":
            return sorted(flightList, key=lambda f:(-f.ffPoint, f.cost, f.currCal))
        else: #time
            return sorted(flightList, key=lambda f:(-f.ffPoint, f.currCal, f.cost))



