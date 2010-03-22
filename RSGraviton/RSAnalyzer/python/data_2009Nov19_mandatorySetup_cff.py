###
# Mandatory setup for 2009 data.
import FWCore.ParameterSet.Config as cms

# Good runs
lumisToProcess = cms.untracked.VLuminosityBlockRange('123596:2-123596:9999',
                                                     '123591:71-123591:9999',
                                                     '123592:2-123592:12',
                                                     '123615:70-123615:9999',
                                                     '123732:56-123732:9999',
                                                     '123815:7-123815:9999',
                                                     '123818:2-123818:42',
                                                     '123908:2-123908:13',
                                                     '123977:1-123977:9999',
                                                     '123976:1-123976:9999',
                                                     '123978:1-123978:9999',
                                                     '123985:1-123985:9999',
                                                     '123987:1-123987:9999',
                                                     '124008:1-124008:1',
                                                     '124009:1-124009:68',
                                                     '124022:66-124022:179',
                                                     '124023:38-124023:96',
                                                     '124020:12-124020:94',
                                                     '124024:2-124024:83',
                                                     '124025:3-124025:13',
                                                     '124027:24-124027:9999',
                                                     '124030:1-124030:9999',
                                                     '124120:1-124120:9999',
                                                     '124275:3-124275:30')
