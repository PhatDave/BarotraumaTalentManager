from TalentManager.TalentManager import TalentManager

talentManager = TalentManager()
talentManager.loadAll()
# print(str(talentManager))
talentManager.move('engineer:weaponsengineer:1:strengthenedalloys->engineer:electrician:1')
# print(talentManager.getTalentByName('militaryapplications'))
