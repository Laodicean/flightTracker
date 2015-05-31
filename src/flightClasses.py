import datetime

class Flight:
    '''
    creates a flight class with the date, time, start city, end city, duration, airline and cost as paramaterised.
    '''
    def __init__(self, date, time, start, end, duration, airline, cost):
        self.date = date
        self.time = time
        self.start = start
        self.end = end
        self.duration = duration
        self.airline = airline
        self.cost = cost


class Trip:
    def __init__(self,date,time,start,end,currCal,cost,ffPoint,airlinePref):
        '''date+time as dateTime >> startCal+currCal
        start (city object) >> start, current
        end (city goal object) >> end
        currCal, cost and ffPoint aren't used for initilisation - should all be zeroed
        airlinePref >> airlinePref
        Empty list of flights the trip has taken called 'listFlights'
        '''
        
        
        self.startCal = convertTime(date,time)
        self.start = start
        self.current = start
        self.end = end
        self.currCal = startCal
        self.cost = cost
        self.ffPoint = ffPoint
        self.airlinePref = airlinePref
        self.listFlights = []

    def appendFlight(self,newFlight):
        """ This adds the flight 'newFlight' onto the end of the list of flights in 'listFlights'
        Takes in:
            Flight: newFlight
        returns:

        """
        self.current = newFlight.end
        self.currCal = convertTime(newFlight.date, newFlight.time)
        self.currCal = addDuration(self.currCal,newFlight)
        self.cost += newFlight.cost
        if self.airlinePref == newFlight.airline:
            self.ffPoint += newFlight.getFFPoints()
        self.listFlights.append(newFlight)

    def addDuration(self,startDate, flight):
        """ This adds the time that the entered flight takes onto the current time
        Takes in:
        DateTime: startDate
        flight: flight
        returns:
        DateTime: endDate
        """
        #increment by the duration of the flight in minutes
        endDate = startDate + datetime.timedelta(minutes = flight.duration)
        return endDate

    def convertTime(self,date,time):
        """ converts the given and time to a DateTime object
        Taken in:
        String: date
        String: time
        returns:
        DateTime: dateTime
        """
        #Creates a datetime from the paramatised date and time
        #Create time object
        timeSplit = time.split(':')
        timeObj = datetime.time(timeSplit[0], timeSplit[1]); #hours, minutes
        #Create date object
        currDate = date
        dateSplit = currDate.split('/')
        dateObj = datetime.date(dateSplit[2], dateSplit[0], dateSplit[1]) #year, day, month
        #combine into datetime object
        dateTime = datetime.datetime.combine(currDateObj, currTimeObj)
        return dateTime

class Query:
    '''
    date as int/int/int, time as int:int
    start and end cities, pref1, pref2 and pref3 as integers representing preferences of cost, time and ffpoints
    numFlights as integer
    '''
    def __init__(self,date,time,start,end,pref1,pref2,pref3,numFlights):
        self.date = date
        self.time = time
        self.start = start
        self.end = end
        self.pref1 = pref1
        self.pref2 = pref2
        self.pref3 = pref3
        self.numFlights = numFlights



COST_PREF = 0
TIME_PREF = 1
POINT_PREF = 2
# As a data structure for the results, since we can store flightplans as a list of flights, we'll be using an array of flightPlans (ordred by preference)
