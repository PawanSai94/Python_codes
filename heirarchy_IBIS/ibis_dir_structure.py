import os

print "\n\n********************* IBIS Database Directory Structure*******************\n"
print "Hello, Good Day!\n"

prompt = '> '

print "Your current working directory is:"
os.system("echo $PWD")

print "\n Please provide the path of IC Manage Library:"
path_entered = raw_input(prompt)
path_name = os.path.join(path_entered)

if ((not path_entered)):
    print "\n You have to specify a path! Cannot Proceed further. ABORTED!\n"
    exit()


print "\nPlease provide the die name"
die_name = raw_input(prompt)
DIE_NAME = die_name.upper()

print "\nPlease provide part number:"
part_num = raw_input(prompt)
PART_NUM = part_num.upper()

print "\nPlease provide IBIS JIRA Request MOD Number:"
mod_num = raw_input(prompt)
MOD_NUM = mod_num.upper()

if ((not DIE_NAME) & (not PART_NUM) & (not MOD_NUM)):
    print ("\n You did not give me any details !!! Directory not created!\n")
    exit()
elif ((not DIE_NAME) & (not PART_NUM)):
    total = MOD_NUM
elif ((not DIE_NAME) & (not MOD_NUM)):
    total = PART_NUM
elif ((not MOD_NUM) & (not PART_NUM)):
    total = DIE_NAME
elif (not DIE_NAME):
    total = PART_NUM+'_'+MOD_NUM
elif (not PART_NUM):
    total = DIE_NAME + '_' + MOD_NUM
elif (not MOD_NUM):
    total = DIE_NAME + '_' + PART_NUM
else:
    total = DIE_NAME+'_'+PART_NUM+'_'+MOD_NUM
#print total
path = path_name + '/' + total
print path
os.mkdir ( path , 0755);

sub1 = path + '/Input_Database'
os.mkdir (sub1 , 0755)
sub2 = path + '/Development/IBIS_Generation'
os.makedirs ( sub2 , 0755 );
sub3 = path + '/Development/IBIS_Generation/netlist'
os.makedirs ( sub3 , 0755 );
sub4 = path + '/Development/IBIS_Generation/model_file'
os.makedirs ( sub4 , 0755 );
sub5 = path + '/Development/IBIS_Generation/include_file'
os.makedirs ( sub5 , 0755 );
sub6 = path + '/Development/Models/Models_Raw'
os.makedirs ( sub6 , 0755 );
sub7 = path + '/Development/Models/Models_Finetune'
os.makedirs ( sub7 , 0755 );
sub8 = path + '/Development/Models/Models_Validation/Simulation_Log'
os.makedirs ( sub8 , 0755 );
sub9 = path + '/Release/IBIS'
os.makedirs (sub9 , 0755)
sub10 = path + '/Release/DOC'
os.makedirs (sub10 , 0755)

print sub1
print sub2
print sub3
print sub4
print sub5
print sub6
print sub7
print sub8
print sub9
print sub10

print "\nYour Heirarchy is created as above.\n"

print "Please copy the following into 'INPUT_DATABASE' - \n (1) Datasheet; (2) Package; (3) Spec. Doc; (4) PDK info.; (5) Any other pre-requisites IBIS Development information\n"

print "Please copy the following into 'Simulation_Log' - \n (1) Local Cadence IBIS_WORK Library; (2) Cadence Simulation log file of IBIS vs Design\n"

print "Please copy the following into 'DOC' - \n (1) Final IBIS file; (2) Validation Report; (3) IQ_report; (4) Any other information that's uploaded to JIRA as final Release\n"


os.chdir(sub1)
readme_file = "readme.txt"
dummy1 = open (readme_file,"w+")
dummy1.write ("Please copy the following into 'INPUT_DATABASE' - \n (1) Datasheet; (2) Package; (3) Spec. Doc; (4) PDK info.; (5) Any other pre-requisites IBIS Development information\n\nPlease copy the following into 'Simulation_Log' - \n (1) Local Cadence IBIS_WORK Library; (2) Cadence Simulation log file of IBIS vs Design\n\nPlease copy the following into 'DOC' - \n (1) Final IBIS file; (2) Validation Report; (3) IQ_report; (4) Any other information that's uploaded to JIRA as final Release\n")
dummy1.close()

os.chdir(sub2)
dummy2 = open ('dummy2.txt',"w")
dummy2.close()

os.chdir(sub3)
dummy3 = open ('dummy3.txt',"w")
dummy3.close()

os.chdir(sub4)
dummy4 = open ('dummy4.txt',"w")
dummy4.close()

os.chdir(sub5)
dummy5 = open ('dummy5.txt',"w")
dummy5.close()

os.chdir(sub6)
dummy6 = open ('dummy6.txt',"w")
dummy6.close()

os.chdir(sub7)
dummy7 = open ('dummy7.txt',"w")
dummy7.close()

os.chdir(sub8)
dummy8 = open ('dummy8.txt',"w")
dummy8.close()

os.chdir(sub9)
dummy9 = open ('dummy9.txt',"w")
dummy9.close()

os.chdir(sub10)
dummy10 = open ('dummy10.txt',"w")
dummy10.close()

print "Thank You! Have a great time!\n"
readme_out = "gvim" + ' ' + sub1 + '/'+ readme_file
os.system(readme_out)






