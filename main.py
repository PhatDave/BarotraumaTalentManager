import os
import xml.etree.ElementTree as ET
import numpy as np
import cv2

# from TalentManager.TalentManager import TalentManager
#
# talentManager = TalentManager()
# talentManager.loadAll()

root = r'D:\Steam\steamapps\common\Barotrauma\Content\Talents'

class Talent:
	def __init__(self, name, sheet, index):
		self.name = name
		self.sheet = sheet
		self.index = index
		self.index = (int(self.index.split(',')[0]), int(self.index.split(',')[1]))

	def cropImage(self, image):
		icon = image[128 * self.index[0]:128 * (self.index[0] + 1), 128 * self.index[1]:128 * (self.index[1] + 1)]
		return icon

	def __str__(self):
		return f'{self.name}\t{self.sheet}\t{self.index}'

talents = []
# Iterate over every file in root directory recursively
for root, dirs, files in os.walk(root):
	for file in files:
		if 'Talents' in file:
			file = f'{root}\\{file}'
			tree = ET.parse(file)
			root = tree.getroot()

			for talent in root:
				talentName = talent.attrib['identifier']
				iconSheet = talent.find('Icon').attrib['texture']
				iconIndex = talent.find('Icon').attrib['sheetindex']
				iconSize = talent.find('Icon').attrib['sheetelementsize']

				talentObj = Talent(talentName, iconSheet, iconIndex)
				talents.append(talentObj)

sheet1 = cv2.imread('TalentsIcons3.png')
for talent in talents:
	if 'TalentsIcons3' in talent.sheet:
		icon = talent.cropImage(sheet1)
		cv2.imwrite(f'{talent.name}.png', icon)
