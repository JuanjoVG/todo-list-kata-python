import unittest

from test.Seeder import Seeder


class FormattingTODOList_test(unittest.TestCase):
    def setUp(self):
        self.seeder = Seeder()

    def test_whenPrintTheTODOs_withoutAnyTODO_thenReturnsEmptyString(self):
        manager = self.seeder.createEmptyManager()
        s = manager.printTODOs()
        self.assertEqual(s, "")

    def test_whenPrintTheTODOs_withAnOnlyTODO_thenReturnsOnlyATODO(self):
        manager = self.seeder.createManagerWithATODO()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(len(TODOList), 1)

    def test_whenPrintTheTODOs_withAnOnlyTODO_thenReturnsTheTODOName(self):
        manager = self.seeder.createManagerWithATODO()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(TODOList[0], "TODO1")

    def test_whenPrintTheTODOs_withTwoTODOs_thenReturnsAStringWithTwoLines(self):
        manager = self.seeder.createManagerWith2TODOs()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(len(TODOList), 2)

    def test_whenPrintTheTODOs_withTwoTODOs_thenReturnsTwoLinesWithTheTwoNames(self):
        manager = self.seeder.createManagerWith2TODOs()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(TODOList[0], "TODO1")
        self.assertEqual(TODOList[1], "TODO2")


if __name__ == '__main__':
    unittest.main()
