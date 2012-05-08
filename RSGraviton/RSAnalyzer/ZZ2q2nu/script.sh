#!/bin/bash

echo "Starting..."
echo "Got arguments?"
echo $1
echo $2
echo $3
echo $4
echo $5
echo $6
echo "Where are we?"
hostname
echo "Which directory?"
pwd
ARRIVALDIR=$PWD
ls -lh
echo "Go to our directory"
cd /home/OSG/uscms062
echo "Trying to setup CMSSW"
export SCRAM_ARCH=slc5_amd64_gcc434
source $OSG_APP/cmssoft/cms/cmsset_default.sh
ls -lh
cd CMSSW_4_2_8_patch6/src
pwd
eval `scramv1 runtime -sh`
echo $CMSSW_BASE
which cmsRun
echo "Go back to our directory"
cd $ARRIVALDIR
cp ./*.py ./localCMSSW.py
cmsRun localCMSSW.py $1 $2 $3 $4 $5 $6
ls -lh
echo "Normalizing output name"
mv *.root output.root