#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='ilastikrag',
      version='0.1',
      description='ND Region Adjacency Graph with edge feature algorithms',
      author='Stuart Berg',
      author_email='bergs@janelia.hhmi.org',
      url='github.com/stuarteberg/ilastikrag',
      packages=find_packages()
      ## see conda-recipe/meta.yaml for dependency information
      ##install_requires=['numpy', 'h5py', 'pandas', 'vigra', 'networkx']
     )
