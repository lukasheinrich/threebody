#!/usr/bin/env python
from hepmcanalysis.events import events
from hepmcanalysis.streamproxy import ifstream_proxy
import hepmc
import pypdt
import argparse
import IPython
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',dest='file',type=str,help='input HepMC file')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

def main():
  proxy = ifstream_proxy(args.file)

  g = hepmc.IO_GenEvent(proxy.stream())
  for i,e in enumerate(events(g)):
    print '----------------'
    finalstate = [p for p in e.particles() if p.status()==1]
    print 'event #{0}: number of particles in event: {1}'.format(i,len(finalstate))
    
if __name__ == '__main__':
  main()
