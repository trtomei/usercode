#! /usr/bin/env python
import os
import random
import sys

# This script helps you to prepare and submit CMSSW
# ALPGEN matching jobs to the SPRACE cluster. It submits
# only ONE job per CONDOR cluster.

# Get parameters from command line
if len(sys.argv) != 2:  # the program name and the taskname
	# stop the program and print an error message
	sys.exit("Usage: sprace_CMSSW_alpgmatch.py <inputfilename>")

# Set parameters to the job
###############################################
tmpstr1 = ((sys.argv[1]).split("_cfg"))[0]
tmpstr2 = tmpstr1+"_dir"
taskname = tmpstr1
print taskname
inputfilename = sys.argv[1]
dryrun = 0
###############################################

if dryrun != 0:
	print "*** DRY RUN ***"

# Prepare working directory 
################################################
pwd = os.getcwd()
workingdir = pwd+"/"+taskname
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

# Prepare the job
################################################                                            

# Prepare the input scripts
rundir = workingdir
submitname = rundir+"/"+taskname+".src"
shellname = rundir+"/"+taskname+".sh"
CMSSWconfigname = rundir+"/CMSSW_"+taskname+"_cfg.py"
CMSSWskeletonname = inputfilename

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
shellfile.write("source /home/OSG_app/app/cmssoft/cms/cmsset_default.sh\n")
shellfile.write("cd "+rundir+"\n")
shellfile.write("eval `scramv1 runtime -sh`\n")
shellfile.write("cmsRun "+CMSSWconfigname+"\n")
shellfile.close()

# The CMSSW config file
CMSSWskeleton = open(CMSSWskeletonname,'r')
CMSSWconfig = open(CMSSWconfigname,'w')
	
for line in CMSSWskeleton:
	if line.find("$CONDORSEED")!=-1:
		newline = line.replace("$CONDORSEED",str(random.randint(100000,999999)))
		CMSSWconfig.write(newline)
	elif line.find("$CONDORINPUT")!=-1:
		newline = line.replace("$CONDORINPUT",'"'+taskname+'"')
		CMSSWconfig.write(newline)
	elif line.find("$CONDOROUTPUT")!=-1:
		newline = line.replace("$CONDOROUTPUT",'"'+taskname+'"')
		CMSSWconfig.write(newline)
	else:
		CMSSWconfig.write(line)
	continue

CMSSWconfig.close()
CMSSWskeleton.close()

if dryrun != 0:
	os.system("echo condor_submit "+submitname)
else:
	os.system("echo condor_submit "+submitname)
	os.system("chmod +x "+shellname)
	os.system("condor_submit "+submitname)
	
