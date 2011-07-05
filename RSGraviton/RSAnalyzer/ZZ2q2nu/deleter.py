import sys
import os

fileName = sys.argv[1]
deletionLine = sys.argv[2]

f= open(fileName)
smallFileList = list()

for line in f:
    if line.find('root') != -1:
#        print line
        tokens = line.split('/')
        smallFileList.append(tokens[len(tokens)-1])

for i in smallFileList:
    delCommand = 'srmrm '+deletionLine+'/'+i 
    os.system(delCommand)
