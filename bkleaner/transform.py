"""Definition of the transformation process.

"""

import logging

logger = logging.getLogger('bkleaner')


class Transformer(object):
    """Class representing objects that transform CSS style sheets
    according to a given scheme.

    """
    def __init__(self, scheme):
        """Store the scheme of transformations to apply.

        """
        self._scheme = scheme
    
    def _apply(self, t, selector, s):
        """Apply the transformation ``t`` to the style ``s`` found in the
        ``selector`` CSS selector.

        """
        if t['operator'] == 'set':
            if s.value != t['value']:
                s.value = t['value']
                msg = ("""Setting value of '{name}' attribute """
                       """for '{selector}' selector""")
                logger.info(msg.format(value=s.value,
                                       name=s.name,
                                       selector=selector.selectorText))
        elif t['operator'] == 'remove':
            values = [v.strip() for v in s.value.split(',')]
            if t['value'] in values:
                values = [v for v in values if v != t['value']]
                s.value = ', '.join(values)
                msg = ("""Removing value of '{name}' attribute """
                       """for '{selector}' selector""")
                logger.info(msg.format(value=s.value,
                                       name=s.name,
                                       selector=selector.selectorText))


    def __call__(self, sheet):
        """Transform the given CSS stylesheet.

        """
        for selector in sheet:
            if selector.selectorText in self._scheme.keys():
                trans = self._scheme[selector.selectorText]
                if not isinstance(trans, list):
                    trans = [trans]
                props = {}
                for n, t in enumerate(trans):
                    props[t['property']] = n
                if len(props) > 0:
                    for s in selector.style:
                        if s.name in props.keys():
                            t = trans[props[s.name]]
                            self._apply(t, selector, s)
