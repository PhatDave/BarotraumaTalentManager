from TalentManager.TalentManager import TalentManager

talentManager = TalentManager()
talentManager.loadAll()
# print(str(talentManager))
talentManager.move('engineer:weaponsengineer:2:strengthenedalloys->securityofficer:specialist:1')
# print(talentManager.getTalentByName('militaryapplications'))
