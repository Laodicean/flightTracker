#!/usr/bin/python3
import graph
import flightClasses
import algorithm
import sys

def makeQueries(filename):
    """creates a graph(list of cities) from the flightdata file
    returns a list of cities (each containing a list of flights)"""
    f = open(filename, 'r')
    queries = []
    for q in f.read().replace("\n","").replace("]","").replace(" ","").strip().split("["):
        if q != "":
        	q = q.replace("(","")
        	q = q.replace(")","")
        	parts = q.split(',')
        	currQ = flightClasses.Query(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], int(parts[7]))
        	queries.append(currQ)
    return queries

#testing file for the project
g = graph.makeGraph(sys.argv[1])

q = makeQueries(sys.argv[2])


for k in q:
	x = algorithm.getFlightSolutions(k,g)
	ret = str(flightClasses.printSolutions(k,x)) + "\n"
	print (ret)



