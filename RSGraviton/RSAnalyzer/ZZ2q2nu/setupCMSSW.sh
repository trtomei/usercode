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
source $OSG_APP/cmssoft/cms/cmsset_default.sh
ls -lh
rm -rf CMSSW_*
scramv1 project CMSSW $1
cd $1/src
eval `scramv1 runtime -sh`
echo $CMSSW_BASE
which cmsRun
echo "Go back to our directory"
cp $ARRIVALDIR/RSGraviton.tar.gz .
tar -xzvf RSGraviton.tar.gz
ls -lh
cd RSGraviton/RSAnalyzer
scram b
