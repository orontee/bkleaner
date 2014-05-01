import logging

logger = logging.getLogger('bkleaner')


class Transformer(object):
    def __init__(self, transform):
        self._trans = transform
    
    def _apply(self, t, rule, s):
        if t['operator'] == 'set':
            if s.value != t['value']:
                s.value = t['value']
                msg = ("""Setting value of '{name}' attribute """
                       """for '{selector}' selector""")
                logger.info(msg.format(value=s.value,
                                       name=s.name,
                                       selector=rule.selectorText))
        elif t['operator'] == 'remove':
            values = [v.strip() for v in s.value.split(',')]
            if t['value'] in values:
                values = [v for v in values if v != t['value']]
                s.value = ', '.join(values)
                msg = ("""Removing value of '{name}' attribute """
                       """for '{selector}' selector""")
                logger.info(msg.format(value=s.value,
                                       name=s.name,
                                       selector=rule.selectorText))


    def __call__(self, sheet):
        for rule in sheet:
            if rule.selectorText in self._trans.keys():
                trans = self._trans[rule.selectorText]
                if not isinstance(trans, list):
                    trans = [trans]
                props = {}
                for n, t in enumerate(trans):
                    props[t['property']] = n
                if len(props) > 0:
                    for s in rule.style:
                        if s.name in props.keys():
                            t = trans[props[s.name]]
                            self._apply(t, rule, s)
