#from pycron import *
#from bash import bash
import subprocess
import re
import logging

class Crontab:
    def Get_jobs(self):
        f = open("./templates/list.html",'w')
        output =subprocess.check_output(["crontab", "-l"])
#        output = os.system('crontab -l')
        string =output.split()
        logging.info("current running crons: "+ str(string))
        jobs=[]
        content='''{% extends "base.html" %}{% block CSS %}body {    background: #FFF;    text-align: center;    font-family: georgia;}#container {    margin: 0 auto;    width: 960px;}img{    display: inline-block;}h1 {    font-size: 4em;    border-bottom: 1px solid #dddddd;    margin: 4%;}h2 {    font-size: 3.5em;    border-bottom: 1px solid #dddddd;    margin: 2%;}p {    font-size: 2em;}.field {     padding: 2%;     margin: 1px;}.textbox {    font-family: monospace;}.textbox:focus {    outline: none;    border: 2px solid #6EA2DE;    box-shadow: 0 0 2px #95B9C7;}label {    margin-left: 1%;}input { display: inline-block;}{% end %}{% block title %}            cronweb{% end %}{% block header %}    List of jobs {% end %}{% block body %}'''+output
        for i in range(0, len(string),6):
            jobs.append(string[i-1])
            content +='<form action="/list" method="post"><div class="field"><label> <input type="text" value="'+string[i-1]+'" name ="cronjob" id="cronjob" class="textbox"><input type="submit"  value = "run this job"></input></div></form>'
        content +='{% end %}'
        f.write(content)

    def run_job(self,job):
        output =subprocess.check_output(job)
        f = open("./templates/result.html",'w')
        f.write(output)

c = Crontab()
if __name__ == '__main__':
    c.Get_jobs()
