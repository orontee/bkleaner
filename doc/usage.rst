Usage
=====

To change the style sheet of an book in EPUB format, say
``mybook.epub``, you just call the following command::

  $ bkleaner -s bibebook mybook.epub

A new file named ``mybook_clean.epub`` is created. The ``-s`` option is
used to select the transformation scheme to apply.

Short help is available with the usual ``-h`` option::
  
  $ bkleaner -h
  usage: bkleaner [-h] -s {bibebook} path [path ...]

  Change stylesheets of ebooks in EPUB format

  positional arguments:
    path           Path to files to transform

  optional arguments:
    -h, --help     show this help message and exit
    -s {bibebook}  Transformation scheme


Return status
-------------

.. automodule:: bkleaner.errors
   :members:
