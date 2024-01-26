__title__ = 'MG_Block'
__author__ = 'Coded_Pro'
__version__ = '1.0'

import clr
clr.AddReferenceByPartialName("Fougerite")
import Fougerite

class MG_Block:

	def On_Research(self, ResearchEvent):
		if "Paper" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")
		elif "Metal Ceiling" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")
		elif "Metal Foundation" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")
		elif "Metal Pillar" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")
		elif "Metal Stairs" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")
		elif "Metal Wall" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")
		elif "Metal Window" in ResearchEvent.ItemName:
			ResearchEvent.Cancel()
			ResearchEvent.Player.Notice("Haji Nemitoni Ina ro Reserch Koni!")            
	def On_Crafting(self, CraftingEvent):
		if "Paper" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")
		elif "Metal Ceiling" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")
		elif "Metal Foundation" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")
		elif "Metal Wall" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")
		elif "Metal Pillar" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")
		elif "Metal Stairs" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")            
		elif "Weapon Part 1" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")     
		elif "Weapon Part 2" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")     
		elif "Weapon Part 3" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")    
		elif "Weapon Part 4" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")    
		elif "Weapon Part 5" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")    
		elif "Weapon Part 6" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")    
		elif "Weapon Part 7" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!") 
		elif "Armor Part 1" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")    
		elif "Armor Part 2" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")  
		elif "Armor Part 3" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")  
		elif "Armor Part 4" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")  
		elif "Armor Part 5" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")  
		elif "Armor Part 6" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")  
		elif "Armor Part 7" in CraftingEvent.ItemName:
			CraftingEvent.Cancel()
			CraftingEvent.Player.Notice("Haji Nemitoni Ina ro Craft Koni!")              