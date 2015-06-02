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
        #setup and call search function
        #
        #
        a = self.request.arguments

        self.write(loader.load("queryResponse.html").generate(
            var=[i+"->"+str(a[i]) for i in a.keys()],
            uri=self.request.uri
            ))
