import datetime
def printSolutions(q,x):
    ret = "( " + str(q) + "\n, ["
    for t in x:
        ret += str(t)
        if t != x[-1]:
            ret += "\n"
    ret += "])"
    return ret

class Flight:
    def __init__(self, date, time, start, end, duration, airline, cost):
        self.date = date
        self.time = time
        self.start = start
        self.end = end
        self.duration = duration
        self.airline = airline
        self.cost = cost

    def __repr__(self):
        s = "[ " + self.date
        s += ", " + self.time
        s += ", " + self.start
        s += ", " + self.end
        s += ", " + str(self.duration)
        s += ", " + self.airline
        s += ", " + str(self.cost)
        s += " ]"
        return s

class Trip:
    def __init__(self,date,time,start,end,airlinePref):
        self.startCal = self.convertTime(date,time)
        self.start = start
        self.current = start
        self.end = end
        self.currCal = self.startCal
        self.cost = 0
        self.ffPoint = 0
        self.airlinePref = airlinePref
        self.listFlights = []

    def __repr__(self):
        x = "(( "
        for f in self.listFlights:
            x += str(f)
            if f != self.listFlights[-1]:
                x += "\n"
        x += " ), " + str(self.cost)
        x += ", " + str(self.currCal)
        x += ", " + str(self.ffPoint)
        x += ")"
        return x

    def appendFlight(self,newFlight):
        """ This adds the flight 'newFlight' onto the end of the list of flights in 'listFlights'
        Takes in:
            Flight: newFlight
        returns:

        """
        self.current = newFlight.end
        self.currCal = self.convertTime(newFlight.date, newFlight.time)
        self.currCal = self.addDuration(self.currCal,newFlight)
        self.cost += newFlight.cost
        if self.airlinePref == newFlight.airline:
            self.ffPoint += newFlight.duration
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
        endDate = startDate + datetime.timedelta(minutes = int(flight.duration))
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
        timeSplit = [int(i) for i in time.split(':')]
        timeObj = datetime.time(timeSplit[0], timeSplit[1]); #hours, minutes
        #Create date object
        currDate = date
        dateSplit = [int(i) for i in currDate.split('/')]
        dateObj = datetime.date(dateSplit[2], dateSplit[1], dateSplit[0]) #year, day, month
        #combine into datetime object
        dateTime = datetime.datetime.combine(dateObj, timeObj)
        return dateTime

class Query:
    def __init__(self,date,time,start,end,pref1,pref2,pref3,numFlights):
        """Create a query class
        date = num/num/num
        time = num:num
        start = origin city
        end = dest city
        pref1 = [0-2]
        pref2 = [0-2]
        pref3 = [0-2]
        numFlights = int of the number of flights to be returned"""


        self.date = date
        self.time = time
        self.start = start
        self.end = end
        self.airlinePref = ""
        self.pref1 = self.getPref(pref1)
        self.pref2 = self.getPref(pref2)
        self.pref3 = self.getPref(pref3)
        self.numFlights = numFlights

    def getPref(self,preference):
    	if (preference != "Cost" and preference != "Time"):
    		self.airlinePref = preference
    		return "ffPoint"
    	else:
    		return preference

    def __repr__(self):
        res = "[ " + self.date
        res += ", "+self.time
        res += ", "+self.start
        res += ", "+self.end
        if self.pref1 == "ffPoint" :
            res += ", ("+str(self.airlinePref)
        else :
            res += ", ("+str(self.pref1)

        if self.pref2 == "ffPoint" :
            res += ", "+str(self.airlinePref)
        else :
            res += ", "+str(self.pref2)

        if self.pref3 == "ffPoint" :
            res += ", "+str(self.airlinePref)
        else :
            res += ", "+str(self.pref3)


        res += "), "+str(self.numFlights)
        res += " ]"
        return res


COST_PREF = "cost"
TIME_PREF = "time"
POINT_PREF = "ffPoint"
# As a data structure for the results, since we can store flightplans as a list of flights, we'll be using an array of flightPlans (ordred by preference)
