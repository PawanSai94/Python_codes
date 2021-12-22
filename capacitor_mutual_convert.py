from sys import argv
import linecache
script, filename, newfile = argv

def first(s):
    return s[:1]

target = open(filename)
newtarget = open(newfile, 'w')
text = target.readlines()
for j in (text):
	if((j[0]=='C')):
		print j
		#modified_j = j[0]+j[1]+j[2]+j[3]+j[4]+'('+j[5]+j[6]+j[7]+j[8]+j[9]+j[10]+j[11]+j[12]+')'+j[13]+"resistor r="+j[14]+j[15]+j[16]+j[17]+j[18]+" * rmult"
		modified_j = j[0:7]+'('+j[7:14]+')'+ " capacitor c="+j[15:-1]
		print modified_j
		newtarget.write(modified_j)
		newtarget.write("\n")
	
	else:
		newtarget.write(j)
		#newtarget.write("\n")

target.close()
newtarget.close()

