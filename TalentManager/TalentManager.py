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

    def move(self, input):
        sourceCharacter, sourceTree, sourceLevel, sourceTalent, destinationCharacter, destinationTree, destinationLevel = self.parseInput(input)
        print(f"Moving {sourceTalent} from {sourceCharacter}'s {sourceTree} tree to {destinationCharacter}'s {destinationTree} tree")

        talent = self.findInTree(sourceTalent)
        sourceRow = self.findRow(f'{sourceCharacter}:{sourceTree}:{sourceLevel}')
        destinationRow = self.findRow(f'{destinationCharacter}:{destinationTree}:{destinationLevel}')
        destinationRow.append(talent)
        sourceRow.remove(talent)

        self.characters[sourceCharacter].removeTalent(talent)
        self.characters[destinationCharacter].addTalent(talent)

        self.save()

    def findInTree(self, talentName):
        for characterTree in self.talentsTree.getroot():
            for talentTree in characterTree:
                for talentRow in talentTree:
                    for talent in talentRow:
                        if talent.attrib['identifier'] == talentName:
                            return talent
        return None

    def findRow(self, input):
        character, tree, level = input.split(':')
        level = int(level)
        for characterTree in self.talentsTree.getroot():
            if characterTree.attrib['jobidentifier'] == character:
                for talentTree in characterTree:
                    if talentTree.attrib['identifier'] == tree:
                        row = 1
                        for talentRow in talentTree:
                            if row == level:
                                return talentRow
                            row += 1
        return None

    def parseInput(self, input):
        # talentManager.move('engineer:weaponsengineer:1:militaryapplications->engineer:electrician:1')
        source, destination = input.split('->')
        sourceCharacter, sourceTree, sourceLevel, sourceTalent = source.split(':')
        destinationCharacter, destinationTree, destinationLevel = destination.split(':')
        return sourceCharacter, sourceTree, sourceLevel, sourceTalent, destinationCharacter, destinationTree, destinationLevel

    def save(self):
        with open(f'{ABSOLUTE_ROOT}\\{self.talents}', 'wb') as f:
            self.talentsTree.write(f)

    def __str__(self):
        output = f"TalentManager ({self.getCount()}):\n"
        for character in self.characters.values():
            output += f"\t{str(character)}\n"
        return output
