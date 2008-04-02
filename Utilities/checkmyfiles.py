import os
import sys
import string

prefix = sys.argv[1]

file = open("raw.list")
while(1):
    filename = file.readline()
    if not filename:
        break
    fullname = prefix+filename
    fullcommand = "stager_qry -M "+fullname
    os.system(fullcommand)
    continue
