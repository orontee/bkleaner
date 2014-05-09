"""Definition of the transformation process."""

import logging

logger = logging.getLogger('bkleaner')


class Transformer(object):
    """CSS style sheets transformer"""

    def __init__(self, scheme):
        """Store the scheme of transformations to apply."""
        self._scheme = scheme

    def _set_property(self, selector, name, value):
        selector.style.setProperty(name, value)
        msg = ("""Setting value of '{name}' attribute """
               """for '{selector}' selector""")
        logger.info(msg.format(value=value,
                               name=name,
                               selector=selector.selectorText))

    def _remove_from_property(self, selector, name, raw, value):
        if value is None:
            must_remove = True
        else:
            values = [v.strip() for v in raw.split(',')]
            must_remove = (values == [value])
            
        if must_remove:
            selector.style.removeProperty(name)
            msg = ("""Removing attribute '{name}' """
                   """ for '{selector}' selector""")          
        elif value in values:
            selector.style.setProperty(name, ', '.join(values))
            msg = ("""Removing value of '{name}' attribute """
                   """for '{selector}' selector""")
        logger.info(msg.format(value=value,
                               name=name,
                               selector=selector.selectorText))
        
    def __call__(self, sheet):
        """Transform the given CSS stylesheet."""
        for selector in sheet:
            if (hasattr(selector, 'selectorText')
                and selector.selectorText in self._scheme.keys()):
                trans = self._scheme[selector.selectorText]
                if not isinstance(trans, list):
                    trans = [trans]
                props = {}
                for n, t in enumerate(trans):
                    props[t['property']] = n
                if len(props) > 0:
                    for t in trans:
                        name = t['property']
                        operator = t['operator']
                        target = t.get('value', None)
                        current = selector.style.getPropertyValue(name)
                        if operator == 'set':
                            if current != target:
                                self._set_property(selector, name, target)
                        elif operator == 'remove' and current != "":
                            self._remove_from_property(selector, name,
                                                       current, target)
