
datatype preferences = time | cost | flyerPoints

class Date {
	var day: int;
	var month: int;

}

class Time {
	var minute: int;
	var hour: int;
}

class Query {
	var date: Date;
	var time: Time;
	var Start: string;
	var Dest: string;
	var pref1: preferences;
	var pref2: preferences;
	var pref3: preferences;
	var numFlight: int;

	constructor init() 
		
}

class Flight {
	var date: Date;
	var time: Time;
	var Start: string;
	var Dest: string;
	var duration: int;
	var airline: string;
	var cost: int;
}

class City {
	var name : string;
	var flights : array<Flight>;
	
	constructor init()
	modifies this;
	ensures flights != null;
	{
		flights := new array<Flight>;
	}
}

class Trip {
	var start: string;
	var current: string;
	var end: string;
	//carrCal??
	var cost: int;
	var ffPoint: int;
	var airLinePref: preferences;
	var listFlights: array<Flight>;

    constructor init()
    {
        
    }
}

class Graph {
	var cities: array<City>;
}

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
		//need to ensure start and dest are in the graph class...
		ensures x.numFlight > 0;
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

predicate correctGraph (x: Graph)
    reads x;


method getFlightSolutions(query: Query, g: Graph) returns (flightList: array<Trip>)
	requires query != null;
	requires correctQuery(query);
    requires correctGraph(g);
    //ensures that flightList matches the spec!
{
    flightList := searchFlights(query, g);
    flightList := sortFlights(flightList, query);
}


method searchFlights(query: Query, g: Graph) returns (solutions: array<Trip>)
{
    var openQueue := new Queue<Trip>.init();
    var closedSet: set<Trip>;
    var solCounter := 0;
    var firstTrip := new Trip.init();
}


function method sortFlights(flightList: array<Trip>, query: Query): array<Trip>
	/*requires query != null;
	requires query.date != null;
	requires query.time != null;
	requires correctQuery(query);
    reads query;*/


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
