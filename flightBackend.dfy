datatype preferences = Time | Cost | ffPoint


class Query {
	var minutes: int
	var start: City;
	var end: City;
    var airlinePref: string;
	var pref1: preferences;
	var pref2: preferences;
	var pref3: preferences;
	var numFlights: int;
}

class Flight {
	var minutes: int
	var start: City;
	var end: City;
	var duration: int;
	var airline: string;
	var cost: int;
}

class City {
	var name : string;
	var flights : seq<Flight>;

	constructor init()
		modifies this;
		{
		flights := [];
		}
}

class Trip {
    var startCal: int
	var start: City;
	var current: City;
	var end: City;
	var currCal: int;
	var cost: int;
	var ffPoint: int;
	var airlinePref: string;
	var listFlights: seq<Flight>;

    constructor init(minutes: int, start: City, end: City, airlinePref: string)
        ensures this.startCal == minutes;
        ensures this.start == start;
        ensures this.current == start;
        ensures this.end == end;
        ensures this.currCal == this.startCal;
        ensures this.cost == 0;
        ensures this.ffPoint == 0;
        ensures this.airlinePref == airlinePref;
        ensures this.listFlights == [];
        modifies this;
    {
        this.startCal := minutes;
        this.start := start;
        this.current := start;
        this.end := end;
        this.currCal := startCal;
        this.cost := 0;
        this.ffPoint := 0;
        this.airlinePref := airlinePref;
        this.listFlights := [];
    }

    method appendFlight(newFlight: Flight)
        requires newFlight != null;
        modifies this;
    {
        this.current := newFlight.end;
        this.currCal := newFlight.minutes;
        this.currCal := this.addDuration(this.currCal, newFlight);
        this.cost := this.cost + newFlight.cost;
        if this.airlinePref == newFlight.airline
        {
            this.ffPoint := this.ffPoint + newFlight.duration;
        }
        this.listFlights := this.listFlights + [newFlight];
    }

    method addDuration(startDate: int, flight: Flight) returns (endDate: int)
        requires flight != null;
    {
        endDate := startDate + flight.duration;
    }
}

class Graph {
	var cities: seq<City>;

	constructor init ()
	ensures this.cities == [];
	modifies this;
	{
	cities := [];
	}

	method getFlights(x: Trip) returns (y: seq<Flight>)

		requires x != null;
        //ensures forall f: Flight | f in y :: f != null;
		{
			var potFlights : seq<Flight>;
			var currentCity : City;
			var index: int;
			assume this.cities != [];
			assume x.current != null;
			index := this.getIndex(this.cities, x.current);
		
			if index > -1
			{
				//assume 0 <= index < |cities|;
				currentCity := cities[index];
				var i: int;
				i := 0;
				assume currentCity != null;
				//we're assuming that the flights and cities have been added to the graph
				//since currentCity is getting an item from cities (in graph class that we're in)
				while i < |currentCity.flights|
				{	
					assume currentCity.flights[i] != null; 
					//we're assuming that the flights and cities have been added to the graph
					//because we're only verifying the algorithms in the code, not the parsing of data
					if currentCity.flights[i].minutes > x.currCal
					{
					y := y + [currentCity.flights[i]];
					}
					i := i + 1;
				}
			}

		}

	method getIndex(citys: seq<City>, searchingFor: City) returns (z : int)
		requires citys != [];
		requires searchingFor != null;
		ensures z < |citys|;
		{

			var j: int;
			j := 0;
			z := -1;
			while (j < |citys|) 
			{
				if citys[j] == searchingFor
				{
					z := j;
					break;
				}
				j := j + 1;
			}		

		}
	

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
	/*
predicate correctGraph (x: Graph)
    reads x;
		requires x != null;
		*/
	
method getFlightSolutions(query: Query, g: Graph) returns (flightList: seq<Trip>)
	requires query != null;
    requires g != null;
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
    requires query != null;
    requires g != null;
{
    var openQueue := new Queue<Trip>.init();
    var closedSet: set<Trip>;
    solutions := [];
    var firstTrip := new Trip.init(query.minutes, query.start, query.end, query.airlinePref);
    openQueue.put(firstTrip);

    while !openQueue.empty()
		//decreases (|openQueue.value|);
		//I1
		//invariant 	
    {
        var currTrip := openQueue.get();
        if !(currTrip in closedSet)
        {
            if currTrip.current == currTrip.end
            {
                currTrip.startCal := currTrip.listFlights[0].minutes;
                currTrip.currCal := currTrip.currCal - currTrip.startCal;
                currTrip.ffPoint := currTrip.ffPoint / 60; // assuming Dafny truncates the result like in Java/C
                solutions := solutions + [currTrip];
            } else {
                var appendList := [];
                appendList := g.getFlights(currTrip); //TODO: write this

                var i := 0;
                while i < |appendList|
                {
                    var currFlight := appendList[i];
                    
                    var newTrip := deepcopy(currTrip);
                    newTrip.appendFlight(currFlight);
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
    newT := new Trip.init(oldT.startCal, oldT.start, oldT.end, oldT.airlinePref);
    newT.current := oldT.current;
    newT.currCal := oldT.currCal;
    newT.cost := oldT.cost;
    newT.ffPoint := oldT.ffPoint;
    newT.listFlights := oldT.listFlights;
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
