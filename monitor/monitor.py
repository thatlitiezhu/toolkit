import requests, time, os, sys

while True:
	r = requests.get('http://yacs.me/api/4/sections/?crn=75196').json()
	seats = 100 - r['result'][0]['seats_taken']
	if seats >= 1:
		while True:
			os.system('say "Alert! Seats available in social psychology!"')
			print (str(seats) + '\n') *22
	time.sleep(960)
	sys.stdout.write('\a')
	sys.stdout.flush()