from unittest import TestCase

from ... import helpers as h


class TestHelpers(TestCase):

    def test_grouper_even_split(self):
        self.assertEqual(list(h.grouper(3, range(9))),
                         [[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    def test_grouper_uneven_split(self):
        self.assertEqual(list(h.grouper(4, range(6))),
                         [[0, 1, 2, 3], [4, 5]])

    def test_grouper_makes_iterable(self):
        try:
            iter(h.grouper(5, [1, 2, 3, 4, 5]))
        except TypeError:
            raise AssertionError('should be iterable')

    def test_grouper_row_larger_than_input(self):
        self.assertEqual(list(h.grouper(5, ['f', 'bar', 'baz'])),
                         [['f', 'bar', 'baz']])

    def test_prettify_plain(self):
        self.assertEqual(h.prettify('joe_user'), 'Joe user')

    def test_prettify_multi(self):
        self.assertEqual(h.prettify('foo_bar_baz_quux'), 'Foo bar baz quux')

    def test_prettify_num(self):
        self.assertEqual(h.prettify(123), '123')
