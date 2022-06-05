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

    def __str__(self):
        output = f'{self.name}:\n'
        for talent in self.talents:
            output += f'\t{str(talent)}\n'
        return output
