"""Test transform module."""

import cssutils
from unittest import (TestCase, main)
from bkleaner.transform import Transformer

CSS = u"""/* a comment with umlaut &auml; */
@namespace html "http://www.w3.org/1999/xhtml";
@variables { BG: #fff }
html|a { color:red; background: var(BG) }
p { margin: 0; text-indent: 0 }
img { width: 100% }"""


class TestTransform(TestCase):

    def setUp(self):
        self.sheet = cssutils.parseString(CSS)

    def test_call(self):
        scheme = {'p': [{'property': 'text-indent',
                         'value': '1em',
                         'operator': 'set'},
                        {'property': 'color',
                         'value': 'red',
                         'operator': 'set'}],
                  'img': {'property': 'width',
                          'operator': 'remove'}}
        Transformer(scheme)(self.sheet)
        for selector in self.sheet:
            if hasattr(selector, 'selectorText'):
                if selector.selectorText == 'p':
                    self.assertEqual(selector.style.getPropertyValue(
                        'text-indent'), '1em')
                    self.assertEqual(selector.style.getPropertyValue(
                        'color'), 'red')
                elif selector.selectorText == 'img':
                    self.assertEqual(selector.style.getPropertyValue(
                        'width'), '')


if __name__ == '__main__':
    main()
