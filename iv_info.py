import os

print "Hi Pawan!"
os.system("pwd")
vi_path = raw_input('Enter the info.info path for VI:\n')
def find_line():
	f = open(vi_path, "r")
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


def add_lines_vi():
	vi_prop = "\"PD_ref\" FLOAT DOUBLE\n\"GCL_ref\" FLOAT DOUBLE\n\"PU_ref\" FLOAT DOUBLE\n\"PCL_ref\" FLOAT DOUBLE\n\"Resolution\" FLOAT DOUBLE\n\"Vpower\" FLOAT DOUBLE\"\n"
	vi_end = "0\n0\n3.300000000000000e+00\n3.300000000000000e+00\n3000\n3.3\n"
	#vi_prop = "BAGGGY\n"
	#vi_end = "SMAAp\n"
	
	f = open(vi_path, "r")
	contents = f.readlines()

	prop_num, end_num = find_line()

	contents.insert(prop_num, vi_prop)
	contents.insert(end_num, vi_end)
	

	f = open(vi_path, "w+")
	contents = "".join(contents)
	f.write(contents)
	f.close()

add_lines_vi()
x = "gvim"+" "+vi_path
os.system(x)


