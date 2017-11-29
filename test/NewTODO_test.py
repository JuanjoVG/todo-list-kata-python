import unittest

from test.Seeder import Seeder


class NewTODO_test(unittest.TestCase):
    def setUp(self):
        self.seeder = Seeder()

    def test_whenCreateANewTODO_withAEmptyManager_thenManagerHasATODO(self):
        manager = self.seeder.createEmptyManager()
        manager.createTODO("TODO name")
        self.assertEqual(len(manager.TODOList), 1)

    def test_whenCreateANewTODO_withAManagerThatContainsATODO_thenManagerHas2TODOs(self):
        manager = self.seeder.createEmptyManager()
        manager.createTODO("TODO name")
        self.assertEqual(len(manager.TODOList), 2)

if __name__ == '__main__':
    unittest.main()
