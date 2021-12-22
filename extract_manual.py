import os
import shutil

####################################################TYP IV DECK ###############################################################
def typ_iv_deck():

    print"\nPlease provide the path for TYP MODEL file\n\n......\n"

    typ_model_path = raw_input(prompt)

    typ_mod_model = "include "  + "\"" + typ_model_path + "\"" + "\n"

    #print typ_mod_model

    
    print"\nPlease provide the path for MAKE file\n\n......\n"
    
    make_file_path_iv_typ = raw_input(prompt)
    
    mod_make_file_iv_typ = "include "  + "\"" + make_file_path_iv_typ + "\"" + "\n"
    
    #print mod_make_file
    
    if not os.path.exists('iv_dir'):
         os.makedirs('iv_dir')
    
    shutil.copy('/design/ibis/work_ibis/users/pawan.sai/max6895_manual/python_scripting_files/universal_iv_wrapper.scs', 'iv_dir/iv_netlist_typ.scs')
    
    f = open("iv_dir/iv_netlist_typ.scs", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(8,mod_netlist)
    contents.insert(10,typ_mod_model)
    contents.insert(12,mod_make_file_iv_typ)
    
    f=open("iv_dir/iv_netlist_typ.scs", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    
    run_iv_typ = command + "spectre " + "iv_dir/iv_netlist_typ.scs &"
    os.system(run_iv_typ)

###################################################### END TYP  IV ######################################################

###################################################### MIN IV DECK ####################################################
def min_iv_deck():

    print"\nPlease provide the path for MIN MODEL file\n\n......\n"

    min_model_path = raw_input(prompt)

    min_mod_model = "include "  + "\"" + min_model_path + "\"" + "\n"

    #print min_mod_model
    
    print"\nPlease provide the path for MAKE file\n\n......\n"
    
    make_file_path_iv_min = raw_input(prompt)
    
    mod_make_file_iv_min = "include "  + "\"" + make_file_path_iv_min + "\"" + "\n"
    
    #print mod_make_file
    
    if not os.path.exists('iv_dir'):
         os.makedirs('iv_dir')
    
    shutil.copy('/design/ibis/work_ibis/users/pawan.sai/max6895_manual/python_scripting_files/universal_iv_wrapper.scs', 'iv_dir/iv_netlist_min.scs')
    
    f = open("iv_dir/iv_netlist_min.scs", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(8,mod_netlist)
    contents.insert(10,min_mod_model)
    contents.insert(12,mod_make_file_iv_min)
    
    f=open("iv_dir/iv_netlist_min.scs", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    
    run_iv_min = command + "spectre " + "iv_dir/iv_netlist_min.scs &"
    os.system(run_iv_min)

###################################################### END MIN IV DECK ################################################

###################################################### MAX IV DECK ####################################################
def max_iv_deck():

    print"\nPlease provide the path for MAX MODEL file\n\n......\n"

    max_model_path = raw_input(prompt)

    max_mod_model = "include "  + "\"" + max_model_path + "\"" + "\n"

    #print max_mod_model
    
    print"\nPlease provide the path for MAKE file\n\n......\n"
    
    make_file_path_iv_max = raw_input(prompt)
    
    mod_make_file_iv_max = "include "  + "\"" + make_file_path_iv_max + "\"" + "\n"
    
    #print mod_make_file_iv_max
    
    if not os.path.exists('iv_dir'):
         os.makedirs('iv_dir')
    
    shutil.copy('/design/ibis/work_ibis/users/pawan.sai/max6895_manual/python_scripting_files/universal_iv_wrapper.scs', 'iv_dir/iv_netlist_max.scs')
    
    f = open("iv_dir/iv_netlist_max.scs", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(8,mod_netlist)
    contents.insert(10,max_mod_model)
    contents.insert(12,mod_make_file_iv_max)
    
    f=open("iv_dir/iv_netlist_max.scs", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    
    run_iv_max = command + "spectre " + "iv_dir/iv_netlist_max.scs &"
    os.system(run_iv_max)

###################################################### END MAX IV DECK ################################################

###################################################### TYP VT DECK ####################################################
def typ_vt_deck():

#    if typ_iv_flag==0:

    print"\nPlease provide the path for TYP MODEL file\n\n......\n"

    typ_model_path = raw_input(prompt)

    typ_mod_model = "include "  + "\"" + typ_model_path + "\"" + "\n"

    #print typ_mod_model

    
    print"\nPlease provide the path for MAKE file\n\n......\n"
    
    make_file_path_vt_typ = raw_input(prompt)
    
    mod_make_file_vt_typ = "include "  + "\"" + make_file_path_vt_typ + "\"" + "\n"
    
    #print mod_make_file
    
    if not os.path.exists('vt_dir'):
         os.makedirs('vt_dir')
    
    shutil.copy('/design/ibis/work_ibis/users/pawan.sai/max6895_manual/python_scripting_files/universal_vt_wrapper.scs', 'vt_dir/vt_netlist_typ.scs')
    
    f = open("vt_dir/vt_netlist_typ.scs", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(8,mod_netlist)
    contents.insert(10,typ_mod_model)
    contents.insert(12,mod_make_file_vt_typ)
    
    f=open("vt_dir/vt_netlist_typ.scs", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    
    run_vt_typ = command + "spectre " + "vt_dir/vt_netlist_typ.scs &"
    os.system(run_vt_typ)

###################################################### END TYP VT DECK ################################################

###################################################### MIN VT DECK ####################################################
def min_vt_deck():

#    if min_iv_flag==0:

    print"\nPlease provide the path for MIN MODEL file\n\n......\n"

    min_model_path = raw_input(prompt)

    min_mod_model = "include "  + "\"" + min_model_path + "\"" + "\n"

    #print min_mod_model


    print"\nPlease provide the path for MAKE file\n\n......\n"
    
    make_file_path_vt_min = raw_input(prompt)
    
    mod_make_file_vt_min = "include "  + "\"" + make_file_path_vt_min + "\"" + "\n"
    
    #print mod_make_file
    
    if not os.path.exists('vt_dir'):
         os.makedirs('vt_dir')
    
    shutil.copy('/design/ibis/work_ibis/users/pawan.sai/max6895_manual/python_scripting_files/universal_vt_wrapper.scs', 'vt_dir/vt_netlist_min.scs')
    
    f = open("vt_dir/vt_netlist_min.scs", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(8,mod_netlist)
    contents.insert(10,min_mod_model)
    contents.insert(12,mod_make_file_vt_min)
    
    f=open("vt_dir/vt_netlist_min.scs", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    
    run_vt_min = command + "spectre " + "vt_dir/vt_netlist_min.scs &"
    os.system(run_vt_min)

###################################################### END MIN VT DECK ################################################

###################################################### MAX VT DECK ####################################################
def max_vt_deck():

#    if max_iv_flag==0:

    print"\nPlease provide the path for MAX MODEL file\n\n......\n"

    max_model_path = raw_input(prompt)

    max_mod_model = "include "  + "\"" + max_model_path + "\"" + "\n"

    #print max_mod_model

    print"\nPlease provide the path for MAKE file\n\n......\n"
    
    make_file_path_vt_max = raw_input(prompt)
    
    mod_make_file_vt_max = "include "  + "\"" + make_file_path_vt_max + "\"" + "\n"
    
    #print mod_make_file_vt_max
    
    if not os.path.exists('vt_dir'):
         os.makedirs('vt_dir')
    
    shutil.copy('/design/ibis/work_ibis/users/pawan.sai/max6895_manual/python_scripting_files/universal_vt_wrapper.scs', 'vt_dir/vt_netlist_max.scs')
    
    f = open("vt_dir/vt_netlist_max.scs", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(8,mod_netlist)
    contents.insert(10,max_mod_model)
    contents.insert(12,mod_make_file_vt_max)
    
    f=open("vt_dir/vt_netlist_max.scs", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    
    run_vt_max = command + "spectre " + "vt_dir/vt_netlist_max.scs  &"
    os.system(run_vt_max)


###################################################### END MAX VT DECK ################################################


###################################################### MAIN ###########################################################
command = "xterm -hold -e "

print "\n\nHello! Wishing you a Good day!\n\nLet's begin the Manual Extraction Process\n\nPlease provide the path for the netlist\n\n......\n"

prompt ='>  '

netlist_path  = raw_input(prompt)

#print netlist_path

mod_netlist = "include "  + "\"" + netlist_path + "\"" + "\n"

#print mod_netlist

#print"\nPlease provide the path for TYP MODEL file\n\n......\n"

#model_path = raw_input(prompt)

#mod_model = "include "  + "\"" + model_path + "\"" + "\n"

#print mod_model


############################################### TYP ####################################
print "\n\nDo you want to prepare netlists for IV-TYP corner?\nPlease enter just alphabet \"y\" or \"n\"\n......"
typ_iv_corner_reply =  raw_input(prompt)

if typ_iv_corner_reply == "y":
    typ_iv_flag=1
    typ_iv_deck()
else:
    typ_iv_flag=0

print "\n\nDo you want to prepare netlists for VT-TYP corner?\nPlease enter just alphabet \"y\" or \"n\"\n......"
typ_vt_corner_reply =  raw_input(prompt)

if typ_vt_corner_reply == "y":
    typ_vt_flag=1
    typ_vt_deck()
else:
    typ_vt_flag=0
############################################### END TYP ################################

############################################## MIN #####################################

print "\n\nDo you want to prepare netlists for IV-MIN corner?\nPlease enter just alphabet \"y\" or \"n\"\n......"
min_iv_corner_reply =  raw_input(prompt)

if min_iv_corner_reply == "y":
    min_iv_flag=1
    min_iv_deck()
else:
    min_iv_flag=0

print "\n\nDo you want to prepare netlists for VT-MIN corner?\nPlease enter just alphabet \"y\" or \"n\"\n......"
min_vt_corner_reply =  raw_input(prompt)

if min_vt_corner_reply == "y":
    min_vt_flag=1
    min_vt_deck()
else:
    min_vt_flag=0

############################################# END MIN ##################################

############################################# MAX ######################################


print "\n\nDo you want to prepare netlists for IV_MAX corner?\nPlease enter just alphabet \"y\" or \"n\"\n......"
max_iv_corner_reply =  raw_input(prompt)

if max_iv_corner_reply == "y":
    max_iv_flag=1
    max_iv_deck()
else:
    max_iv_flag=0

print "\n\nDo you want to prepare netlists for VT-MAX corner?\nPlease enter just alphabet \"y\" or \"n\"\n......"
max_vt_corner_reply =  raw_input(prompt)

if max_vt_corner_reply == "y":
    max_vt_flag=1
    max_vt_deck()
else:
    max_vt_flag=0

########################################### END MAX ####################################

#print typ_iv_flag
#print typ_vt_flag
#print min_iv_flag
#print min_vt_flag
#print max_iv_flag
#print max_vt_flag

print "\n Thank you! Have a nice day! \n"





