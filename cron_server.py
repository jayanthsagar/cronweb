#!/bin/python
# Services exposed by the VM Manager
# The REST url :
# http://host-name/api/1.0/disk-usage
# http://host-name/api/1.0/running-time
# http://host-name/api/1.0/mem-usage
# http://host-name/api/1.0/running-processes
# http://host-name/api/1.0/cpu-load
# http://host-name/api/1.0/execute/<command>
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
        c.run_job(post_data['cronjob'])
        self.render('result.html')

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
