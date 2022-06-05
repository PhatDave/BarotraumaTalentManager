import xml.etree.ElementTree as ET

from TalentManager.Character import Character
from Constants import ABSOLUTE_ROOT


class TalentManager:
    def __init__(self):
        self.talents = 'TalentTrees.xml'
        self.talentsTree = None
        self.characters = {}

    def loadAll(self):
        self.talentsTree = ET.parse(f'{ABSOLUTE_ROOT}\\{self.talents}')
        root = self.talentsTree.getroot()
        for talentTree in root:
            character = talentTree.attrib['jobidentifier']
            if character not in self.characters.keys():
                char = Character(character)
                char.parse(talentTree)
                self.characters[character] = char
        for character in self.characters.values():
            character.loadTalentDetails()
            character.verifyTalents()

    def getCount(self):
        count = 0
        for character in self.characters.values():
            count += character.getCount()
        return count

    def getTalentByName(self, name):
        talent = None
        for character in self.characters.values():
            talent = character.getTalentByName(name)
            if talent is not None:
                break
        return talent
    def __str__(self):
        output = f"TalentManager ({self.getCount()}):\n"
        for character in self.characters.values():
            output += f"\t{str(character)}\n"
        return output
