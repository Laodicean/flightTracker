#!/usr/bin/python3
import graph
import flightClasses
import algorithm
import sys

def makeQueries(filename, g):
    """creates a graph(list of cities) from the flightdata file
    returns a list of cities (each containing a list of flights)"""
    f = open(filename, 'r')
    queries = []
    #replace("]","")
    for q in f.read().replace("\n","").replace(" ","").strip().split("["):
        if q != "":
        	q = q.replace("(","")
        	q = q.replace(")","")
        	parts = q.split(',')
            
            #invalid entry cases
            #Checking that the query has 8 parts
            if len(parts) != 8:
                print 'incorrectly formatted flight data'
                exit(1)
            tempDate = parts[0].split['/']
            #checking there are 3 parts of date
            else if len(tempDate) != 3:
                print 'incorrectly formatted flight data'
                exit(1)
            #checking they are all numbers
            else if !isinstance( tempDate[0], int) and !isinstance( tempDate[1], int) and !isinstance( tempDate[2], int):
                print 'incorrectly formatted flight data'
                exit(1)
            tempTime = parts[1].split[':']:
            #checking time is number:number
            else if len(tempTime) != 2:
                print 'incorrectly formatted flight data'
                exit(1)
            #checking that the hours and minutes are integers
            else if !isinstance( tempTime[0], int) and !isinstance( tempTime[1], int):
                print 'incorrectly formatted flight data'
                exit(1)
            #check the names of cities are strings
            else if !isinstance( parts[2], str) !isinstance( parts[3], str):
                print 'incorrectly formatted flight data'
                exit(1)          
            #check if the names start with a capital
            else if !parts[2][0].isupper() and !parts[3][0].isupper():
                print 'incorrectly formatted flight data'
                exit(1)
            #check the names of the cities are not the same
            else if parts[2] == parts[3]:
                print 'incorrectly formatted flight data'
                exit(1)
            #Checking preference order
            else if !(parts[4] == ('Cost' or 'Time' or (parts[4] in g.getAirlines())) and parts[5] == ('Cost' or 'Time' or (parts[4] in g.getAirlines())) and parts[6] = ('Cost' or 'Time' or (parts[4] in g.getAirlines())):
                print 'incorrectly formatted flight data'
                exit(1)
            else if parts[7][-1] != ']':
                print 'incorrectly formatted flight data'
                exit(1)
            parts[7] = parts[7][:-1]
            else if !isinstance( parts[7], int):
                print 'incorrectly formatted flight data'
                exit(1)
            
        	currQ = flightClasses.Query(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], int(parts[7]))
        	queries.append(currQ)
    return queries

#testing file for the project
g = graph.makeGraph(sys.argv[1])

q = makeQueries(sys.argv[2], g)


for k in q:
	x = algorithm.getFlightSolutions(k,g)
	ret = str(flightClasses.printSolutions(k,x)) + "\n"
	print (ret)



