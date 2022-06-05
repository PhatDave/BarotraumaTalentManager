from TalentManager.Talent import Talent


class TalentTree:
    def __init__(self, name):
        self.name = name
        self.talents = []

    def parse(self, tree):
        talentLevel = 0
        for talentRow in tree:
            talentLevel += 1
            for talent in talentRow:
                talentName = talent.attrib['identifier']
                talentObj = Talent(talentName, talentLevel)
                self.talents.append(talentObj)

    def parseTalentDetails(self, tree):
        for talent in self.talents:
            talent.parseDetails(tree)

    def verifyTalents(self):
        for talent in self.talents:
            assert talent.element is not None

    def getCount(self):
        count = len(self.talents)
        return count

    def getTalentByName(self, name):
        talent = None
        for talentIt in self.talents:
            if talentIt.name == name:
                talent = talentIt
                break
        return talent

    def __str__(self):
        output = f'{self.name} ({self.getCount()}):\n'
        for talent in self.talents:
            output += f'\t{str(talent)}\n'
        return output
