#Pages definition file. Page response handler classes should be defined here.
import tornado.web
import tornado.template
import random
import json

class SSEHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.set_header('Content-Type', 'text/event-stream')
        self.set_header('Cache-Control', 'no-cache')

    def emit(self, data, event=None):
        """
        Actually emits the data to the waiting JS
        """
        response = u''
        encoded_data = json.dumps(data)
        if event != None:
            response += u'event: ' + unicode(event).strip() + u'\n'

        response += u'data: ' + encoded_data.strip() + u'\n\n'

        self.write(response)
        self.flush()
    def get(self):
        self.emit("Hello, world!")


class SSETestPageHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader("templates/")
        self.write(loader.load("sseTest.html").generate())

class QueryHandler(tornado.web.RequestHandler):
    counter = 0;
    def get(self):
        self.write("Hello get " + str(self.counter))
        self.counter += 1
    def post(self):
        self.write("Hello post " + str(self.counter))
        self.counter -= 1

class LandingHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader("templates/")
        self.write(loader.load("landing.html").generate())
    def post(self):
        get(self)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class RandomHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader("templates/")

        minimum = self.get_argument("min", "1")
        maximum = self.get_argument("max", "1000")

        if not minimum.isnumeric():
            minimum = 1
        else:
            minimum = int(minimum)

        if not maximum.isnumeric():
            maximum = 1000
        else:
            maximum = int(maximum)


        lines = []
        for i in range(10):
            lines.append(random.randint(minimum,maximum))

        lines = sorted(lines)

        self.write(loader.load("test.html").generate(lines = lines,min=minimum, max=maximum))
    def post(self):
        self.get()
