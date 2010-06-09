import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0078/422336C5-FE4B-DF11-8F3A-003048635C78.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/FEE6205A-6F4A-DF11-9D2F-00E08179180D.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/FA55E079-704A-DF11-B1F3-00E08178C0FF.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/B636C147-6B4A-DF11-99D7-002481E150FE.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/B002D0EF-704A-DF11-9D37-0015170AE3B0.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/9EF8AFCB-714A-DF11-8E83-00E08177F39D.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/9C231E0F-6F4A-DF11-B7FF-00E08178C0FF.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/929053EF-694A-DF11-9D17-0025B3E05D68.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/90E27EB3-6B4A-DF11-89EF-0025B3E06466.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/86F9A2B5-6F4A-DF11-8FC1-00E08178C0BF.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/7A8B340A-6D4A-DF11-A97E-00E08178C12F.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/764E887B-704A-DF11-8659-00E08178C129.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/761429E7-6B4A-DF11-A9F4-003048670BAA.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/14FC954B-6F4A-DF11-8618-0015170AE484.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0063/144D063C-6D4A-DF11-8FA5-003048673EFE.root',
       '/store/mc/Spring10/QCD5Jets_Pt500to5000-alpgen/GEN-SIM-RECO/START3X_V26_S09-v1/0062/5AB56F7F-674A-DF11-8848-002481E15270.root' ] );


secFiles.extend( [
               ] )

