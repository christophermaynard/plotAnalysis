#!/opt/python/gnu/2.7.9/bin/python

import sys

def timeins(timestr):
        nsecs=timestr.split(".")
        secs=nsecs[0][4:]
        mins=nsecs[0][2:4]
        hours=nsecs[0][0:2]
        ts = 3600*float(hours) + 60*float(mins) + float(secs) + float(nsecs[1])/1000.0
        return ts

def tstamp(search_string, file):
	f = open(file)
	ts=0
	for line in f:
		if search_string in line:
			print line
			words=line.split()
			ts=timeins(words[1])
			return ts
#	close(file)
	return ts

#for file in sys.argv[1:]:
string1 = sys.argv[1]
string2 = sys.argv[2]
file = sys.argv[3]

ts1 = tstamp(string1,file)
ts2 = tstamp(string2,file)
print ts1
print ts2
print ts2-ts1

