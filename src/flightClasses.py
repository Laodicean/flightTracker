class Flight:
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
		self.startCal = convertTime(date,time)
		self.start = start
		self.current = start
		self.end = end
		self.currCal = currCal
		self.cost = cost
		self.ffPoint = ffPoint
		self.airlinePref = airlinePref
		self.listFlights = []

	def appendFlight(self,newFlight):
		self.current = newFlight.end
		self.currCal += addDuration(self.currCal,newFlight)
		self.currCal += newFlight.currCal
		self.cost += newFlight.cost
		if self.airlinePref == newFlight.airline:
			self.ffPoint += newFlight.getFFPoints()
		self.listFlights.append(newFlight)
	def addDuration(startDate, flight):
	#Brayden, here is the function to get the time delay between the entered flight and the current time,
	#as well as the time of the flight (its probably easier to do it all in one)
		

	def convertTime(date,time):
		#This is something that you can use to convert date and time to a dateTime
        
class Query:
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
TIME_PREF = 0
POINT_PREF = 0
# As a data structure for the results, since we can store flightplans as a list of flights, we'll be using an array of flightPlans (ordred by preference)
