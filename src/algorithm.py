#!/usr/bin/python3
import flightClasses
from operator import itemgetter
from queue import Queue #no module named queue?

def getFlightSolutions(query,graph):
    """Retrieves a list of Trips containing soultions to the given query
    query: query object containing parameters for the search
    graph: Graph of cities
    """
    flightList = searchFlights(query,graph)
    flightList = sortFlights(flightList,query)
    return flightList

def searchFlights(query,graph):
    q = Queue()
    visited = Queue()
    openQueue = q
    closedQueue = visited
    solutions = []
    solCounter = 0
    firstTrip = flightClasses.Trip(query.date,query.time,query.start,query.end,0,0,0,"")
    openQueue.put(firstTrip)
    while( not openQueue.empty() & solCounter < query.numFlights):
        currTrip = openQueue.get()
        if (currTrip.current == currTrip.end):
            solutions.append(currTrip)
            solCounter += 1
        else:
            appendList = []
            appendList = graph.getFlights(currTrip)
            for currFlight in appendList:
                newTrip = currTrip.clone()
                newTrip.appendFlight(currFlight)
                if (currTrip not in closedQueue & currTrip not in openQueue):
                    openQueue.put(newTrip)

        closedQueue.put(currTrip)
    return solutions


def sortFlights(flightList,query):
    if query.pref1 == "cost":
        if query.pref2 == "time":
            return sorted(flightList, key=lambda f:(f.cost, f.curCal - f.startCal, f.ffPoint))
        else:#ffPoint
            return sorted(flightList, key=lambda f:(f.cost, f.ffPoint, f.curCal - f.startCal))
    elif query.pref1 == "time":
        if query.pref2 == "cost":
            return sorted(flightList, key=lambda f:(f.curCal - f.startCal, f.cost, f.ffPoint))
        else: #ffPoint
            return sorted(flightList, key=lambda f:(f.curCal - f.startCal, f.ffPoint, f.cost))
    else: #ffPoint
        if query.pref2 == "cost":
            return sorted(flightList, key=lambda f:(f.ffPoint, f.cost, f.curCal - f.startCal))
        else: #time
            return sorted(flightList, key=lambda f:(f.ffPoint, f.curCal - f.startCal, f.cost))



