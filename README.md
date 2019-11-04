# IPChecker
Run this script to continually check your ip address for those of us that cannot afford a static one. Will send an email from your specified email address to the email address you specified if your ip changes.
# How to use it
Fill out all of the fields in the smtp.config.json file.
Then run ```python check_ip.py```
You will get an email on the first check and every check that a change is detected in thereafter.
