import os

x = raw_input("\nWhat is the extension you are looking for?\n")

command = "perl -le \'use File::Find; find(sub{-f && $_ =~ /."+x+"$/ && print $File::Find::name},\".\")\'"

os.system(command)

