import unittest

from Item import Item


class ItemShould(unittest.TestCase):
    def test_print_with_x_when_checked(self):
        item = Item("done")
        item.check()
        self.assertEqual(item.representation(), "[x] done")

    def test_print_empty_when_unchecked(self):
        item = Item("test")
        self.assertEqual(item.representation(), "[] test")

    def test_item_is_checked_when_check(self):
        item = Item("test")
        item.check()
        self.assertEqual(item.is_checked(), True)

    def test_item_is_unchecked_when_create(self):
        item = Item("test")
        self.assertEqual(item.is_checked(), False)
