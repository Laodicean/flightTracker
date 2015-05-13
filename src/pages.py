#Pages definition file. Page response handler classes should be defined here.
import tornado.web
import tornado.template
import random


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
