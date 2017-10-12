import unittest

from Todo import Todo


class TodoShould(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.todo = Todo()

    def test_new_todo_has_no_items_when_created(self):
        self.assertEqual(len(self.todo.items), 0)

    def test_todo_checks_an_item(self):
        self.todo.add("item 1")
        self.todo.check(0)
        self.assertEqual(len(self.todo.items), 1)
        self.assertEqual(self.todo.items[0].is_checked(), True)

    def test_removes_makes_todo_have_one_item_less(self):
        self.todo.add("item 1")
        self.assertEqual((len(self.todo.items)), 1)
        self.todo.remove(0)
        self.assertEqual((len(self.todo.items)), 0)

    def test_removes_on_empty_list_does_not_throw_an_exception(self):
        self.assertEqual((len(self.todo.items)), 0)
        self.todo.remove(5)
        self.assertRaises(IndexError)

    def test_todo_uncheck_an_item(self):
        self.todo.add("item 1")
        self.todo.check(0)
        self.assertEqual(self.todo.items[0].is_checked(), True)
        self.todo.uncheck(0)
        self.assertEqual(self.todo.items[0].is_checked(), False)
