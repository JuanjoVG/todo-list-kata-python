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
