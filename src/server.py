#!/usr/bin/python3

#Tornado server file. Should not need to modify much.

import tornado
import os
import pages 
import sys

if len(sys.argv) < 2:
    pages.g = pages.graph.makeGraph('testData')
else:
    pages.g = pages.graph.makeGraph(sys.argv[1])

PORT = 8080

application = tornado.web.Application([
    #Example page handlers.
    (r"/", pages.LandingHandler),
    (r"/landing", pages.LandingHandler),
    (r"/query", pages.QueryHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), "static")})
    ], debug=True
    )

if __name__ == "__main__":
    print("Starting tornado server on port {}".format(PORT))
    tornado.log.enable_pretty_logging()
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
