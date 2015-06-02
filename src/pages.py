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
            airlines= g.getAirlines() + ["None"]
            ))


class QueryHandler(tornado.web.RequestHandler):
    """Class which handles a request for flights"""
    def get(self):
        loader = tornado.template.Loader("templates/")

        date = self.get_argument("tDate")
        date = '/'.join(reversed(date.split('-')))
        prefs = self.get_argument("prefs").split(',')
        prefs[prefs.index("ffp")] = self.get_argument("ffpAirline")
        q = flightClasses.Query(
                date,
                self.get_argument("depTime"),
                self.get_argument("origCity"),
                self.get_argument("desCity"),
                prefs[0],
                prefs[1],
                prefs[2],
                int(self.get_argument("number")))

        try:
            self.write(loader.load("queryResponse.html").generate(
            trips = algorithm.getFlightSolutions(q,g)))
        except:
            self.write(loader.load("errorResponse.html").generate())