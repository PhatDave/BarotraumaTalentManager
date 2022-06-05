class Talent:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.treeElement = None

    def parseDetails(self, tree):
        element = tree.find(f'Talent[@identifier="{self.name}"]')
        print(element)

    def __str__(self):
        return f'\t{self.name} {self.level}'
