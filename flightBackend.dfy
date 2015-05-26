
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
		requires x.time != null;
		requires x.date != null;
		ensures correctTime(x.time);
		ensures correctDate(x.date);
		ensures correctPref(x.pref1) && correctPref(x.pref2) && correctPref(x.pref3)
		//need to ensure start and dest are in the graph class...
		ensures x.numFlight > 0;
		//now thinking about it...I don't think we need to have correctTime
		//and correctDate... since the user can input invalid numbers, thus we cannot ensure this...
		//second thoughts...we're not parsing the data here... so we need to have correct datas ...
		//might need to ensure everything else is not null or valid

method getFlightSolutions(query: Query, graph: Graph) returns (flightList: array<Trip>)
	requires query != null;
	requires query.date != null;
	requires query.time != null;
	//above keeps dafny quiet, because we're assuming that we've already parsed the required data
	requires correctQuery(query);
	//need to do something about the graph

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
