import urllib.request as req
from threading import Timer
from sys import argv
from smtplib import SMTP
import json
import os

dirpath = os.getcwd()
config = {}
with open(dirpath + '/smtp.config.json') as jf:
    config = json.load(jf)

server = SMTP(config['smtp_server'], config['smtp_port'])
server.starttls()
server.login(config['from_address'], config['password'])

last_ip = ''


def send_email(new_ip):
    global server
    server.sendmail(
        config['from_address'],
        config['to_address'],
        new_ip
    )


def check():
    ip_check = req.urlopen("http://icanhazip.com/")
    ip = ip_check.read().decode('utf-8').strip()
    global last_ip
    if last_ip != ip:
        last_ip = ip
        send_email(ip)

    Timer(config['check_interval_in_seconds'], check).start()


print('Checks begin.')
try:
    check()
finally:
    server.quit()
