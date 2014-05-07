"""Definition of common transformation schemes.

A scheme is an item of the ``scheme`` dictionary. Each scheme is
itself a dictionary with two keys: ``path`` and ``transformations``.
The value of the ``path`` key is the path of the style sheet where
transformations apply. The value of the ``transformations`` dictionary
is a dictionary whose keys are CSS selectors and values describes
transformations or list such descriptions.

A transformation description is a dictionary with the following keys:

- ``property`` for the name of a CSS property to transform.

- ``operator`` to characterize the transformation to do. At the
  current time, it must be one of ``set`` or ``remove``.

- ``value`` for the value to set or remove according to the choosen
  operation.

"""

schemes = {'bibebook': {'path': 'stylesheet.css',
                        'transformations':
                        {'.indent': [{'property': 'text-indent',
                                     'value': '1em',
                                     'operator': 'set'},
                                    {'property': 'margin',
                                     'value': '0',
                                     'operator': 'set'}],
                        '.dropcap': {'property': 'font-family',
                                     'value': '"Lettrines"',
                                     'operator': 'remove'},
                        '.bib-img': [{'property': 'height',
                                      'value': '100%',
                                      'operator': 'set'},
                                     {'property': 'width',
                                      'value': '100%',
                                      'operator': 'set'}],
                        '.bib-body': [{'property': 'font-family',
                                       'value': '"Fontbase"',
                                       'operator': 'remove'},
                                      {'property': 'margin',
                                       'value': '0 4pt 0 4pt',
                                       'operator': 'set'}]}},
           'efele': {'path': 'OEBPS/style-common.css',
                     'transformations':
                     {'img.fullpageimage': [{'property': 'height',
                                             'value': '100%',
                                             'operator': 'set'},
                                            {'property': 'width',
                                             'value': '100%',
                                             'operator': 'set'}]}}}
