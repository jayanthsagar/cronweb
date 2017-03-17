#from pycron import *
#from bash import bash
import subprocess
import re

class Crontab:
    def Get_jobs(self):
        f = open("./templates/list.html",'w')
        output =subprocess.check_output(["crontab", "-l"])
#        output = os.system('crontab -l')
        string =output.split()
        print string
        jobs=[]
        for i in range(0, len(string),6):
            jobs.append(string[i-1])
        f.write(str(jobs))

    def run_job(self,job):
        output =subprocess.check_output(job)

c = Crontab()
if __name__ == '__main__':
    c.Get_jobs()
