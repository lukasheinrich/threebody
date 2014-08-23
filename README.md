SUSY Three Body Decays
======================


This is code for an upcoming analysis of ATLAS data looking for supersymmetric decays.

Setup
------

    git clone https://github.com/lukasheinrich/threebody.git ~/threebody
    cd ~/threebody
    mkvirtualenv threebody
    workon threebody
    HEPMCPATH=$HOME/heptools/local pip install --editable $PWD --process-dependency-links
    cd workflow
    ./waf configure


## Bootstraps
### lxplus

    wget https://raw.githubusercontent.com/lukasheinrich/threebody/master/utils/lxplus-bootstrap
    chmod +x lxplus-bootstrap
    ./lxlpus-bootsrap

### CernVM

to setup a fresh CernVM 3 instance you can use these scripts:

    https://github.com/lukasheinrich/code-snippets/tree/master/vmscripts

Details
-------
For EVGEN generation using `asetup 18.1.0,here` works as an Athena Release

Requirements
-------

* python2.7, virtualenv 1.6
* madgraph 1.5.10: `bzr branch lp:~maddevelopers/mg5amcnlo/1.5.10 madgraph-1.5.10`
* pythia8: `wget http://home.thep.lu.se/~torbjorn/pythia8/pythia8186.tgz`
* rivet (comes with HepMC): `wget http://rivet.hepforge.org/hg/bootstrap/raw-file/2.1.2/rivet-bootstrap`


Get Results
-----
configure waf (if the binaries are not in your current path use with `--with-X` flags). for me this is

	./waf configure --with-inkscape /Applications/Inkscape.app/Contents/Resources/bin --with-madgraph=/Users/lukas/heptools/madgraph-1.5.10    


and run waf

	./waf
	
this should produce results in the `results` directory.
