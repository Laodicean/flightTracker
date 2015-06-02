#!/usr/bin/python3
import graph
import flightClasses
import algorithm

#testing file for the project
g = graph.makeGraph("testdata")


q = flightClasses.Query(
        "29/2/2000",
        "08:40",
        "Adelaide",
        "Singapore",
        "Qantas",
        "Cost",
        "Time",
        1)

x = algorithm.getFlightSolutions(q,g)
ret = flightClasses.printSolutions(q,x)
print (ret)
