#!/usr/bin/python3

#Tornado server file. Should not need to modify much.

import tornado
import pages

PORT = 8080

application = tornado.web.Application([
    #Example page handlers.
    (r"/", pages.LandingHandler),
    (r"/landing", pages.LandingHandler),
    (r"/query", pages.QueryHandler),
    ], debug=True
    )

if __name__ == "__main__":
    print("Starting tornado server on port {}".format(PORT))
    tornado.log.enable_pretty_logging()
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
