import os

print "Hi Pawan!"
os.system("pwd")
iv_path = raw_input('Enter the srcSweep.DC file path for IV:\n')
f = open(iv_path, "r")
contents = f.readlines()
contents = "".join(contents)
contents = contents.replace("vsweep", "v_sweep")
contents = contents.replace("I6:3", "Epulldown:1")
contents = contents.replace("I0:3", "Epullup:1")

f.close()
f = open(iv_path, "w+")
f.write(contents)
f.close()
x = "gvim"+" "+iv_path
os.system(x)