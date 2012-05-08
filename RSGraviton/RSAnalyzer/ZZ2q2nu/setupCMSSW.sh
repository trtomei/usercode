#!/bin/bash

echo "Starting..."
echo "Got arguments?"
echo $1
echo "Where are we?"
hostname
echo "Which directory?"
pwd
ARRIVALDIR=$PWD
ls -lh
echo "Go to our directory"
# Here we have to go to our particular directory. It depends on who you are and
# to which username you're mapped.
cd /home/OSG/uscms062
echo "Trying to setup CMSSW"
export SCRAM_ARCH=slc5_amd64_gcc434
source $OSG_APP/cmssoft/cms/cmsset_default.sh
rm gram_job_mgr_*.log
ls -lh
#rm -rf CMSSW_4*
#rm -rf $1
#scramv1 project CMSSW $1
### Choose our destination.
#cd $1/src
#cd $1/src/RSGraviton/RSAnalyzer
cd $1/src/RSGraviton/RSAnalyzer/python
eval `scramv1 runtime -sh`
echo $CMSSW_BASE
which cmsRun
echo "Get our payload here"
### Choose payload
#cp $ARRIVALDIR/RecoMET.tar.gz .
#cp $ARRIVALDIR/tarredRSGraviton.tar.gz .
cp $ARRIVALDIR/Summer11.tar.gz . 
#cp $ARRIVALDIR/physicsToolspatAlgos.tar.gz .
#tar -xzvf RecoMET.tar.gz
#tar -xzvf tarredRSGraviton.tar.gz
tar -xzvf Summer11.tar.gz
#tar -xzvf physicsToolspatAlgos.tar.gz
ls -lh
#cd RecoMET
#cd PhysicsTools/PatAlgos
scram b
