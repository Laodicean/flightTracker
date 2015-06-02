#!/usr/bin/python3
import time, datetime
import flightClasses
from operator import itemgetter
from queue import Queue #no module named queue?
from copy import deepcopy
def getFlightSolutions(query,g):
    """Retrieves a list of Trips containing soultions to the given query
    query: query object containing parameters for the search
    graph: Graph of cities
    """
    flightList = searchFlights(query,g)
    flightList = sortFlights(flightList,query)
    return flightList

def searchFlights(query,g):
    openQueue = Queue()
    closedSet = set()
    solutions = []
    solCounter = 0
    firstTrip = flightClasses.Trip(query.date,query.time,query.start,query.end,query.airlinePref)
    openQueue.put(firstTrip)
    while( not openQueue.empty() and solCounter < query.numFlights):
        currTrip = openQueue.get()
        if currTrip in closedSet:
            continue
        if (currTrip.current == currTrip.end):
            #currTrip.currCal = the amount of time between the provided start date and the eventual arrival time.
            currTrip.currCal = int(time.mktime(currTrip.currCal.timetuple()) - time.mktime(currTrip.startCal.timetuple())/60) #currCal may or may not be the right place to put this
            solutions.append(currTrip)
            solCounter += 1
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
    if query.pref1 == "Cost":
        if query.pref2 == "Time":
            return sorted(flightList, key=lambda f:(f.cost, f.currCal - f.startCal, f.ffPoint))
        else:#ffPoint
            return sorted(flightList, key=lambda f:(f.cost, f.ffPoint, f.currCal - f.startCal))
    elif query.pref1 == "Time":
        if query.pref2 == "Cost":
            return sorted(flightList, key=lambda f:(f.currCal - f.startCal, f.cost, f.ffPoint))
        else: #ffPoint
            return sorted(flightList, key=lambda f:(f.currCal - f.startCal, f.ffPoint, f.cost))
    else: #ffPoint
        if query.pref2 == "Cost":
            return sorted(flightList, key=lambda f:(f.ffPoint, f.cost, f.currCal - f.startCal))
        else: #time
            return sorted(flightList, key=lambda f:(f.ffPoint, f.currCal - f.startCal, f.cost))



