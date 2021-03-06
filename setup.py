from setuptools import find_packages, setup

setup(
      name = 'threebody',
      version = 0.1,
      packages = find_packages(),
      author = 'Lukas Heinrich',
      author_email = 'lukas.heinrich@cern.ch',
      scripts=['utils/readhepmc.py','utils/jj2.py'],
      install_requires=['pyhepmc>=0.5','mcviz','hepmcanalysis','pypdt','jinja2'],
      dependency_links=['https://github.com/mcviz/mcviz/tarball/master#egg=mcviz-0.1',
                        'https://github.com/lukasheinrich/hepmcanalysis/tarball/master#egg=hepmcanalysis-0.0.1']
      )
