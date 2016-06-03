.. currentmodule:: ilastikrag.rag

.. _rag:

Rag
---

..
   (The following |br| definition is the only way
   I can force numpydoc to display explicit newlines...) 

.. |br| raw:: html

   <br />


- :py:class:`Rag`
  
  - :py:meth:`__init__ <Rag.__init__>`
  - :py:meth:`supported_features <Rag.supported_features>`
  - :py:meth:`compute_features <Rag.compute_features>`
  - :py:meth:`edge_decisions_from_groundtruth <Rag.edge_decisions_from_groundtruth>`
  - :py:meth:`naive_segmentation_from_edge_decisions <Rag.naive_segmentation_from_edge_decisions>`
  - :py:meth:`serialize_hdf5 <Rag.serialize_hdf5>`
  - :py:meth:`deserialize_hdf5 <Rag.deserialize_hdf5>`
  - :py:meth:`dense_edge_tables <Rag.dense_edge_tables>`

.. autoclass:: Rag

   .. automethod:: __init__
   .. automethod:: supported_features
   .. automethod:: compute_features
   .. automethod:: edge_decisions_from_groundtruth
   .. automethod:: naive_segmentation_from_edge_decisions
   .. automethod:: serialize_hdf5
   .. automethod:: deserialize_hdf5
   .. autoattribute:: dense_edge_tables
   