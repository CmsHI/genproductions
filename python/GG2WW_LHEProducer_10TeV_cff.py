import FWCore.ParameterSet.Config as cms
from Configuration.GenProduction.PythiaUESettings_cfi import *

source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring('file:LHEtoEDM.root'),
                    skipEvents = cms.untracked.uint32(0)
                    )

generator = cms.EDProducer("LHEProducer",
                           hadronisation = cms.PSet(pythiaUESettingsBlock,
                                                    generator = cms.string('Pythia6'),
                                                    parameterSets = cms.vstring('pythiaUESettings',
                                                                                'pythiaCMSDefaults'
                                                                                ),
                                                    pythiaCMSDefaults = cms.vstring('PMAS(5,1)=4.4    ! b quarks mass', 
                                                                                    'PMAS(6,1)=172.4  ! t quarks mass', 
                                                                                    'MSTJ(1)=1        !...Fragmentation/hadronization on or off', 
                                                                                    'MSTP(61)=1       ! Parton showering on or off', 
                                                                                    'MSEL=0           ! User defined processes/Full user control'
                                                                                    )
                                                    )
                           )


ProducerSourceSequence = cms.Sequence(generator)

configurationMetadata = cms.untracked.PSet(version = cms.untracked.string('$Revision: 1.1 $'),
                                           name = cms.untracked.string('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/GG2WW_LHEProducer_10TeV_cff.py,v $'),
                                           annotation = cms.untracked.string('GG2WW process at 10 TeV')
                                           )

