Welcome to bkleaner's documentation!
====================================

A tool which allows to change style sheets of books in EPUB format.

Installation
============

The code has been written and tested with Python 3. To build a source
distribution and install it, one need the Python package `setuptools`
then::

  make install

To uninstall::

  make uninstall

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

Global variables for values of scripts return status.

+-------+-----------------------+
| Value | Description           |
+=======+=======================+
|0      | No error              |
+-------+-----------------------+
|1      | File not found        |
+-------+-----------------------+
|2      | Scheme not found      |
+-------+-----------------------+
|3      | Style sheet not found |
+-------+-----------------------+

Credits
=======

* Matthias Meulien <orontee@gmail.com>
