import sys

options = sys.argv
numJobs = 21
eventsPerJob = 50000
configFile = "patTuple_PF2PAT_cfg_with110GeVCut.py"

if "numJobs" in options:
    numJobs = int(options[options.index("numJobs")+1])
if "eventsPerJob" in options:
    eventsPerJob = int(options[options.index("eventsPerJob")+1])
if "configFile" in options:
    configFile = options[options.index("configFile")+1]
    
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
    line1 = "arguments            = skipEvents "+eventsToSkip+" numEvents "+str(eventsPerJob)+" useData True"
    line2 = "initialdir           = /home/trtomei/hdacs/CMSSW_4_2_3_patch2/src/RSGraviton/RSAnalyzer/ZZ2q2nu/condor_dataPattuples_2011May10ReReco_triggerStudies_"+str(i)
    line3 = "queue"
    print line1
    print line2
    print line3

