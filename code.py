import os

print "Hello Pawan!"

prompt = '> '

#print " Please provide the path spectre files:"
#path_entered = raw_input(prompt)
#path= os.path.join(path_entered)

os.system ("ls -f $PWD/*.sp > results.txt")

f = open("results.txt","r")
#if f.mode =='r':
#	contents=f.read()
#	print contents

f1=f.readlines()
for x in f1:
	print x
	y = "spectre" + " " + x
	print y
	os.system(y)


os.system("grep -rnw \"errors\" ./*.log")
os.system("grep -rnw \"premature\" ./*.log")


