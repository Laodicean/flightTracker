class Date {
	var day: int;
	var month: int;
}

class Time {
	var minute: int;
	var hour: int;
}

function method correctTime(x: Time): bool
	reads x;
	{
		x != null && x.minute >= 0 && x.minute <= 60 && x.hour >= 0 && x.hour <= 60  
	}

function method correctDate(x:Date) : bool
	reads x;
	{
		x != null && x.day >= 0 && x.month > 0 && x.month <= 12 
		//since the upper bound is varied for days (28, 29, 30, 31), we can't explicitly denote that
	}

class Query {
	var date: Date;
	var time: Time;
	var Start: string;
	var Dest: string;
	var pref1: string;
	var pref2: string;
	var pref3: string;
	var numFlight: int;

	constructor init () 
		ensures correctDate(date);
		ensures correctTime(time);
}


/*
function method correctQuery (x: Query) : bool

	reads x;

	{	
		x != null
	}
*/



method getFlightSolutions(query: Query, graph: Graph) returns (flightList: array<Trip>)

method searchFlights(query: Query, graph: Graph) returns (solutions: array<Trip>)

method sortFlights(flightList: array<Trip>, query: Query)
	




// Abstract queue class
class Queue<T> {
    ghost var value: seq<T>;

    constructor init()
        ensures value == [];
        modifies this;

    method put(x: T)
        ensures value == old(value) + [x];
        modifies this;
	
    method get() returns (r: T)
        requires value != [];
        ensures r == old(value[0]);
        ensures value == old(value[1..]);
        modifies this;

    method empty() returns (r: bool)
        ensures r <==> value == [];

    method contains(x: T) returns (r: bool)
        ensures r <==> x in value;
}
