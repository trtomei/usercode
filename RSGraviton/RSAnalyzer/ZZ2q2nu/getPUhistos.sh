#!/bin/bash

CERN=lxplus.cern.ch
LOCATION=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp

# For the PU_S4 samples: If you are not worried about out-of-time pileup,
# use the "spike-at-zero-smeared distribution", above, as the MC input, 
# in-time weighting only. Use the correct observed luminosity distribution 
# for the data. ( Note that this is a change from the previous recommendation. ) 
# OR, if you want a "full" reweighting, use the 3D reweighting described below. 
# This requires the true "Flat10+Tail" MC input, and the true distributions 
# from the data. To avoid small biases introduced by sampling from an 
# integer-based distribution for the data histograms, one should use the 
# "pileupTruth_v2_finebin.root" series of inputs from the /afs pileup area. 

# Data distributions
scp tomei@${CERN}:"${LOCATION}/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.pileupTruth_v2_finebin.root \
${LOCATION}/Cert_165088-167913_7TeV_PromptReco_JSON.pileupTruth_v2_finebin.root \
${LOCATION}/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v2.pileupTruth_v2_finebin.root \
${LOCATION}/Cert_172620-173692_PromptReco_JSON.pileupTruth_v2_finebin.root \
${LOCATION}/Cert_175832-177515_PromptReco_JSON.pileupTruth_v2_finebin.root \
${LOCATION}/Cert_177718_178078_7TeV_PromptReco_Collisons11_JSON.pileupTruth_v2_finebin.root \
${LOCATION}/Cert_178098-180252_7TeV_PromptReco_Collisions11_JSON.pileupTruth_v2_finebin.root" .

rm PUData_dist.root
hadd PUData_dist.root Cert_*pileupTruth_v2_finebin.root

# MC distributions
root -b -l -q -x makePUhistMC.C+

ls -lh PU*_dist.root
