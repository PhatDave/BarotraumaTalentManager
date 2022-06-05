import xml.etree.ElementTree as ET

from TalentManager.Character import Character


class TalentManager:
    def __init__(self):
        from main import ABSOLUTE_ROOT
        global ABSOLUTE_ROOT

        self.talents = 'TalentTrees.xml'
        self.characters = []

    def loadAll(self):
        tree = ET.parse(f'{ABSOLUTE_ROOT}\\{self.talents}')
        root = tree.getroot()
        for talentTree in root:
            character = talentTree.attrib['jobidentifier']
            if character not in self.characters:
                char = Character(character)
                char.parse(talentTree)
                self.characters.append(char)

    def __str__(self):
        output = "TalentManager:\n"
        for character in self.characters:
            output += f"\t{str(character)}\n"
        return output
