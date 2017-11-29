from src.TODOManager import TODOManager

class Seeder:
    def __init__(self):
        pass

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
