#!/bin/python
# Services exposed by cronweb
# The REST url :
# http://host-name/
# http://host-name/list
import urlparse
import os
import os.path
import json
# bunch of tornado imports
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import Crontab
import logging

define("port", default=8000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class List_of_jobs(tornado.web.RequestHandler):

    def get(self):
       c= Crontab.Crontab()
       c.Get_jobs()
       self.render('list.html')

    def post(self):
        post_data = dict(urlparse.parse_qsl(self.request.body))
        c = Crontab.Crontab()
        logging.info("Recieved POST request with post-data: "+ str(post_data))
        a = 'FALSE'
        if len(post_data.keys())==2:
            a = c.run_job(post_data['cronjob'],post_data['arguments'])
        else:
            a = c.run_job(post_data['cronjob'])
        if a =='TRUE':
            self.render('result.html')
        else:
            self.render('error.html')

if __name__ == "__main__":
        tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
			(r"/", MainHandler),
                        (r"/list", List_of_jobs),
		        ],
		        template_path=os.path.join(os.path.dirname(__file__), "templates"),debug = True)
	http_server = tornado.httpserver.HTTPServer(app)
	current_file_path = os.path.dirname(os.path.abspath(__file__))
	options.port = 8080
	logging.info("cronweb_server: It will run on port : "+str(options.port))
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
