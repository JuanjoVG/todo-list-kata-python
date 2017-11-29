import unittest

from src.TODOManager import TODOManager


class TODOManager_test(unittest.TestCase):

    def test_whenPrintTheTODOs_withoutAnyTODO_thenReturnsEmptyString(self):
        manager = self.createEmptyManager()
        s = manager.printTODOs()
        self.assertEqual(s, "")

    def test_whenPrintTheTODOs_withAnOnlyTODO_thenReturnsOnlyATODO(self):
        manager = self.createManagerWithATODO()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(len(TODOList), 1)

    def test_whenPrintTheTODOs_withAnOnlyTODO_thenReturnsTheTODOName(self):
        manager = self.createManagerWithATODO()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(TODOList[0], "TODO1")

    def test_whenPrintTheTODOs_withTwoTODOs_thenReturnsAStringWithTwoLines(self):
        manager = self.createManagerWith2TODOs()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(len(TODOList), 2)

    def test_whenPrintTheTODOs_withTwoTODOs_thenReturnsTwoLinesWithTheTwoNames(self):
        manager = self.createManagerWith2TODOs()
        s = manager.printTODOs()
        TODOList = s.splitlines()
        self.assertEqual(TODOList[0], "TODO1")
        self.assertEqual(TODOList[1], "TODO2")

    def createEmptyManager(self):
        return TODOManager()

    def createManagerWithATODO(self):
        manager = TODOManager()
        manager.TODOList = ["TODO1"]
        return manager

    def createManagerWith2TODOs(self):
        manager = TODOManager()
        manager.TODOList = ["TODO1", "TODO2"]
        return manager