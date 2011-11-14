### Generic file to submit jobs to SPRACE cluster.
import sys
import os
import shutil

options = sys.argv
numJobs = 15
eventsPerJob = 10000
configFile = "patTuple_PF2PAT_cfg_with110GeVCut.py"
dirName = "condor_dataPattuples_Run2011A_ReRecoAug05"
currentDirectory = os.getcwd()
useData = "False"

if "numJobs" in options:
    numJobs = int(options[options.index("numJobs")+1])
if "eventsPerJob" in options:
    eventsPerJob = int(options[options.index("eventsPerJob")+1])
if "configFile" in options:
    configFile = options[options.index("configFile")+1]
if "dirName" in options:
    dirName = options[options.index("dirName")+1]
if "currentDirectory" in options:
    currentDirectory = options[options.index("currentDirectory")+1]
if "useData " in options:
    useData = options[options.index("useData")+1]

boilerplate = ["executable           = script.sh",
               "transfer_executable  = true",
               "universe             = grid",
               "grid_resource        = gt2 osg-ce.sprace.org.br/jobmanager-condor",
               "log                  = resultado.log",
               "output               = resultado.out",
               "error                = resultado.error",
               "should_transfer_files   = YES",
               "transfer_output_files = output.root",
               "transfer_input_files = "+configFile,
               "when_to_transfer_output = ON_EXIT",
               ]

for i in boilerplate:
    print i
    
for i in range(0,numJobs):
    eventsToSkip = str(eventsPerJob*i)
    eventsToRun = eventsPerJob
    line1 = "arguments            = skipEvents "+eventsToSkip+" numEvents "+str(eventsPerJob)+" useData "+useData
    line2 = "initialdir           = "+currentDirectory+dirName+"_"+str(i)
    line3 = "queue"
    os.mkdir(dirName+"_"+str(i))
    shutil.copy(configFile,dirName+"_"+str(i))
    print line1
    print line2
    print line3
