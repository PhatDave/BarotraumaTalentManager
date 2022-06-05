from TalentManager.TalentTree import TalentTree


class Character:
    def __init__(self, name):
        from main import ABSOLUTE_ROOT
        global ABSOLUTE_ROOT

        self.name = name

        self.prettyName = self.name.capitalize()
        self.fileName = f'{ABSOLUTE_ROOT}\\{self.prettyName}\\Talents{self.prettyName}.xml'
        self.talentTrees = []

    def parse(self, tree):
        for talentTree in tree:
            treeName = talentTree.attrib['identifier']
            ttree = TalentTree(treeName)
            ttree.parse(talentTree)
            self.talentTrees.append(ttree)

    def __str__(self):
        output = f'{self.prettyName}:\n'
        for tree in self.talentTrees:
            output += f'\t{str(tree)}\n'
        return output
