PYTHIA   = /Users/lukas/heptools/pythia8186
HEPMC    = /Users/lukas/heptools/local
MADGRAPH = /Users/lukas/heptools/madgraph-1.5.10

all: rivetanalysis/plots

madgraphrun/Events/run_01/events.lhe.gz: mg5steering.cmd
	$(MADGRAPH)/bin/mg5 -f mg5steering.cmd
	
madgraphrun/Events/run_01/events.lhe: madgraphrun/Events/run_01/events.lhe.gz
	gunzip -c $< > $@
	
pythiarun/pythiarun: pythiarun/pythiarun.cxx
	c++ -O2 -ansi -pedantic -W -Wall -Wshadow -m64 -Wno-shadow -I$(PYTHIA)/include -I$(HEPMC)/include \
		$< -o $@ \
		-L$(PYTHIA)/lib/archive -lpythia8 -llhapdfdummy -lpythia8tohepmc \
		-L$(HEPMC)/lib -lHepMC

pythiarun/output.hepmc: pythiarun/pythiarun pythiasteering.cmnd madgraphrun/Events/run_01/events.lhe
	PYTHIA8DATA=$(PYTHIA)/xmldoc pythiarun/pythiarun pythiasteering.cmnd pythiarun/output.hepmc

rivetanalysis/RivetStops.so : rivetanalysis/RivetStops.cxx
	rivet-buildplugin $@ $<

rivetanalysis/Rivet.yoda: rivetanalysis/RivetStops.so pythiarun/output.hepmc
	rivet pythiarun/output.hepmc -a StopThreeBody --analysis-path=$(PWD)/rivetanalysis --histo-file=rivetanalysis/Rivet.yoda

rivetanalysis/plots : rivetanalysis/Rivet.yoda
	rivet-mkhtml rivetanalysis/Rivet.yoda -o rivetanalysis/plots

clean:
	rm -rf madgraphrun
	rm -rf pythiarun/pythiarun
	rm -rf pythiarun/output.hepmc
	rm -rf rivetanalysis/Rivet.yoda
	rm -rf rivetanalysis/RivetStops.so
	rm -rf rivetanalysis/plots

.PHONY: clean