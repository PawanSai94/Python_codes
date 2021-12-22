import os

print "Hello Pawan!"

prompt = '> '

f = open("timeSweep.scs","r")
f1 = open("time.scs","w")
f2 = open("pu_on.scs","w")
f3 = open("pu_off.scs","w")
f4 = open("pd_on.scs","w")
f5 = open("pd_off.scs","w")
#if f.mode =='r':
#	contents=f.read()
#	print contents

#f1=f.readlines()
for line in f:
	if "time" in line:
		print line
		f1.write(line)
	elif "Out_pu_on" in line:
		print line
		f2.write(line)
	elif "Out_pu_off" in line:
		print line
		f3.write(line)
	elif "Out_pd_on" in line:
		print line
		f4.write(line)
	elif "Out_pd_off" in line:
		print line
		f5.write(line)

	


