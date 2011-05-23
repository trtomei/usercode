#!/bin/bash

echo "Starting..."
echo "Got arguments?"
echo $1
echo $2
echo $3
echo $4
echo "Where are we?"
hostname
echo "Which directory?"
pwd
ARRIVALDIR=$PWD
ls -lh
echo "Go to our directory"
cd /home/OSG/uscms062
echo "Trying to setup CMSSW"
source $OSG_APP/cmssoft/cms/cmsset_default.sh
ls -lh
cd CMSSW_3_9_9_patch1/src
pwd
eval `scramv1 runtime -sh`
echo $CMSSW_BASE
which cmsRun
echo "Go back to our directory"
cd $ARRIVALDIR
cp ./*.py ./CMSSW.py
cmsRun CMSSW.py $1 $2 $3 $4
ls -lh
echo "Normalizing output name"
mv *.root output.root