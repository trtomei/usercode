import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles, duplicateCheckMode=cms.untracked.string("checkEachFile"))
readFiles.extend( [
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_079fc9c385e7449481fdf97b5121e040.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_07a1a01eaf8e4ebb80cea66e6ce6710e.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_088980503a7440e9acf0a44ddd223924.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_0ab202103ebf4183abe143e411308c7f.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_0ec714afefcb459db67523b31dbcf4f8.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_0f280068991d41cc81b67c124f2ded66.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_15624c2bbfd942f6b45a4db6d4935242.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_1727bc8b9d6d445b8d206be70eb2f217.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_258ed908eace4ba3a7849360e0c415c2.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_26149163ee4349fb9df685ff68763e30.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_261b3546ac054ca18ff0b2e2799ecbab.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_3eb9f4fb980c465fb2f1739479684a33.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_49a7c9368d654820a15f7d8472bc5ace.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_4c8ec1b2a8af4103bfeca9ce747da5f0.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_53959098055d4fe19bad5344d0889a36.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_55c318439e3a40b98ec056530487665d.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_5813a5d13cd34f5696e5d5c61116eb5b.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_59e0c8fbd7854a06bd2a42e906fd1c6b.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_63facfceacd94ca39862db0b62244a3c.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_641d842a1b264eac9ae3c659a8e437f0.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_6cb77ad529134acfaa4d1f85a58a6781.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_6cd42fc4118e4a9f9212b4868d02f437.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_6dc8ee6568f240f0b67074239974d5d3.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_6f5a4040490f465aa1b86c51741ef8f9.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_73311efabec5466dbe98be53b5173ebc.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_7dc575a052044433b45befb1d24bb5a2.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_82193c1844124b88a64065d72d6caf86.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_8865c80ed3ee497b9e629029392b4786.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_9168617d91904709a243b57985037987.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_92f21f07e03a4a089afa756da34c35c3.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_9454dbce38ba4ff1ba73e469d145f133.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_95c34a655514464b9b9ad7753e120ef5.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_95c954a07afc4f47a433afa43c08fe07.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_9f7100bd2f8e44adb4b3c995c79c216a.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_a1dffd776180411ab4ec580080dd6145.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_a649d85e97ba4840aa23790926dc5061.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_a72ecc2823214bccaf332b83cde1b475.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_aa1d3d78b6a14bd5adc40c117d61ef4b.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_abb58b4e0b2c4365970c8e28b6548cae.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_b04896731bc041beab0c9672b61196a8.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_b0a081c992174fab8b2125d3748aad2b.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_b2dc16ae477e4f13890ade07a7a03d34.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_bcf87370523949e496504c4ca6143013.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_bddc029a3da646958e62589ead16ffae.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_bdf7e86a9a8f4a14a7f151381f33cec0.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_c5a1c9b4fae54b42aaac29233adadb16.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_c5a76d796c3e497387796d6614dcfb13.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_c5e4b640f3e440ad8f3e6dba7ddef3be.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_c96bd3e3786e4748a45f4296d416af36.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_da623690eaac48de9d5f5ff6e8b2c188.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_db2c2ec538584f659ec127c38c0a3c75.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_dbeb4860ee5446a0b18e34365f824175.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_e1d9a6e1fc6b4f3299a570f0c32af32d.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_e3a44aa33f8e4cbfbd315af36e37970b.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_ea921e4139a2475b98ed58b5a85b32ea.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_f4aa7465e4b94ba2918fd48b5538d610.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_f4ae2a7716e44e3a9d1486b6323c0ee1.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_f9a302c0d9cc44168e70af4598e0072e.root',
'file:/storage/trtomei/data/FASTSIM/RSZZ_mass800coupling005/Pythia_Zjjnunu_fbb4bbf3534f40d6a6778dc043d12f16.root'
 ] );
secFiles.extend( [
               ] )
