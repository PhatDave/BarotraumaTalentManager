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
        self.fileTree = None
        self.talentTrees = []

    def parse(self, tree):
        for talentTree in tree:
            treeName = talentTree.attrib['identifier']
            ttree = TalentTree(treeName)
            ttree.parse(talentTree)
            self.talentTrees.append(ttree)

    def loadTalentDetails(self):
        self.fileTree = ET.parse(self.fileName)
        root = self.fileTree.getroot()
        for talentTree in self.talentTrees:
            talentTree.parseTalentDetails(root)

    def verifyTalents(self):
        for tree in self.talentTrees:
            tree.verifyTalents()

    def getCount(self):
        count = 0
        for tree in self.talentTrees:
            count += tree.getCount()
        return count

    def getTalentByName(self, name):
        talent = None
        for tree in self.talentTrees:
            talent = tree.getTalentByName(name)
            if talent is not None:
                break
        return talent

    def removeTalent(self, talent):
        root = self.fileTree.getroot()
        element = root.find(f'Talent[@identifier="{talent.element.attrib["identifier"]}"]')
        root.remove(element)

    def addTalent(self, talent):
        self.fileTree.getroot().append(talent.element)

    def save(self):
        with open(self.fileName, 'wb') as f:
            self.fileTree.write(f)

    def __str__(self):
        output = f'{self.characterSubstitutionTable[self.name]} ({self.getCount()}):\n'
        for tree in self.talentTrees:
            output += f'\t{str(tree)}\n'
        return output
