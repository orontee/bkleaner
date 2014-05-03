Usage
=====

To change the style sheet of an book in EPUB format, say
``mybook.epub``, you just call the following command::

  $ bkleaner -s bibebook mybook.epub

A new file named ``mybook_clean.epub`` is created. The ``-s`` option is
used to select the transformation scheme to apply.

Short help is available with the usual ``-h`` option.

Return status
-------------

.. automodule:: bkleaner.errors
   :members:
