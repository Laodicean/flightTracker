import datetime

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
        s = "date:"+self.date
        s += " time:" + self.time
        s += " start:" + self.start
        s += " end:" + self.end
        s += " dur:" + str(self.duration)
        s += " airline:" + self.airline
        s += " cost:" + str(self.cost)
        return s

class Trip:
    def __init__(self,date,time,start,end,currCal,cost,ffPoint,airlinePref):
        self.startCal = self.convertTime(date,time)
        self.start = start
        self.current = start
        self.end = end
        self.currCal = self.startCal
        self.cost = cost
        self.ffPoint = ffPoint
        self.airlinePref = airlinePref
        self.listFlights = []

    def __repr__(self):
        x = str(self.startCal)
        x += " start:" + self.start
        x += " end:" + self.end
        x += " cost:" + str(self.cost)
        for f in self.listFlights:
            x += "\n   flight:" + str(f)

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
        dateObj = datetime.date(dateSplit[2], dateSplit[0], dateSplit[1]) #year, day, month
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
        self.pref1 = pref1
        self.pref2 = pref2
        self.pref3 = pref3
        self.numFlights = numFlights
    def __repr__(self):
        res = "date:"+self.date
        res += " time:"+self.time
        res += " start:"+self.start
        res += " end:"+self.end
        res += " pref1:"+str(self.pref1)
        res += " pref2:"+str(self.pref2)
        res += " pref3:"+str(self.pref3)
        res += " numFlights:"+str(self.numFlights)
        return res


COST_PREF = "cost"
TIME_PREF = "time"
POINT_PREF = "ffPoint"
# As a data structure for the results, since we can store flightplans as a list of flights, we'll be using an array of flightPlans (ordred by preference)
