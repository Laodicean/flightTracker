datatype preferences = Time | Cost | ffPoint

// The variable minutes is used here in the Dafny code
// to represent Python's datetime, where minutes is
// the number of minutes since January 1, 2000
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
        //requires start != null;
		//requires end != null;
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
		requires x.current != null;
        requires correctCities(this.cities);
        ensures null !in y;
		ensures forall f: Flight | f in y :: x.currCal < f.minutes;
		{
            y := [];
			var potFlights : seq<Flight>;
			var currentCity : City;
			var index: int;
			index := this.getIndex(this.cities, x.current);
		
			if index > -1
			{

				currentCity := cities[index];
				var i: nat;
				i := 0;
				while i < |currentCity.flights|
					//I1
					invariant i <= |currentCity.flights|
					//I2
					invariant forall j: nat :: j < i ==> currentCity.flights[j] != null;
					//I3
					//this invariant says that if y is empty, nothing is in that list, otherwise 
					//if y is not empty, then an element (x1 - Flight) is in y
					invariant y == [] ==> (forall x1 : Flight :: x1 in currentCity.flights ==> x1 !in y) &&  
					y != [] ==> (forall x1 : Flight :: x1 in currentCity.flights && x1.minutes > x.currCal ==> x1 in y);
                    //I4
                    invariant null !in y;
                    //I5
                    invariant forall f: Flight | f in y :: x.currCal < f.minutes;

					//decreases (|currentCity.flights| - i) // Not required
				{	
					if currentCity.flights[i].minutes > x.currCal
					{
						y := y + [currentCity.flights[i]];
					}
					i := i + 1;
				}
			}
	}

	method getIndex(citys: seq<City>, searchingFor: City) returns (z : int)
		//requires citys != [];
		requires searchingFor != null;
		ensures z < |citys|;
		{
			var j: nat;
			j := 0;
			z := -1;
			while (j < |citys|) && z == -1

			invariant j <= |citys|;
			invariant forall i: nat :: i < j ==> citys[i] != searchingFor;

			//decreases (|citys| - j) // Not required
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
	
predicate correctQuery(q: Query)
    reads q;
{
    q != null && q.start != null && q.end != null && q.start != q.end
}

predicate correctCities(cities: seq<City>)
    reads cities;
{
    null !in cities && forall c: City | c in cities :: null !in c.flights
}

predicate flightInGraph(f: Flight, g: Graph)
    reads f, g;
{
    g != null && f != null && f.end in g.cities && f.start in g.cities
}


// This is main backend function which searches the graph to produce solutions to the given query
method searchFlights(query: Query, g: Graph) returns (solutions: seq<Trip>)
    requires correctQuery(query);
    requires g != null;
    requires correctCities(g.cities);
    requires forall c: City | c in g.cities :: forall f: Flight | f in c.flights :: flightInGraph(f, g);
    ensures forall t: Trip | t in solutions :: t != null;
    decreases *;
{
    var openQueue := new Queue<Trip>.init();
    var closedSet: set<Trip>;
    solutions := [];
    var firstTrip := new Trip.init(query.minutes, query.start, query.end, query.airlinePref);
    openQueue.put(firstTrip);

    while !openQueue.empty()
        invariant null !in openQueue.value;
        invariant forall t: Trip | t in openQueue.value :: fresh(t);
        invariant forall t: Trip | t in openQueue.value :: t.current != null;
        invariant forall t: Trip | t in openQueue.value :: (forall f: Flight | f in t.listFlights :: f != null);
        invariant forall t: Trip | t in openQueue.value :: t != firstTrip ==> |t.listFlights| > 0;
        invariant firstTrip.current != firstTrip.end;
        invariant forall t: Trip | t in solutions :: t != null;
		decreases *;
    {
		
        var currTrip := openQueue.get();
        if !(currTrip in closedSet)
        {
            if currTrip.current == currTrip.end
            {
                var airlineFlag := 0;
                if query.pref1 == ffPoint && query.airlinePref != "None"
                {
                    var j := 0;
                    while j < |currTrip.listFlights|
                    {
                        var lookFlight := currTrip.listFlights[j];

                        if lookFlight.airline != query.airlinePref
                        {
                            airlineFlag := 1;
                        }

                        j := j + 1;
                    }
                }
                if airlineFlag == 0
                {
                    currTrip.startCal := currTrip.listFlights[0].minutes;
                    currTrip.currCal := currTrip.currCal - currTrip.startCal;
                    solutions := solutions + [currTrip];
                }
            } else {
                var appendList := [];
                appendList := g.getFlights(currTrip);

                var i := 0;
                while i < |appendList|
                    invariant null !in openQueue.value;
                    invariant forall t: Trip | t in openQueue.value :: fresh(t);
                    invariant forall t: Trip | t in openQueue.value :: t.current != null;
                    invariant forall t: Trip | t in openQueue.value :: (forall f: Flight | f in t.listFlights :: f != null);
                    invariant forall t: Trip | t in openQueue.value :: t != firstTrip ==> |t.listFlights| > 0;
                    invariant firstTrip.current != firstTrip.end;
                {
                    var currFlight := appendList[i];
                    
                    var newTrip := deepcopy(currTrip);
                    newTrip.appendFlight(currFlight);
                    assume newTrip.current != null;
                    assume forall f: Flight | f in newTrip.listFlights :: f != null;
                    assume newTrip != firstTrip ==> |newTrip.listFlights| > 0;
                    openQueue.put(newTrip);

                    i := i + 1;
                }
            }
            closedSet := closedSet + {currTrip};
        }
    }
}


method deepcopy(oldT: Trip) returns (newT: Trip)
    requires oldT != null;
    //requires oldT.start != null;
    //requires oldT.end != null;
    ensures newT != null;
    ensures fresh(newT);
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
		ensures |value| == old (|value|) + 1
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
