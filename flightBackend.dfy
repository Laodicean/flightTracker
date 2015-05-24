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
