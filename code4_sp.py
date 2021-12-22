import os

print "Hello Pawan!"

prompt = '> '

#print " Please provide the path spectre-15.10.345-da files:"
#path_entered = raw_input(prompt)
#path= os.path.join(path_entered)

os.system ("ls -f $PWD/*.sp > results.txt")

file = open("results.txt","r")
#if f.mode =='r':
#	contents=f.read()
#	print contents

a = file.readline()
b = file.readline()
c = file.readline()
d = file.readline()
e = file.readline()
f = file.readline()
g = file.readline()
h = file.readline()
i = file.readline()
j = file.readline()
k = file.readline()
l = file.readline()
# print a
# print b
# print c
# print d
# print e
# print f
# print g
# print h
# print i
# print j
# print k
# print l
a = a[:-1]
b = b[:-1]
c = c[:-1]
d = d[:-1]
e = e[:-1]
f = f[:-1]
g = g[:-1]
h = h[:-1]
i = i[:-1]
j = j[:-1]
k = k[:-1]
l = l[:-1]
# print a
# print b
# print c
# print d
# print e
# print f
# print g
# print h
# print i
# print j
# print k
# print l

a1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + a + "\""
b1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + b + "\""
c1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + c + "\""
d1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + d + "\""
e1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + e + "\""
f1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + f + "\""
g1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + g + "\""
h1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + h + "\""
i1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + i + "\""
j1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + j + "\""
k1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + k + "\""
l1 = "gnome-terminal --tab -e " + "\"" + "spectre-15.10.345-da" + " " + l + "\""

# print a1
# print b1
# print c1
# print d1
# print e1
# print f1
# print g1
# print h1
# print i1
# print j1
# print k1
# print l1

z =  a1 + " ; " + b1 + " ; " + c1 + " ; " + d1 + " ; " + e1 + " ; " + f1 + " ; " + g1 + " ; " + h1 + " ; " + i1 + " ; " + j1 + " ; " + k1 + " ; " + l1

# print z

os.system(z)
os.system("echo grep -rnw \"errors\" ./*.log")
os.system("echo grep -rnw \"premature\" ./*.log")
#p = "gnome-terminal --tab -e \"spectre-15.10.345-da dout2_ivmax.sp\" ; gnome-terminal --tab -e \"spectre-15.10.345-da dout2_ivmin.sp\" ; gnome-terminal --tab -e \"spectre-15.10.345-da dout2_ivtyp.sp\""

#p = "gnome-terminal --tab -e \"/scratch/user/pawansai/maxim_ibis/sim/ds1088_project/ds1088_redo/dout/Models/dout2/IBIS/dout2_ivmax.sp\" ; gnome-terminal --tab -e \"/scratch/user/pawansai/maxim_ibis/sim/ds1088_project/ds1088_redo/dout/Models/dout2/IBIS/dout2_ivmin.sp\" ; gnome-terminal --tab -e \"/scratch/user/pawansai/maxim_ibis/sim/ds1088_project/ds1088_redo/dout/Models/dout2/IBIS/dout2_ivtyp.sp\""


#os.system()


#f1=f.readlines()
#for x in f1:
#	print x
#	y = "spectre-15.10.345-da" + " " + x
#	print y
#	#os.system(y)
#	z = "gnome-terminal --tab"
#	os.system(z)
#	os.system(y)





