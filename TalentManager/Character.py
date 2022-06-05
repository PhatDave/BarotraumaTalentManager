from main import ABSOLUTE_ROOT

class Character:
    def __init__(self, name):
        self.name = name

        self.prettyName = self.name.capitalize()
        self.fileName = f'{ABSOLUTE_ROOT}\\{self.prettyName}\\Talents{self.prettyName}.xml'

    def parseTalents(self, tree):
        for talentTree in tree:
            print(talentTree.attrib['identifier'])
