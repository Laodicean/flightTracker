def getFlightSolutions(query):
    flightList[query.numFlights] = searchFlights(query)
    flightList = sortFlights(flightList,query)
    return flightList

def sortFlight(flightList,query):
    swaps = 1
    passes = 0
    while (passes <query.numFlight-1 && swaps != 0):
        counter = 0
        swaps = 0
        while (counter < query.numFlights - 1):
            current = compare(flightList[counter],flightList[counter+1],query.pref1)
           if (current == 1):
               #swap
               swaps = 1
           elif (current == -1):
               currPref2 = compare(flightList[counter],flightList[counter+1],query.pref2)
               if (currPref2 == 1):
                   #swap
                   swap = 1
               elif (currPref2 == -1):
                   currPref3 = compare(flightList[counter],flightList[counter+1],query.pref3)
                   if (currPref3 == 1):
                       #swap
                       swap = 1
            counter ++
        passes ++
        
                    

def compare(one,two,comparator):
           if (comparator = POINT_PREF):
               if (one.ffPoint > two.ffPoint):
                   return 1
               elif (one.ffPoint == two.ffPoint):
                   return -1
           else:
               if(comparator = TIME_PREF):
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
