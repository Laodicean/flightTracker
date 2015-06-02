
datatype preferences = time | cost | flyerPoints

class Date {
	var day: int;
	var month: int;
    var year: int;
/*
	constructor init()
	modifies this;
	
	{
	correctDate(this)
	}
	*/
	/*predicate correctDate(x:Date)
	reads x;
		requires x != null 
		{ x.day >= 0 && x.day <= 31 &&
		  x.month > 0 && x.month <= 12
		}
		*/
}

class Time {
	var minute: int;
	var hour: int;
}

class Query {
	var date: Date;
	var time: Time;
	var start: string;
	var end: string;
    var airlinePref: preferences;
	var pref1: preferences;
	var pref2: preferences;
	var pref3: preferences;
	var numFlights: int;

	constructor init() 

}

class Flight {
	var date: Date;
	var time: Time;
	var start: string;
	var end: string;
	var duration: int;
	var airline: string;
	var cost: int;
}

class City {
	var name : string;
	var flights : seq<Flight>;
	/*
	constructor init()
	modifies this;
	ensures flights != null;
	{
		flights := new seq<Flight>;
	}
	*/
}

class Trip {
    var startCal: (Date, Time);
	var start: string;
	var current: string;
	var end: string;
	var currCal: (Date, Time);
	var cost: int;
	var ffPoint: int;
	var airlinePref: preferences;
	var listFlights: seq<Flight>;

    constructor init(date: Date, time: Time, start: string, end: string, airlinePref: preferences)
        modifies this;
    {
        this.startCal := (date, time);
        this.start := start;
        this.current := start;
        this.end := end;
        this.currCal := startCal;
        this.cost := 0;
        this.ffPoint := 0;
        this.airlinePref := airlinePref;
        this.listFlights := [];
    }
}

class Graph {
	var cities: seq<City>;

	constructor init()
	modifies this;
	ensures cities == [];
	{
		cities := [];
	}

	method getFlights(x: Trip) returns (y: seq<Flight>)

		{
		var potFlights : seq<Flight>;
		var currentCity : int;
		currentCity := this.getIndex(cities, currentCities);
		}

	method get
	

}
/*
predicate correctPref(c:preferences) 
	ensures c in {time, cost, flyerPoints} ;


predicate correctTime(x: Time)
	reads x;
		ensures x != null;
		ensures x.minute >= 0;
		ensures x.minute < 60;
		ensures x.hour >= 0;
		ensures x.hour < 24;
		
predicate correctDate(x:Date)
	reads x;
		ensures x != null 
		ensures x.day >= 0
		ensures x.month > 0 
		ensures x.month <= 12 
		//since the upper bound is varied for days (28, 29, 30, 31), 
		//we can't explicitly denote that, unless you want it to be <= 31...

predicate correctQuery (x: Query)
	reads x;
		requires x != null;
		ensures correctTime(x.time);
		ensures correctDate(x.date);
		ensures correctPref(x.pref1) && correctPref(x.pref2) && correctPref(x.pref3)
		//need to ensure start and end are in the graph class...
		ensures x.numFlights > 0;
		//second thoughts...we're not parsing the data here... so we need to have correct datas ...
		//might need to ensure everything else is not null or valid

//need to make pre-post for following, ensuring that data collected from these are correct
//just so we can use it for later onwards, unless we don't have too?
predicate correctFlight (x: Flight, y: Graph)
	reads x;
	reads y;
		requires x != null;
		requires y != null;
		requires correctGraph(y);
		ensures correctTime(x.time);
		ensures correctDate(x.date);
		ensures exists u : City :: (u != null && u in y.cities && u.name == x.start);
		ensures exists u : City :: (u != null && u in y.cities && u.name == x.dest);

predicate correctCity (x: City, y : Graph)
	reads x;
	reads y;
		requires x != null;
		requires y != null;
		requires correctGraph(y);

predicate correctTrip (x: Trip)
    reads x;
	*/
predicate correctGraph (x: Graph)
    reads x;

	
method getFlightSolutions(query: Query, g: Graph) returns (flightList: seq<Trip>)
	requires query != null;
//	requires correctQuery(query);
//    requires correctGraph(g);

    //ensures that flightList matches the spec!
{

    flightList := searchFlights(query, g);
//	ghost var oldFlightList
	assume flightList != [];
    flightList := sortFlights(flightList, query);
}


method searchFlights(query: Query, g: Graph) returns (solutions: seq<Trip>)

{
    var openQueue := new Queue<Trip>.init();
    var closedSet: set<Trip>;
    solutions := [];
    var firstTrip := new Trip.init(query.date, query.time, query.start, query.end, query.airlinePref);
    openQueue.put(firstTrip);
    while !openQueue.empty()
    {
        var currTrip := openQueue.get();
        if !(currTrip in closedSet)
        {
            if currTrip.current == currTrip.end
            {
                currTrip.startCal := (currTrip.listFlights[0].date, currTrip.listFlights[0].time);
                currTrip.currCal := compare(currTrip.currCal, currTrip.startCal); //TODO: write this
                currTrip.ffPoint := currTrip.ffPoint / 60; // assuming that Dafny truncates the result like Java/C
                solutions := solutions + [currTrip];
            } else {
                var appendList := [];
                appendList := g.getFlights(currTrip); //TODO: write this

                var i := 0;
                while i < |appendList|
                {
                    var currFlight := appendList[i];
                    
                    var newTrip := deepcopy(currTrip); //TODO: write this
                    newTrip.appendFlight(currFlight); //TODO: write this
                    openQueue.put(newTrip);

                    i := i + 1;
                }
            }
            closedSet := closedSet + {currTrip};
        }
    }
}


 method sortFlights(flightList: seq<Trip>, query: Query) returns (sortedList: seq<Trip>)
	requires query != null;
	requires flightList != [] && |flightList| > 0;

//	ensures a sorted list
// for i j, if i > j ==> seq[i] > seq[j]

	{
	}

method deepcopy(oldT: Trip) returns (newT: Trip)
    requires oldT != null;
    ensures newT != null;
    ensures newT != oldT;
    ensures newT.startCal == oldT.startCal;
	ensures newT.start == oldT.start;
	ensures newT.current == oldT.current;
	ensures newT.end == oldT.end;
	ensures newT.currCal == oldT.currCal;
	ensures newT.cost == oldT.cost;
	ensures newT.ffPoint == oldT.ffPoint;
	ensures newT.airlinePref == oldT.airlinePref;
	ensures newT.listFlights == oldT.listFlights;
{
    newT := new Trip.init(oldT.startCal.0, oldT.startCal.1, oldT.start, oldT.end, oldT.airlinePref);
}

method compare(cal1: (Date, Time), cal2: (Date, Time)) returns (difference: int)
{

}


// Generic queue class
class Queue<T> {
    var value: seq<T>;

    constructor init()
        ensures value == [];
        modifies this;
    {
        value := [];
    }

    method put(x: T)
        ensures value == old(value) + [x];
        modifies this;
    {
        value := value + [x];
    }
	
    method get() returns (r: T)
        requires value != [];
        ensures r == old(value[0]);
        ensures value == old(value[1..]);
        modifies this;
    {
        r := value[0];
        value := value[1..];
    }

    function method empty(): bool
        reads this;
    {
        value == []
    }
}
