from AthenaCommon.AppMgr import ServiceMgr
import AthenaPoolCnvSvc.ReadAthenaPool
ServiceMgr.EventSelector.InputCollections = ["evgen.pool.root"]

from AthenaCommon.AlgSequence import AlgSequence
job = AlgSequence()

from McParticleTools.McParticleToolsConf import HepMcWriterTool
from McParticleAlgs.McParticleAlgsConf   import GenEventAsciiWriter
McWriter = HepMcWriterTool(McEvents="GEN_EVENT", Output="events.hepmc")
job += GenEventAsciiWriter(McWriter=McWriter, OutputLevel=INFO)

theApp.EvtMax = 10
