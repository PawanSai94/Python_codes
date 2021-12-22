import os

print "Hi Pawan!"
os.system("pwd")
vt_path = raw_input('Enter the TRAN file path for VT:\n')
f = open(vt_path, "r")
contents = f.readlines()
contents = "".join(contents)
contents = contents.replace("FALLING_HIGH_FIX", "Out_pd_on")
contents = contents.replace("FALLING_LOW_FIX", "Out_pd_off")
contents = contents.replace("RISING_HIGH_FIX", "Out_pu_on")
contents = contents.replace("RISING_LOW_FIX", "Out_pu_off")
f.close()
f = open(vt_path, "w+")
f.write(contents)
f.close()
x = "gvim"+" "+vt_path
os.system(x)