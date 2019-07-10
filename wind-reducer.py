#! /usr/bin/env python
import sys

speeds = dict()
# for the extension we will need another dictionary
# counts = dict()

for line in sys.stdin:
	try:
		line = line.strip()
		station, speed = line.split('\t')
		speed = float(speed)
		if station in speeds:
			speeds[station] = speed if speed > speeds[station] else speeds[station]    
		else: 
			speeds[station] = speed
	except ValueError:
		pass

for k, v in speeds.iteritems():
	print (speeds)
	# add code here to output the results
