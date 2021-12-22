import os

print "Hi Pawan!"
os.system("pwd")
vt_path = raw_input('Enter the info.info path for VT:\n')
def find_line():
	f = open(vt_path, "r")
	lookup1='PROP'
	lookup2='END'
	for num, line in enumerate(f):
		if lookup1 in line:
			print line, num
			a= num
		if lookup2 in line:
			print line,num
			b=num
			return a,b
			f.close()


def add_lines_vt():
	vt_prop = "\"Vfx_pd_on\" FLOAT DOUBLE\n\"Vfx_pd_off\" FLOAT DOUBLE\n\"Vfx_pu_on\" FLOAT DOUBLE\n\"Vfx_pu_off\" FLOAT DOUBLE\n\"Rfx_pd_on\" FLOAT DOUBLE\n\"Rfx_pd_off\" FLOAT DOUBLE\n\"Rfx_pu_on\" FLOAT DOUBLE\n\"Rfx_pu_off\" FLOAT DOUBLE\n\"Cfx_pd_on\" FLOAT DOUBLE\n\"Cfx_pd_off\" FLOAT DOUBLE\n\"Cfx_pu_on\" FLOAT DOUBLE\n\"Cfx_pu_off\" FLOAT DOUBLE\n\"TimeDelay\" FLOAT DOUBLE\n\"Vpower\" FLOAT DOUBLE\n"
	vt_end = "3.300000000000000e+00\n3.300000000000000e+00\n0.000000000000000e+00\n0.000000000000000e+00\n1000\n1000\n1000\n1000\n0.000000000000000e+00\n0.000000000000000e+00\n0.000000000000000e+00\n0.000000000000000e+00\n0\n3.3\n"
	#vi_prop = "BAGGGY\n"
	#vi_end = "SMAAp\n"
	
	f = open(vt_path, "r")
	contents = f.readlines()

	prop_num, end_num = find_line()

	contents.insert(prop_num, vt_prop)
	contents.insert(end_num, vt_end)
	

	f = open(vt_path, "w+")
	contents = "".join(contents)
	f.write(contents)
	f.close()

add_lines_vt()
#os.startfile(vt_path)
x = "gvim"+" "+vt_path
os.system(x)


