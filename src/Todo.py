from Item import Item


class Todo(object):
    def __init__(self):
        self.items = []

    def add(self, description):
        self.items.append(Item(description))

    def check(self, index):
        try:
            self.items[index].check()
        except IndexError:
            pass

    def print(self):
        print("TODO list:")
        print("----------")
        for i in range(len(self.items)):
            print(str(i) + ": " + self.items[i].representation())
        print()

    def remove(self, index):
        try:
            self.items.pop(index)
        except IndexError:
            pass

    def uncheck(self, index):
        try:
            self.items[index].uncheck()
        except IndexError:
            pass
