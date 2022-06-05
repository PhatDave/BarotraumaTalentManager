import xml.etree.ElementTree as ET

from Constants import ABSOLUTE_ROOT
from TalentManager.TalentTree import TalentTree


class Character:
    def __init__(self, name):
        self.characterSubstitutionTable = {
            'securityofficer': "Security",
            'captain': "Captain",
            'assistant': "Assistant",
            'engineer': "Engineer",
            'mechanic': "Mechanic",
            'medicaldoctor': "Doctor",
        }

        self.name = name

        alternateName = self.characterSubstitutionTable[self.name]
        self.fileName = f'{ABSOLUTE_ROOT}\\{alternateName}\\Talents{alternateName}.xml'
        self.talentTrees = []

    def parse(self, tree):
        for talentTree in tree:
            treeName = talentTree.attrib['identifier']
            ttree = TalentTree(treeName)
            ttree.parse(talentTree)
            self.talentTrees.append(ttree)

    def loadTalentDetails(self):
        tree = ET.parse(self.fileName)
        root = tree.getroot()
        for tree in self.talentTrees:
            tree.parseTalentDetails(root)

    def __str__(self):
        output = f'{self.characterSubstitutionTable[self.name]}:\n'
        for tree in self.talentTrees:
            output += f'\t{str(tree)}\n'
        return output
