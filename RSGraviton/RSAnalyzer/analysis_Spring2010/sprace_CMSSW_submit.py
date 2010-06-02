#! /usr/bin/env python
import os
import random
import sys

# This script helps you to prepare and submit CMSSW
# MC generation jobs to the SPRACE cluster. It submits
# only ONE job per CONDOR cluster.

# Get parameters from command line
if len(sys.argv) < 4:  # the program name and the config file
	# stop the program and print an error message
	sys.exit("Usage: sprace_CMSSW_submit.py <config file> <seq number> <many parameters>")

# Set parameters to the job
###############################################
configargname = sys.argv[1]
tasknumber = str(sys.argv[2])
dryrun = 0
###############################################

if dryrun != 0:
	print "*** DRY RUN *** (change to dryrun = 0 to really run)"
	
# Getting the label
################################################
label = configargname.split("_cfg.py")[0]
taskname = label

# Prepare working directory 
################################################
pwd = os.getcwd()
workingdir = pwd+"/"+taskname+"_dir"
workingdir = workingdir+"_"+tasknumber
if not os.path.exists(workingdir):
	os.mkdir(workingdir)

# Make a nice random seed
################################################
os.system("uuidgen > seedfile")
seedfile = open("seedfile",'r')
myseed = seedfile.readline()
seedfile.close()
os.system("\\rm seedfile")
random.seed(myseed)

# Generate the task.
################################################                                            

# Prepare the input scripts
rundir = workingdir
submitname = rundir+"/"+taskname+".src"
shellname = rundir+"/"+taskname+".sh"
configname = rundir+"/"+taskname+"_cfg.py"

# The submit file
submitfile = open(submitname,'w')
submitfile.write("universe       = vanilla\n")
submitfile.write("executable     = "+shellname+"\n")
submitfile.write("initialdir     = "+rundir+"\n")
submitfile.write("output         = "+rundir+"/STDOUT\n")
submitfile.write("error          = "+rundir+"/STDERR\n")
submitfile.write("log            = "+rundir+"/LOGFILE\n")
submitfile.write("queue\n")
submitfile.close()

# The shell file
shellfile = open(shellname,'w')
shellfile.write("#!/bin/bash\n")
shellfile.write('export OSG_APP=/home/OSG_app/app\n')
shellfile.write('source $OSG_APP/cmssoft/cms/cmsset_default.sh\n')
shellfile.write('cd '+workingdir+'\n')
shellfile.write('eval `scramv1 runtime -sh`\n')
# cmsRun rsanalyzer_cfg.py ptCut=70.0 etaCut=1.2 massCut=20.0 metCut=30.0 fileLabel=QCDStandardCuts print
shellfile.write('cmsRun '+configname+' ptCut='+str(sys.argv[3])+
		' etaCut='+str(sys.argv[4])+
		' massCut='+str(sys.argv[5])+
		' metCut='+str(sys.argv[6])+
		' fileLabel='+str(sys.argv[7])+
		' print\n')
#shellfile.write('myfilename=`cat weAreCreatingTheFile.txt`\n')
#shellfile.write('cp $myfilename '+workingdir+'\n')
shellfile.close()

# Fix random seeds in the Alpgen config file.
oldconfigfile = open(configargname,"r")
newconfigfile = open(configname, "w")
for line in oldconfigfile:
	if line.find("iseed1") >= 0:
		newline = "iseed1 "+str(random.randint(10000,99999))+"\n"
	elif line.find("iseed2") >= 0:
		newline = "iseed2 "+str(random.randint(10000,99999))+"\n"
	elif line.find("iseed3") >= 0:
		newline = "iseed3 "+str(random.randint(10000,99999))+"\n"
	elif line.find("iseed4") >= 0:
		newline = "iseed4 "+str(random.randint(10000,99999))+"\n"
	else:     
		newline = line
	newconfigfile.write(newline)
	continue

# Create and submit the task.
################################################   
if dryrun != 0:
	os.system("echo condor_submit "+submitname)
else:
	os.system("echo condor_submit "+submitname)
	os.system("chmod +x "+shellname)
	os.system("condor_submit "+submitname)
