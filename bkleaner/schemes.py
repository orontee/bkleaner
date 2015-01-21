"""Definition of common transformation schemes.

A scheme is an item of the ``scheme`` dictionary. Each scheme is
itself a dictionary with two keys: ``path`` and ``transformations``.
The value of the ``path`` key is the path of the style sheet where
transformations apply. The value of the ``transformations`` key is a
dictionary whose keys are CSS selectors and values describes
transformations or list such descriptions.

A transformation description is a dictionary with the following keys:

- ``property`` for the name of a CSS property to transform.

- ``operator`` to characterize the transformation to do. At the
  current time, it must be one of ``set`` or ``remove``.

- ``value`` for the value to set or remove according to the choosen
  operation."""

schemes = {'bibebook': {'path': 'stylesheet.css',
                        'transformations':
                        {'.indent': [{'property': 'text-indent',
                                      'value': '1em',
                                      'operator': 'set'},
                                     {'property': 'margin',
                                      'value': '0',
                                      'operator': 'set'}],
                         '.dropcap': [{'property': 'font-family',
                                       'value': '"Lettrines"',
                                       'operator': 'remove'},
                                      {'property': 'text-indent',
                                       'value': '0',
                                       'operator': 'set'}],
                         '.small-caps': [{'property': 'text-indent',
                                          'value': '0',
                                          'operator': 'set'},
                                         {'property': 'font-family',
                                          'value': '"SmallCaps"',
                                          'operator': 'remove'}],
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
                                             'operator': 'set'},
                                            {'property': 'display',
                                             'value': 'block',
                                             'operator': 'set'}]}},
           'pearson': {'path': 'OEBPS/html/0321601610.css',
                       'transformations':
                       {'.programlisting': [{'property': 'text-align',
                                             'value': 'left',
                                             'operator': 'set'},
                                            {'property': 'margin-left',
                                             'value': '0pt',
                                             'operator': 'set'}],
                        '.programlisting1': [{'property': 'text-align',
                                              'value': 'left',
                                              'operator': 'set'}],
                        '.romanAlt': [{'property': 'font-size',
                                       'operator': 'remove'}],
                        '.strongAlt': [{'property': 'font-size',
                                        'operator': 'remove'}],
                        'body': [{'property': 'margin-right',
                                  'value': '0pt',
                                  'operator': 'set'}],
                        'code': [{'property': 'font-size',
                                  'value': 'small',
                                  'operator': 'set'}]}}}
