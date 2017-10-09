from Item import Item


class Todo(object):
    def __init__(self):
        self.items = []

    def add(self, param):
        item = Item(param)
        self.items.append(item)

    def check(self, index):
        self.items[index].check()

    def print(self):
        print("TODO list:")
        print("----------")
        for item in self.items:
            print(item.representation())
        print()
