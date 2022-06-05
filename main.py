from TalentManager import TalentManager

ABSOLUTE_ROOT = r'D:\Steam\steamapps\common\Barotrauma\Content\Talents'

talentManager = TalentManager.TalentManager()
talentManager.loadAll()
print(str(talentManager))
