from setuptools import find_packages, setup

setup(
      name = 'threebody',
      version = 0.1,
      packages = find_packages(),
      author = 'Lukas Heinrich',
      author_email = 'lukas.heinrich@cern.ch',
      scripts=['utils/readhepmc.py','utils/jj2.py'],
      )
