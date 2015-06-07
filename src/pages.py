#Pages definition file. Page response handler classes should be defined here.
import tornado.web
import tornado.template
import graph
import flightClasses
import algorithm

g = graph.makeGraph("testFiles/testdata2")

class LandingHandler(tornado.web.RequestHandler):
    """Class which allows users to make requests for flights
    Additionally, request responses will be displayed as an element of the
    page this class genereates.
    """
    def get(self):
        loader = tornado.template.Loader("templates/")
        self.write(loader.load("landing.html").generate(
            cities=sorted(g.getCityNames()),
            airlines=["None"] + g.getAirlines()
            ))


class QueryHandler(tornado.web.RequestHandler):
    """Class which handles a request for flights"""
    def get(self):
        loader = tornado.template.Loader("templates/")


        if (self.get_argument("origCity") == self.get_argument("desCity")):
            self.write(loader.load("errorResponse.html").generate(msg="The origin and destination city you entered are the same"))
        else:
            date = self.get_argument("tDate")
            date = '/'.join(reversed(date.split('-')))
            prefs = self.get_argument("prefs").split(',')
            prefs[prefs.index("ffp")] = self.get_argument("ffpAirline")
            n = self.get_argument("number")
            n = int(n) if n else 0
            q = flightClasses.Query(
                    date,
                    self.get_argument("depTime"),
                    self.get_argument("origCity"),
                    self.get_argument("desCity"),
                    prefs[0],
                    prefs[1],
                    prefs[2],
                    n)
            try:
                solutions = algorithm.getFlightSolutions(q,g);
                if len(solutions) > 0:
                    self.write(loader.load("queryResponse.html").generate(trips = solutions))
                else:
                    self.write(loader.load("noFlights.html").generate())
            except Exception as e:
                self.write(loader.load("errorResponse.html").generate(msg="Please check your input, and try again"))
                #raise e #debugging line
