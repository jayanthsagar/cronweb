from pycron import *
from bash import bash

class Crontab:
    def Get_jobs(self):
        f = open("./templates/list.html",'w')
        output = bash('crontab -l')
        f.write(str(output))

