import FWCore.ParameterSet.Config as cms

myParameters = cms.vstring('PMAS(5,1)=4.8 ! b quark mass', 
    'PMAS(6,1)=172.3 ! t quark mass', 
    'PMAS(347,1)= 500.0 ! graviton mass', 
    'MSEL=0         ! User defined processes', 
    'MSUB(391)=1    ! ffbar->G*', 
    'MSUB(392)=1    ! gg->G*', 
    'MDME(4158,1)=0 ! graviton decay into d dbar', 
    'MDME(4159,1)=0 ! graviton decay into u ubar', 
    'MDME(4160,1)=0 ! graviton decay into s sbar', 
    'MDME(4161,1)=0 ! graviton decay into c cbar', 
    'MDME(4162,1)=0 ! graviton decay into b bbar', 
    'MDME(4163,1)=0 ! graviton decay into t tbar', 
    'MDME(4166,1)=0 ! graviton decay into e+ e-', 
    'MDME(4167,1)=0 ! graviton decay into nu_e nu_ebar', 
    'MDME(4168,1)=0 ! graviton decay into mu+ mu-', 
    'MDME(4169,1)=0 ! graviton decay into nu_mu nu_mubar', 
    'MDME(4170,1)=0 ! graviton decay into tau+ tau-', 
    'MDME(4171,1)=0 ! graviton decay into nu_tau nu_taubar', 
    'MDME(4174,1)=0 ! graviton decay into g', 
    'MDME(4175,1)=0 ! graviton decay into gamma', 
    'MDME(4176,1)=1 ! graviton decay into Z0', 
    'MDME(4177,1)=0 ! graviton decay into W+ W-', 
    'MDME(174,1)=4  !Z decay into d dbar', 
    'MDME(175,1)=4  !Z decay into u ubar', 
    'MDME(176,1)=4  !Z decay into s sbar', 
    'MDME(177,1)=4  !Z decay into c cbar', 
    'MDME(178,1)=4  !Z decay into b bbar', 
    'MDME(179,1)=4  !Z decay into t tbar', 
    'MDME(182,1)=0  !Z decay into e- e+', 
    'MDME(183,1)=5  !Z decay into nu_e nu_ebar', 
    'MDME(184,1)=0  !Z decay into mu- mu+', 
    'MDME(185,1)=5  !Z decay into nu_mu nu_mubar', 
    'MDME(186,1)=0  !Z decay into tau- tau+', 
    'MDME(187,1)=5  !Z decay into nu_tau nu_taubar', 
    'PARP(50)=0.54  ! related to the mass of the graviton - study this!', 
    'CKIN(3)=25.    ! Pt hat lower cut', 
    'CKIN(4)=-1.    ! Pt hat upper cut', 
    'CKIN(13)=-10.  ! etamin', 
    'CKIN(14)=10.   ! etamax', 
    'CKIN(15)=-10.  ! -etamax', 
    'CKIN(16)=10.   ! -etamin')

