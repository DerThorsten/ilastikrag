.. ilastikrag documentation master file, created by
   sphinx-quickstart on Wed Mar  2 17:59:16 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |br| raw:: html

   <br />


The ``ilastikrag`` package implements an ND Region Adjacency Graph (Rag) datastructure,
along with  algorithms to compute *features* for the edges between superpixels in the ``Rag``.
It has good performance, thanks to the `VIGRA <http://ukoethe.github.io/vigra>`_ image processing
library and the `pandas <http://pandas.pydata.org/>`_ data analysis package.

Tutorials
=========

- `Quickstart Tutorial <_static/quickstart-tutorial.html>`_
- `Anisotropic Rag Tutorial <_static/anisotropic-tutorial.html>`_


API Reference
=============

.. toctree::
   :maxdepth: 2

   rag
   accumulators
   util
   gui
