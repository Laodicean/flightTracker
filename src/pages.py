#Pages definition file. Page response handler classes should be defined here.
import tornado.web
import tornado.template

class LandingHandler(tornado.web.RequestHandler):
    """Class which allows users to make requests for flights
    Additionally, request responses will be displayed as an element of the
    page this class genereates.
    """
    def get(self):
        loader = tornado.template.Loader("templates/")
        self.write(loader.load("landing.html").generate())


class QueryHandler(tornado.web.RequestHandler):
    """Class which handles a request for flights"""
    def get(self):
        self.write("Error")
    def post(self):
        loader = tornado.template.Loader("templates/")
        self.write(loader.load("queryResponse.html").generate())
