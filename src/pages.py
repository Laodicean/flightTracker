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
    def post(self):


class QueryHandler(tornado.web.RequestHandler):
    """Class which handles a request for flights"""
    counter = 0;
    def get(self):
        self.write("Hello get " + str(self.counter))
        self.counter += 1
    def post(self):
        self.write("Hello post " + str(self.counter))
        self.counter -= 1

       get(self)
