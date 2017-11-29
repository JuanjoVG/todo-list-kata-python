class TODOManager():
    TODOList = []

    def __init__(self):
        pass

    def printTODOs(self):
        return '\n'.join(self.TODOList)

    def createTODO(self, name):
        self.TODOList.append(name)
