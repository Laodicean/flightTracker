#Pages definition file. Page response handler classes should be defined here.
import tornado.web
import tornado.template
import graph
import flightClasses
import algorithm

g = graph.makeGraph("testFlights.txt")

class LandingHandler(tornado.web.RequestHandler):
    """Class which allows users to make requests for flights
    Additionally, request responses will be displayed as an element of the
    page this class genereates.
    """
    def get(self):
        loader = tornado.template.Loader("templates/")
        self.write(loader.load("landing.html").generate(
            cities=g.getCityNames(),
            ))


class QueryHandler(tornado.web.RequestHandler):
    """Class which handles a request for flights"""
    def get(self):
        loader = tornado.template.Loader("templates/")

        date = self.get_argument("tDate")
        date = '/'.join(reversed(date.split('-')))

        q = flightClasses.Query(
                date,
                self.get_argument("depTime"),
                self.get_argument("origCity"),
                self.get_argument("desCity"),
                "Cost",
                "Time",
                "None",
                int(self.get_argument("number")))


        self.write(loader.load("queryResponse.html").generate(
            trips = algorithm.getFlightSolutions(q,g)
            ))
