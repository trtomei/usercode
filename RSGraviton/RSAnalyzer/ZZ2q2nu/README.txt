To run the analysis:

cmsRun rsanalyzer_JetMET_PATsignalAndControlTogether_cfg.py input $DATASETNAME

$DATASETNAME can be one of the following:

%%%%%%%%%%%%%%
QCD2j_120to280
QCD2j_280to500
QCD2j_40to120
QCD2j_500to5000
QCD3j_120to280
QCD3j_280to500
QCD3j_40to120
QCD3j_500to5000
QCD4j_120to280
QCD4j_280to500
QCD4j_40to120
QCD4j_500to5000
QCD5j_120to280
QCD5j_280to500
QCD5j_40to120
QCD5j_500to5000
QCD6j_120to280
QCD6j_280to500
QCD6j_40to120
QCD6j_500to5000

RSToZZToNuNuJJ_m1000
RSToZZToNuNuJJ_m1250
RSToZZToNuNuJJ_m750

TTbar0Jets
TTbar1Jets
TTbar2Jets
TTbar3Jets
TTbar4Jets

W0j
W1j_0to100
W1j_100to300
W1j_300to800
W2j_0to100
W2j_100to300
W2j_300to800
W3j_0to100
W3j_100to300
W3j_300to800
W4j_0to100
W4j_100to300
W4j_300to800
W5j_0to100
W5j_100to300
W5j_300to800

ZinvisibleJets
%%%%%%%%%%%%%%

It would be advisable to use CONDOR to run over those datasets, since it can take a fair amount of time.
To run CMSSW in SPRACE with CONDOR, you should bootstrap a CMSSW area in your personal directory
(check setupCMSSW.sh and setupCMSSW.submit for that), and then set it up ("cmsenv") prior to running
(check script.sh for that).

To merge the resulting output files: use the following commands:
(but DON'T copy and paste these commands mindlessly - you have to change the paths to the files you want to merge.
If you run the standard submit files, the commands below are ok.

%%%%%%%%%%%%%%
QCD 

mergeTFileServiceHistograms -w 1.06E+003,5.20E+000,6.41E-002,3.00E-003,3.33E+002,9.29E+000,2.15E-001,8.53E-003,5.07E+001,5.91E+000,1.60E-001,6.90E-003,1.66E+001,3.97E+000,1.08E-001,7.02E-003 -o output_QCD.root -i QCD2j_040to120/output.root QCD2j_120to280/output.root QCD2j_280to500/output.root QCD2j_500to5000/output.root QCD3j_040to120/output.root QCD3j_120to280/output.root QCD3j_280to500/output.root QCD3j_500to5000/output.root QCD4j_040to120/output.root QCD4j_120to280/output.root QCD4j_280to500/output.root QCD4j_500to5000/output.root QCD5j_040to120/output.root QCD5j_120to280/output.root QCD5j_280to500/output.root QCD5j_500to5000/output.root

Wjets

mergeTFileServiceHistograms -w 1.95E-001,1.25E-001,4.67E-002,8.94E-003,8.58E-003,7.61E-003,2.64E-003,2.27E-003,3.23E-003,4.28E-003,1.97E-003,2.01E-005,3.64E-005,1.08E-004,3.20E-004,1.90E-004 -o output_Wjets.root -i W0j/output.root W1j_0to100/output.root W2j_0to100/output.root W3j_0to100/output.root W4j_0to100/output.root W5j_0to100/output.root W1j_100to300/output.root W2j_100to300/output.root W3j_100to300/output.root W4j_100to300/output.root W5j_100to300/output.root W1j_300to800/output.root W2j_300to800/output.root W3j_300to800/output.root W4j_300to800/output.root W5j_300to800/output.root

ttbar

mergeTFileServiceHistograms -w 1.11E-003,4.42E-004,3.52E-004,6.09E-004,1.98E-004 -o output_ttbar.root -i TTbar0Jets/output.root TTbar1Jets/output.root TTbar2Jets/output.root TTbar3Jets/output.root TTbar4Jets/output.root

Zinvisible

mergeTFileServiceHistograms -w 6.81E-002 -o output_Zinvisible.root -i ZinvisibleJets/output.root
