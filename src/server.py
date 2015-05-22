#!/usr/bin/python3

#Tornado server file. Should not need to modify much.

import tornado.ioloop
import pages

PORT = 8080

application = tornado.web.Application([
    #Example page handlers.
    (r"/", pages.IndexHandler),
    (r"/random", pages.RandomHandler),
    (r"/sseTest", pages.SSEHandler),
    (r"/sseTestPage", pages.SSETestPageHandler),
    (r"/query", pages.QueryHandler),
    (r"/landing", pages.LandingHandler),
])

if __name__ == "__main__":
    print("Starting tornado server on port {}".format(PORT))
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
