SUSY Three Body Decays
======================


This is code for an upcoming analysis of ATLAS data looking for supersymmetric decays.

Setup
------

    git clone https://github.com/lukasheinrich/threebody.git
    cd threebody                                            
    mkvirtualenv threebody --system-site-packages
	workon threebody
	pip install $PWD
	workon threebody #optional, resource $PATH for tab completion
	
Details
-------
For EVGEN generation using `asetup 18.1.0,here` works as an Athena Release

Requirements
-------

madgraph 1.5.10: `bzr branch lp:~maddevelopers/mg5amcnlo/1.5.10 madgraph-1.5.10`

Get Results
-----
get waf into the workflow dir:
    
    cd workflow
    wget http://waf.googlecode.com/files/waf-1.7.11 -O waf && chmod +x ./waf

configure waf (if the binaries are not in your current path use with `--with-X` flags). for me this is

	./waf configure --with-inkscape /Applications/Inkscape.app/Contents/Resources/bin --with-madgraph=/Users/lukas/heptools/madgraph-1.5.10    


and run waf

	./waf
	
this should produce results in the `results` directory.