from sys import argv
import linecache
script, filename, newfile = argv

def first(s):
    return s[:1]

target = open(filename)
newtarget = open(newfile, 'w')
text = target.readlines()
for j in (text):
	if((j[0]=='R')):
		print j
		#modified_j = j[0]+j[1]+j[2]+j[3]+j[4]+'('+j[5]+j[6]+j[7]+j[8]+j[9]+j[10]+j[11]+j[12]+')'+j[13]+"resistor r="+j[14]+j[15]+j[16]+j[17]+j[18]+" * rmult"
		modified_j = j[0:5]+'('+j[5:13]+')'+j[13]+"resistor r="+j[14:19]+" * rmult"
		print modified_j
		newtarget.write(modified_j)
		newtarget.write("\n")
	elif ((j[0]=='L')):
		print j
		modified_j = j[0:5]+'('+j[5:13]+')'+j[13]+"inductor l="+j[14:-1]
		print modified_j
		newtarget.write(modified_j)
		newtarget.write("\n")
	elif ((j[0]=='C')):
		print j
		if((j[0]+j[1])=="CP"):
			modified_j = j[0:7]+'('+j[7:15]+')'+j[15]+"capacitor c="+j[16:-1]
			newtarget.write(modified_j)
			newtarget.write("\n")
		else:
	 		modified_j = j[0:4]+'('+j[4:9]+')'+j[9]+"capacitor c="+j[10:-1]
			print modified_j
			newtarget.write(modified_j)
			newtarget.write("\n")
	elif ((j[0]=='K')):
		modified_j = j[0:9]+"mutual_inductor ind1="+j[9:14]+" ind2="+j[14:19]+"coupling="+j[21:-1]
		print modified_j
		newtarget.write(modified_j)
		newtarget.write("\n")

	else:
		newtarget.write(j)
		#newtarget.write("\n")

target.close()
newtarget.close()

