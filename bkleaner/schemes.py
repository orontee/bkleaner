"""
Defines common transformation schemes.

A scheme is an item of the ``scheme`` dictionary. Each scheme is
itself a dictionary whose keys are CSS selectors and values describes
transformations or list such descriptions.

A transformation description is dictionary with the following keys: 

- ``property`` for the name of a CSS property to transform.

- ``operator`` to characterize the transformation to do. At the
  current time, it must be one of ``set`` or ``remove``.

- ``value`` for the value to set or remove according to the choosen
  operation.
"""

schemes = {'bibebook': {'.indent': [{'property': 'text-indent',
                                     'value': '1em',
                                     'operator': 'set'},
                                    {'property': 'margin',
                                     'value': '0',
                                     'operator': 'set'}],
                        '.bib-img': [{'property': 'height',
                                      'value': '100%',
                                      'operator': 'set'},
                                     {'property': 'width',
                                      'value': '100%',
                                      'operator': 'set'}],
                        '.bib-body': {'property': 'font-family',
                                      'value': '"Fontbase"',
                                      'operator': 'remove'}}}
