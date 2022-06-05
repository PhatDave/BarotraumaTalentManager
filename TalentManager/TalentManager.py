import xml.etree.ElementTree as ET

from Character import Character
from main import ABSOLUTE_ROOT

class TalentManager:
    def __init__(self):
        self.talents = 'TalentTrees.xml'
        self.characters = []

    def loadAll(self):
        tree = ET.parse(f'{ABSOLUTE_ROOT}\\{self.talents}')
        root = tree.getroot()
        for talentTree in root:
            character = talentTree.attrib['jobidentifier']
            if character not in self.characters:
                char = Character(character)
                char.parseTalents(talentTree)



