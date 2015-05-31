#!/usr/bin/python3
import graph
import flightClasses
import algorithm

#testing file for the project
g = graph.makeGraph("testFlights.txt")
for c in g.cities:
    print(c)

q = flightClasses.Query(
        "1/1/2000",
        "00:00",
        "Syd",
        "Wag",
        "cost",
        "time",
        "ffPoint",
        2)
print(q)

x = algorithm.getFlightSolutions(q,g)
for t in x:
    print(t)
