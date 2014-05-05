"""Test transform module."""

import cssutils
from unittest import (TestCase, main)
from bkleaner.transform import Transformer

CSS = u"""/* a comment with umlaut &auml; */
@namespace html "http://www.w3.org/1999/xhtml";
@variables { BG: #fff }
html|a { color:red; background: var(BG) }
p { margin: 0; text-indent: 0 }"""


class TestTransform(TestCase):

    def setUp(self):
        self.sheet = cssutils.parseString(CSS)

    def test_call(self):
        scheme = {'p': [{'property': 'text-indent',
                         'value': '1em',
                         'operator': 'set'}]}

        Transformer(scheme)(self.sheet)
        for selector in self.sheet:
            if (hasattr(selector, 'selectorText')
                and selector.selectorText == 'p'):
                for s in selector.style:
                    if s.name == 'text-indent':
                        self.assertEqual(s.value, '1em')


if __name__ == '__main__':
    main()
