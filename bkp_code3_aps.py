import os

print "Hello Pawan!"

prompt = '> '

#print " Please provide the path aps files:"
#path_entered = raw_input(prompt)
#path= os.path.join(path_entered)

os.system ("ls -f $PWD/*.spi > results.txt")

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
m = file.readline()
n = file.readline()
o = file.readline()
p = file.readline()
q = file.readline()
r = file.readline()
#s = file.readline()
#t = file.readline()
#u = file.readline()
#v = file.readline()
#w = file.readline()
#x = file.readline()
#y = file.readline()

a0cat = a [-12:]
b0cat = b [-12:]
c0cat = c [-12:]
d0cat = d [-12:]
e0cat = e [-12:]
f0cat = f [-12:]
g0cat = g [-12:]
h0cat = h [-12:]
i0cat = i [-12:]
j0cat = j [-12:]
k0cat = k [-12:]
l0cat = l [-12:]
m0cat = m [-12:]
n0cat = n [-12:]
o0cat = o [-12:]
p0cat = p [-12:]
q0cat = q [-12:]
r0cat = r [-12:]
#s0cat = s [-12:]
#t0cat = t [-12:]
#u0cat = u [-12:]
#v0cat = v [-12:]
#w0cat = w [-12:]
#x0cat = x [-12:]
#y0cat = y [-12:]


print a0cat
oa = a0cat.replace("spi","out")
ob = b0cat.replace("spi","out")
oc = c0cat.replace("spi","out")
od = d0cat.replace("spi","out")
oe = e0cat.replace("spi","out")
of = f0cat.replace("spi","out")
og = g0cat.replace("spi","out")
oh = h0cat.replace("spi","out")
oi = i0cat.replace("spi","out")
oj = j0cat.replace("spi","out")
ok = k0cat.replace("spi","out")
ol = l0cat.replace("spi","out")
om = m0cat.replace("spi","out")
on = n0cat.replace("spi","out")
oo = o0cat.replace("spi","out")
op = p0cat.replace("spi","out")
oq = q0cat.replace("spi","out")
orr = r0cat.replace("spi","out")
#os = s0cat.replace("spi","out")
#ot = t0cat.replace("spi","out")
#ou = u0cat.replace("spi","out")
#ov = v0cat.replace("spi","out")
#ow = w0cat.replace("spi","out")
#ox = x0cat.replace("spi","out")
#oy = y0cat.replace("spi","out")

print oa
ma =a0cat.replace("spi","msg")
mb =b0cat.replace("spi","msg")
mc =c0cat.replace("spi","msg")
md =d0cat.replace("spi","msg")
me =e0cat.replace("spi","msg")
mf =f0cat.replace("spi","msg")
mg =g0cat.replace("spi","msg")
mh =h0cat.replace("spi","msg")
mi =i0cat.replace("spi","msg")
mj =j0cat.replace("spi","msg")
mk =k0cat.replace("spi","msg")
ml =l0cat.replace("spi","msg")
mm =m0cat.replace("spi","msg")
mn =n0cat.replace("spi","msg")
mo =o0cat.replace("spi","msg")
mp =p0cat.replace("spi","msg")
mq =q0cat.replace("spi","msg")
mr =r0cat.replace("spi","msg")
#ms =s0cat.replace("spi","msg")
#mt =t0cat.replace("spi","msg")
#mu =u0cat.replace("spi","msg")
#mv =v0cat.replace("spi","msg")
#mw =w0cat.replace("spi","msg")
#mx =x0cat.replace("spi","msg")
#my =y0cat.replace("spi","msg")

print ma
#c = file.readline()
#d = file.readline()
#e = file.readline()
#f = file.readline()
#g = file.readline()
#h = file.readline()
#i = file.readline()
#j = file.readline()
#k = file.readline()
#l = file.readline()
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
m = m[:-1]
n = n[:-1]
o = o[:-1]
p = p[:-1]
q = q[:-1]
r = r[:-1]
#s = s[:-1]
#t = t[:-1]
#u = u[:-1]
#v = v[:-1]
#w = w[:-1]
#x = x[:-1]
#y = y[:-1]

#g = g[:-1]
#h = h[:-1]
#i = i[:-1]
#j = j[:-1]
#k = k[:-1]
#l = l[:-1]
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

#a1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + a + "\""
#a1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + a +  "\""
a1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + a + " -r " + oa + " =l " + ma +  "\""
b1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + b + " -r " + ob + " =l " + mb +  "\""
c1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + c + " -r " + oc + " =l " + mc +  "\""
d1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + d + " -r " + od + " =l " + md +  "\""
e1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + e + " -r " + oe + " =l " + me +  "\""
f1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + f + " -r " + of + " =l " + mf +  "\""
g1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + g + " -r " + og + " =l " + mg +  "\""
h1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + h + " -r " + oh + " =l " + mh +  "\""
i1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + i + " -r " + oi + " =l " + mi +  "\""
j1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + j + " -r " + oj + " =l " + mj +  "\""
k1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + k + " -r " + ok + " =l " + mk +  "\""
l1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + l + " -r " + ol + " =l " + ml +  "\""
m1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + m + " -r " + om + " =l " + mm +  "\""
n1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + n + " -r " + on + " =l " + mn +  "\""
o1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + o + " -r " + oo + " =l " + mo +  "\""
p1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + p + " -r " + op + " =l " + mp +  "\""
q1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + q + " -r " + oq + " =l " + mq +  "\""
r1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + r + " -r " + orr+ " =l " + mr +  "\""
#s1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + s + " -r " + os + " =l " + ms +  "\""
#t1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + t + " -r " + ot + " =l " + mt +  "\""
#u1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + u + " -r " + ou + " =l " + mu +  "\""
#v1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + v + " -r " + ov + " =l " + mv +  "\""
#w1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + w + " -r " + ow + " =l " + mw +  "\""
#x1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + x + " -r " + ox + " =l " + mx +  "\""
#y1  = "gnome-terminal --tab -e " + "\"" + "spectre -f nutascii -cols 132 +errpreset=conservative" + " " + y + " -r " + oy + " =l " + my +  "\""


#b1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + b + "\""
#c1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + c + "\""
#d1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + d + "\""
#e1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + e + "\""
#f1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + f + "\""
#g1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + g + "\""
#h1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + h + "\""
#i1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + i + "\""
#j1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + j + "\""
#k1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + k + "\""
#l1 = "gnome-terminal --tab -e " + "\"" + "aps" + " " + l + "\""

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

z =  a1 + " ; " + b1 + " ; " + c1 + " ; " + d1 + " ; " + e1 + " ; " + f1 + " ; " + g1 + " ; " + h1 + " ; " + i1 + " ; " + j1 + " ; " + k1 + " ; " + l1 + " ; " + m1 + " ; " + n1 + " ; " + o1 + " ; " + p1 + " ; " + q1 + " ; " + r1 
#+ " ; " + s1 + " ; " + t1 + " ; " + u1 + " ; " + v1 + " ; " + w1 + " ; " + x1 + " ; " + y1 

print z

os.system(z)
os.system("echo grep -rnw \"errors\" ./*.log")
os.system("echo grep -rnw \"premature\" ./*.log")
#p = "gnome-terminal --tab -e \"aps dout2_ivmax.sp\" ; gnome-terminal --tab -e \"aps dout2_ivmin.sp\" ; gnome-terminal --tab -e \"aps dout2_ivtyp.sp\""

#p = "gnome-terminal --tab -e \"/scratch/user/pawansai/maxim_ibis/sim/ds1088_project/ds1088_redo/dout/Models/dout2/IBIS/dout2_ivmax.sp\" ; gnome-terminal --tab -e \"/scratch/user/pawansai/maxim_ibis/sim/ds1088_project/ds1088_redo/dout/Models/dout2/IBIS/dout2_ivmin.sp\" ; gnome-terminal --tab -e \"/scratch/user/pawansai/maxim_ibis/sim/ds1088_project/ds1088_redo/dout/Models/dout2/IBIS/dout2_ivtyp.sp\""


#os.system()


#f1=f.readlines()
#for x in f1:
#	print x
#	y = "aps" + " " + x
#	print y
#	#os.system(y)
#	z = "gnome-terminal --tab"
#	os.system(z)
#	os.system(y)





