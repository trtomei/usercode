#####################################
# CMSSW configuration file - Python #
#####################################

import FWCore.ParameterSet.Config as cms
import datetime

process = cms.Process("USER")

###########################
# Basic process controls. #
###########################
today = str(datetime.date.today())
fileLabel = ''

# Source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/tomei/skim1/skim_45.root',
    '/store/user/tomei/skim1/skim_4.root',
    '/store/user/tomei/skim1/skim_36.root',
    '/store/user/tomei/skim1/skim_10.root',
    '/store/user/tomei/skim1/skim_27.root',
    '/store/user/tomei/skim1/skim_18.root',
    '/store/user/tomei/skim1/skim_55.root',
    '/store/user/tomei/skim1/skim_5.root',
    '/store/user/tomei/skim1/skim_46.root',
    '/store/user/tomei/skim1/skim_20.root',
    '/store/user/tomei/skim1/skim_11.root',
    '/store/user/tomei/skim1/skim_37.root',
    '/store/user/tomei/skim1/skim_28.root',
    '/store/user/tomei/skim1/skim_19.root',
    '/store/user/tomei/skim1/skim_6.root',
    '/store/user/tomei/skim1/skim_30.root',
    '/store/user/tomei/skim1/skim_56.root',
    '/store/user/tomei/skim1/skim_47.root',
    '/store/user/tomei/skim1/skim_21.root',
    '/store/user/tomei/skim1/skim_12.root',
    '/store/user/tomei/skim1/skim_38.root',
    '/store/user/tomei/skim1/skim_29.root',
    '/store/user/tomei/skim1/skim_7.root',
    '/store/user/tomei/skim1/skim_40.root',
    '/store/user/tomei/skim1/skim_31.root',
    '/store/user/tomei/skim1/skim_22.root',
    '/store/user/tomei/skim1/skim_48.root',
    '/store/user/tomei/skim1/skim_13.root',
    '/store/user/tomei/skim1/skim_39.root',
    '/store/user/tomei/skim1/skim_8.root',
    '/store/user/tomei/skim1/skim_50.root',
    '/store/user/tomei/skim1/skim_41.root',
    '/store/user/tomei/skim1/skim_32.root',
    '/store/user/tomei/skim1/skim_9.root',
    '/store/user/tomei/skim1/skim_49.root',
    '/store/user/tomei/skim1/skim_23.root',
    '/store/user/tomei/skim1/skim_14.root',
    '/store/user/tomei/skim1/skim_51.root',
    '/store/user/tomei/skim1/skim_42.root',
    '/store/user/tomei/skim1/skim_33.root',
    '/store/user/tomei/skim1/skim_24.root',
    '/store/user/tomei/skim1/skim_15.root',
    '/store/user/tomei/skim1/skim_52.root',
    '/store/user/tomei/skim1/skim_1.root',
    '/store/user/tomei/skim1/skim_43.root',
    '/store/user/tomei/skim1/skim_34.root',
    '/store/user/tomei/skim1/skim_25.root',
    '/store/user/tomei/skim1/skim_2.root',
    '/store/user/tomei/skim1/skim_16.root',
    '/store/user/tomei/skim1/skim_53.root',
    '/store/user/tomei/skim1/skim_44.root',
    '/store/user/tomei/skim1/skim_35.root',
    '/store/user/tomei/skim1/skim_3.root',
    '/store/user/tomei/skim1/skim_26.root',
    '/store/user/tomei/skim1/skim_17.root',
    '/store/user/tomei/skim1/skim_54.root'
    )
                            )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

##################
# Basic services #
##################

process.MessageLogger = cms.Service("MessageLogger")

#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string('results_'+fileLabel+today+'.root')
#)

#process.Tracer = cms.Service("Tracer")

process.OUT = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('herwig80_skim.root'),
                               outputCommands = cms.untracked.vstring('keep *')
                               )

#########
# Paths #
#########

process.e1 = cms.EndPath(process.OUT)
