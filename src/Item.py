class Item(object):
    def __init__(self, description):
        self.description = description
        self.checked = False

    def is_checked(self):
        return self.checked

    def representation(self):
        checked_representation = '[x]' if self.checked else '[]'
        return checked_representation + " " + self.description

    def check(self):
        self.checked = True
