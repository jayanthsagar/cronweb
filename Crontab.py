import subprocess
import re
import logging

jobs_dict = {}
class Crontab:
    def Get_jobs(self):
        f = open("./templates/list.html",'w')
        output =subprocess.check_output(["crontab", "-l"])
#        output = os.system('crontab -l')
        string =output.split()
        jobs=[]
        logging.info("current running crons: "+ str(string))
# Ignore content variable. It is jus for styling purpose
        content='''{% extends "base.html" %}{% block CSS %}body {    background: #FFF;    text-align: center;    font-family: georgia;}#container {    margin: 0 auto;    width: 960px;}img{    display: inline-block;}h1 {    font-size: 4em;    border-bottom: 1px solid #dddddd;    margin: 4%;}h2 {    font-size: 3.5em;    border-bottom: 1px solid #dddddd;    margin: 2%;}p {    font-size: 2em;}.field {     padding: 2%;     margin: 1px;}.textbox {    font-family: monospace;}.textbox:focus {    outline: none;    border: 2px solid #6EA2DE;    box-shadow: 0 0 2px #95B9C7;}label {    margin-left: 1%;}input { display: inline-block;}{% end %}{% block title %}            cronweb{% end %}{% block header %}    List of jobs {% end %}{% block body %}'''+output
        for i in range(0, len(string),6):
            jobs.append(string[i-1])
#            content +='<form action="/list" method="post"><div class="field"><label> <input type="text" value="'+string[i-1]+'" name ="cronjob" id="cronjob" class="textbox"><input type="submit"  value = "run this job"></input></div></form>'
#        content +='{% end %}'
#        print type(jobs)
#        jobs_dict={}
        for i, v in enumerate(jobs):
            jobs_dict[i]= v
            content +='<form action="/list" method="post"><div class="field"><label> job '+str(i+1)+':<input type="text" value="'+v+'" name ="cronjob" id="cronjob" class="textbox"></input><label>arguments: <input type="text" value=" " name="arguments" id="arguments"class="textbox"></input><input type="submit"  value = "run this job"></input></div></form>'
        content +='{% end %}'
        print jobs_dict
        f.write(content)

    def run_job(self,job,arguments=" "):
        for key,value in jobs_dict.iteritems():
            if value == job:
                output =subprocess.check_output(value+arguments,shell=True)
                f = open("./templates/result.html",'w')
                f.write(output)
                return 'TRUE'

c = Crontab()
if __name__ == '__main__':
    c.Get_jobs()

