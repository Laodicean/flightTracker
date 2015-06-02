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
        "Cost",
        "Time",
        "Qantas",
        2)

x = algorithm.getFlightSolutions(q,g)
ret = flightClasses.printSolutions(q,x)
print (ret)
