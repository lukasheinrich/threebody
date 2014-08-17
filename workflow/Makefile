PYTHIA   = /Users/lukas/heptools/local
HEPMC    = /Users/lukas/heptools/local
MADGRAPH = /Users/lukas/heptools/madgraph-1.5.10
#MADGRAPH = /tmp/lheinric/madgraph-1.5.10
INKSCAPE = /Applications/Inkscape.app/Contents/Resources/bin/inkscape

all: rivetanalysis/plots mcviz.pdf

MADEVENTDIR=$(PWD)/madgraphrun/Events/run_01

$(MADEVENTDIR)/events.lhe: mg5steering.cmd madgraphcards/param_card_stop3body.dat madgraphcards/proc_card_mg5_stop.dat
	$(MADGRAPH)/bin/mg5 -f mg5steering.cmd
	gunzip -c $(MADEVENTDIR)/events.lhe.gz > $@

pythiarun/pythiarun: pythiarun/pythiarun.cxx
	c++ -O2 -ansi -pedantic -W -Wall -Wshadow -m64 -Wno-shadow -I$(PYTHIA)/include -I$(HEPMC)/include \
		$< -o $@ \
		-L$(PYTHIA)/lib/archive -lpythia8 -llhapdfdummy -lpythia8tohepmc \
		-L$(HEPMC)/lib -lHepMC

pythiarun/output.hepmc: pythiarun/pythiarun pythiasteering.cmnd $(MADEVENTDIR)/events.lhe
	PYTHIA8DATA=$(PYTHIA)/xmldoc pythiarun/pythiarun pythiasteering.cmnd pythiarun/output.hepmc

rivetanalysis/RivetStops.so : rivetanalysis/RivetStops.cxx
	rivet-buildplugin $@ $<

rivetanalysis/Rivet.yoda: rivetanalysis/RivetStops.so pythiarun/output.hepmc
	rivet pythiarun/output.hepmc -a StopThreeBody --analysis-path=$(PWD)/rivetanalysis --histo-file=rivetanalysis/Rivet.yoda

rivetanalysis/plots : rivetanalysis/Rivet.yoda
	rivet-mkhtml rivetanalysis/Rivet.yoda -o rivetanalysis/plots

$(MADEVENTDIR)/events.lhe._0001.evts: $(MADEVENTDIR)/events.lhe
	ln $(MADEVENTDIR)/events.lhe $(MADEVENTDIR)/events.lhe._0001.evts

$(MADEVENTDIR)/events.lhe._0001.tar.gz: $(MADEVENTDIR)/events.lhe._0001.evts
	tar --directory $(MADEVENTDIR) -cvzf $(MADEVENTDIR)/events.lhe._0001.tar.gz events.lhe._0001.evts

gen_tf/evgen.pool.root: $(MADEVENTDIR)/events.lhe._0001.tar.gz
	mkdir -p gen_tf
	cd gen_tf && \
	JOBOPTSEARCHPATH=/cvmfs/atlas.cern.ch/repo/sw/Generators/MC12JobOptions/latest/common:$(JOBOPTSEARCHPATH) \
	Generate_tf.py --randomSeed 1234 --runNumber 10003 --ecmEnergy 14000 --maxEvents 100 \
	--jobConfig ../evgenJO.py --firstEvent 0 --inputGeneratorFile $(MADEVENTDIR)/events.lhe._0001.tar.gz \
	--outputEVNTFile evgen.pool.root

gen_tf/output.NTUP_TRUTH.root: gen_tf/evgen.pool.root
	cd gen_tf && \
	Reco_trf.py preExec="rec.doApplyAODFix.set_Value_and_Lock(False);from D3PDMakerConfig.D3PDMakerFlags import D3PDMakerFlags;D3PDMakerFlags.TruthWriteHadrons=True" \
	inputEVNTFile=evgen.pool.root outputNTUP_TRUTHFile=output.NTUP_TRUTH.root

mcviz.svg: pythiarun/output.hepmc
	mcviz -sFancyLines -sSimpleColors -tGluballs -e fdp -tNoKinks $<:4

mcviz.pdf: mcviz.svg
	$(INKSCAPE) --export-pdf $@ $< --verb=FitCanvasToDrawing
	pdfcrop $@
	mv $(basename $@)-crop.pdf $@
clean:
	rm -rf madgraphrun
	rm -rf pythiarun/pythiarun
	rm -rf pythiarun/output.hepmc
	rm -rf rivetanalysis/Rivet.yoda
	rm -rf rivetanalysis/RivetStops.so
	rm -rf rivetanalysis/plots
	rm -rf mcviz.pdf mcviz.svg
	rm -rf gen_tf

.PHONY: clean
