#!/usr/bin/python3
import flightClasses
#import Queue #no module named queue?

def getFlightSolutions(query,graph):
    """Retrieves a list of Trips containing soultions to the given query
    query: query object containing parameters for the search
    graph: Graph of cities
    """
    flightList[query.numFlights] = searchFlights(query,cities)
    flightList = sortFlights(flightList,query)
    return flightList

def searchFlights(query,cities):
    q = Queue.Queue()
    visited = Queue.Queue()
    openQueue = q
    closedQueue = visited
    solutions = []
    solCounter = 0
    firstTrip = flightClasses.Trip(query.date,query.time,query.start,query.end,0,0,0)
    openQueue.put(firstTrip)
    while( not openeQueue.empty() & solCounter < query.numFlights):
        currTrip = openeQueue.get()
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


def sortFlight(flightList,query):
    swaps = 1
    passes = 0
    while (passes <query.numFlight-1 & swaps != 0):
        counter = 0
        swaps = 0
        while (counter < query.numFlights - 1):
            current = compare(flightList[counter],flightList[counter+1],query.pref1)
            if current == 1:
                solutionSwap(flightList,counter);
                swaps = 1
            elif (current == -1):
                currPref2 = compare(flightList[counter],flightList[counter+1],query.pref2)
                if (currPref2 == 1):
                    solutionSwap(flightList,counter);
                    swap = 1
                elif (currPref2 == -1):
                    currPref3 = compare(flightList[counter],flightList[counter+1],query.pref3)
                    if (currPref3 == 1):
                        solutionSwap(flightList,counter);
                        swap = 1
            counter += 1
        passes += 1

def compare(one,two,comparator):
    if (comparator == POINT_PREF):
        if (one.ffPoint > two.ffPoint):
            return 1
        elif (one.ffPoint == two.ffPoint):
            return -1
    else:
        if(comparator == TIME_PREF):
            if(one.duration < two.duration):
                return 1
            elif(one.duration == two.duration):
                return -1
        else:
            if (one.cost < two.cost):
                return 1
            elif (one.cost < two.cost):
                return -1
    return 0


def solutionSwap(flightList,counter):
    temp = flightList[counter]
    flightList[counter] = flightList[counter + 1]
    flightList[coutner +1] = temp
