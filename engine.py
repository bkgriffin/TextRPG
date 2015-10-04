#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Engine class~
# 
__author__     = "Brandon Griffin"
__copyright__  = "Copyright 2015"
__credits__    = "Brandon Griffin"
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Brandon Griffin"
__email__      = "brandon.k.griffin@gmail.com"
__status__     = "Development"

from sys import exit
import time, toolkit
from character import *
from weapon import *
from armor import *
from accessory import *
from item import *

class Engine(object):
	"""Game Engine"""
	def __init__(self):
		pass
		
	def start(self):
		"""Start the Game Engine"""
		choice = "no"
		while toolkit.find_word("no", choice) or toolkit.find_word("n", choice):
			print "What is your name?"
			name = raw_input("> ")
			print "%s...did I hear you correctly?" % name
			choice = raw_input("> ").lower()
			if choice != "no" and choice != "n" and choice != "yes" and choice != "y":
				print "(muttering)...take it...a yes." 
			
		time.sleep(1)
		print "."
		time.sleep(1)
		print "..."
		time.sleep(1)
		print "......"
		time.sleep(1.5)
		print "\nRUN!!"
		time.sleep(0.6)
		print " "
		time.sleep(0.5)
		print "*hff* *hfff*"
		time.sleep(0.4)
		print "*hffff*"
		time.sleep(0.3)
		print "*hf-"
		print ""
		time.sleep(0.2)
		print ""
		time.sleep(0.3)
		print ""
		time.sleep(1.2)
		print "SNTHHHKK!!"
		time.sleep(0.1)
		
		# TODO: print cray cray things.
		# for i in range(0, 500000):
			# symbols = ["/","-","|","\\","|", "!", "\"", "#", "$", "%", "&", "'", "(" 
			# 			")", "*", "+", ",", "-", ".", ":", ";", "<", "=", ">", "?", 
			# 			"@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
			# print symbols[randint(0, len(symbols) - 1)]
			
		time.sleep(0.5)
		main_character = Hero(name)
		
		
		
		# ----Remove in production.  Just testing items.----
		
		# Items
		autumnHerbs = AutumnHerbs()
		springWater = SpringWater()
		gardenVegetables = GardenVegetables()
		
		# Key Items
		braidedRope = BraidedRope()
		cowlTheScaredCrow = CowlTheScaredCrow()
		spikeMaul = SpikeMaul()
		bundleOfDynamite = BundleOfDynamite()
		malachiteCrystal = MalachiteCrystal()
		
		# Weapons
		woodCuttingAxe = WoodCuttingAxe()
		rustedHook = RustedHook()
		
		# Armors
		animalCarcass = AnimalCarcass()
		scarecrowClothes = ScarecrowClothes()
		bizzleBeakArmor = BizzleBeakArmor()
		
		# Accessories
		rottingBucket = RottingBucket()
		stoneUrn = StoneUrn()
		oldMare = OldMare()
		
		main_character.consumables.append(autumnHerbs)
		main_character.consumables.append(springWater)
		main_character.consumables.append(gardenVegetables)
		
		main_character.key_items.append(braidedRope)
		main_character.key_items.append(cowlTheScaredCrow)
		main_character.key_items.append(spikeMaul)
		main_character.key_items.append(bundleOfDynamite)
		main_character.key_items.append(malachiteCrystal)
		
		main_character.weapons.append(woodCuttingAxe)
		main_character.weapons.append(rustedHook)
		
		main_character.armors.append(animalCarcass)
		main_character.armors.append(scarecrowClothes)
		main_character.armors.append(bizzleBeakArmor)
		
		main_character.accessories.append(rottingBucket)
		main_character.accessories.append(stoneUrn)
		main_character.accessories.append(oldMare)
		
		# ----End removal section----
		
		
		
		main_character.introduction()
		while True:
			command = raw_input("> ").lower()
			print ""
			if toolkit.find_word("menu", command):
				print """
status/stats 
	- Opens your characters stats menu.
	
map
	- Opens the map.
					
move/go/tavel [north/south/east/west]
	- Travel the desired direction.
				
equip [weapon/armor/accessory]
	- Equip a weapon, armor, or an accessory.
			
unequip/remove [weapon/armor/accessory]
	- Un-equip a weapon, armor, or an accessory.
				
use [consumable/key item]
	- Use a consumable item or key item.
					
exit/quit
	- Exit the game.
				"""
			elif toolkit.find_word("status", command) or toolkit.find_word("stats", command):
				main_character.stats()
			elif toolkit.find_word("map", command):
				main_character.map.use()
			elif toolkit.find_word("move", command) or toolkit.find_word("go", command) or toolkit.find_word("travel", command):
				if toolkit.find_word("north", command):
					main_character.map.move("north")
				elif toolkit.find_word("south", command):
					main_character.map.move("south")
				elif toolkit.find_word("east", command):
					main_character.map.move("east")
				elif toolkit.find_word("west", command):
					main_character.map.move("west")
				else:
					print "That is not a direction we can take."
			elif toolkit.find_word("equip", command):
				# ------ Weapons ------
				if toolkit.find_word("wood axe", command) or toolkit.find_word("cutting axe", command) or toolkit.find_word("wood", command) or toolkit.find_word("cutting", command):
					print "Equip the Wood-cutting Axe? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.weapons:
							if isinstance(item, WoodCuttingAxe):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Wood-cutting Axe to equip."
					else:
						pass
				elif toolkit.find_word("rusted", command) or toolkit.find_word("hook", command):
					print "Equip the Rusted Hook? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.weapons:
							if isinstance(item, RustedHook):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Rusted Hook to equip."
					else:
						pass
				elif toolkit.find_word("worn axe", command) or toolkit.find_word("war axe", command) or toolkit.find_word("worn", command) or toolkit.find_word("war", command):
					print "Equip the Worn War Axe? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.weapons:
							if isinstance(item, WornWarAxe):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Worn War Axe to equip."
					else:
						pass
				# ------ Armors ------
				elif toolkit.find_word("animal", command) or toolkit.find_word("carcass", command):
					print "Equip the Animal Carcass? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.armors:
							if isinstance(item, AnimalCarcass):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Animal Carcass to equip."
					else:
						pass
				elif toolkit.find_word("scarecrow", command) or toolkit.find_word("clothes", command):
					print "Equip the Scarecrow Clothes? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.armors:
							if isinstance(item, ScarecrowClothes):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Scarecrow Clothes to equip."
					else:
						pass						
				elif toolkit.find_word("bizzle armor", command) or toolkit.find_word("beak armor", command) or toolkit.find_word("bizzle", command) or toolkit.find_word("beak", command):
					print "Equip the Bizzle Beak Armor? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.armors:
							if isinstance(item, BizzleBeakArmor):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Bizzle Beak Armor to equip."
					else:
						pass	
				# ------ Accessories ------
				elif toolkit.find_word("rotting", command) or toolkit.find_word("bucket", command):
					print "Equip the Rotting Bucket? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.accessories:
							if isinstance(item, RottingBucket):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Rotting Bucket to equip."
					else:
						pass
				elif toolkit.find_word("stone", command) or toolkit.find_word("urn", command):
					print "Equip the Stone Urn? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.accessories:
							if isinstance(item, StoneUrn):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Stone Urn to equip."
					else:
						pass
				elif toolkit.find_word("old", command) or toolkit.find_word("mare", command):
					print "Mount the Old Mare? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.accessories:
							if isinstance(item, OldMare):
								found_item = True
								item.equip(main_character)
						if not found_item:
							print "You have no Old Mare to ride."
					else:
						pass
				else:
					print "That is not something we can equip."
			elif toolkit.find_word("unequip", command) or toolkit.find_word("remove", command):
				# ------ Weapons ------
				if toolkit.find_word("wood axe", command) or toolkit.find_word("cuttin axe", command) or toolkit.find_word("wood", command) or toolkit.find_word("cuttin", command):
					print "Unequip the Wood-cutting Axe? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.weapon, WoodCuttingAxe):
							item.unequip(main_character)
						else:
							print "You have no Wood-cutting Axe to unequip."
					else:
						pass
				elif toolkit.find_word("rusted", command) or toolkit.find_word("hook", command):
					print "Unequip the Rusted Hook? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.weapon, RustedHook):
							item.unequip(main_character)
						else:
							print "You have no Rusted Hook to unequip."
					else:
						pass
				elif toolkit.find_word("worn axe", command) or toolkit.find_word("war axe", command) or toolkit.find_word("worn", command) or toolkit.find_word("war", command):
					print "Unequip the Worn War Axe? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", command) or toolkit.find_word("y", command):
						if isinstance(main_character.weapon, WornWarAxe):
							item.unequip(main_character)
						else:
							print "You have no Worn War Axe to unequip."
					else:
						pass
				# ------ Armors ------
				elif toolkit.find_word("animal", command) or toolkit.find_word("carcass", command):
					print "Unequip the Animal Carcass? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.armor, AnimalCarcass):
							item.unequip(main_character)
						else:
							print "You have no Animal Carcass to unequip."
					else:
						pass
				elif toolkit.find_word("scarecrow", command) or toolkit.find_word("clothes", command):
					print "Unequip the Scarecrow Clothes? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.armor, ScarecrowClothes):
							item.unequip(main_character)
						else:
							print "You have no Scarecrow Clothes to unequip."
					else:
						pass
				elif toolkit.find_word("bizzle armor", command) or toolkit.find_word("beak armor", command) or toolkit.find_word("bizzle", command) or toolkit.find_word("beak", command):
					print "Unequip the Bizzle Beak Armor? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.armor, BizzleBeakArmor):
							item.unequip(main_character)
						else:
							print "You have no Bizzle Beak Armor to unequip."
					else:
						pass
				# ------ Accessories ------
				elif toolkit.find_word("rotting", command) or toolkit.find_word("bucket", command):
					print "Unequip the Rotting Bucket? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.accessory, RottingBucket):
							item.unequip(main_character)
						else:
							print "You have no Rotting Bucket to unequip."
					else:
						pass
				elif toolkit.find_word("stone", command) or toolkit.find_word("urn", command):
					print "Unequip the Stone Urn? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.accessory, StoneUrn):
							item.unequip(main_character)
						else:
							print "You have no Stone Urn to unequip."
					else:
						pass
				elif toolkit.find_word("old", command) or toolkit.find_word("mare", command):
					print "Get off the Old Mare? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						if isinstance(main_character.accessory, OldMare):
							item.unequip(main_character)
						else:
							print "You have no Old Mare to unmount."
					else:
						pass
				else:
					print "That is not something we can unequip."
			elif toolkit.find_word("use", command):
				# ------ Consumable Items ------
				if toolkit.find_word("autumn", command) or toolkit.find_word("herbs", command):
					print "Use Autumn Herbs? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.consumables:
							if isinstance(item, AutumnHerbs):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Autumn Herbs to use."
					else:
						pass
				elif toolkit.find_word("spring", command) or toolkit.find_word("water", command):
					print "Use Spring Water? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.consumables:
							if isinstance(item, SpringWater):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Spring Water to use."
					else:
						pass
				elif toolkit.find_word("garden", command) or toolkit.find_word("vegetables", command):
					print "Use Garden Vegetables? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.consumables:
							if isinstance(item, GardenVegetables):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Garden Vegetables to use."
					else:
						pass
				# ------ Key Items ------
				elif toolkit.find_word("braided", command) or toolkit.find_word("rope", command):
					print "Use Braided Rope? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, BraidedRope):
								found_item = True
								item.use()
						if not found_item:
							print "You have no BraidedRope to use."
					else:
						pass
				elif toolkit.find_word("cowl", command) or toolkit.find_word("scared", command) or toolkit.find_word("crow", command):
					print "Use Cowl the Scared Crow? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, CowlTheScaredCrow):
								found_item = True
								item.use()
						if not found_item:
							print "You have no Cowl the Scared Crow to use."
					else:
						pass
				elif toolkit.find_word("bundle", command) or toolkit.find_word("dynamite", command):
					print "Use Bundle of Dynamite? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, BundleOfDynamite):
								found_item = True
								item.use()
						if not found_item:
							print "You have no Bundle of Dynamite to use."
					else:
						pass
				elif toolkit.find_word("malachite", command) or toolkit.find_word("crystal", command):
					print "Use Malachite Crystal? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, MalachiteCrystal):
								found_item = True
								item.use()
						if not found_item:
							print "You have no Malachite Crystal to use."
					else:
						pass
				elif toolkit.find_word("spike", command) or toolkit.find_word("maul", command):
					print "Use Spike Maul? "
					choice = raw_input().lower()
					if toolkit.find_word("yes", choice) or toolkit.find_word("y", choice):
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, SpikeMaul):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Spike Maul to use."
					else:
						pass
				else:
					print "That is not something we can use."
			elif toolkit.find_word("exit", command) or toolkit.find_word("quit", command):
				main_character.die()
			else:
				print "Your voice falls on deaf ears."
		
	def stop(self):
		"""Stop the Game Engine"""
		print "Finish implementing this..."
		


## -------------------------Tests below-------------------------

game = Engine()
game.start()
game.stop()

## -------------------------End Tests-------------------------