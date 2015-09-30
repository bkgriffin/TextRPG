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
import time
from character import *
from weapon import *
from armor import *
from item import *

class Engine(object):
	"""Game Engine"""
	def __init__(self):
		pass
		
	def start(self):
		"""Start the Game Engine"""
		choice = "no"
		while choice == "no" or choice == "n":
			print "What is your name?"
			name = raw_input("> ")
			print "%s...did I hear you correctly?" % name
			choice = raw_input("> ").lower()
		print "..."
		time.sleep(1)
		print "......"
		time.sleep(1)
		main_character = Hero(name)
		
		# Remove in production.  Just testing items.
		
		autumnHerbs = AutumnHerbs()
		woodCuttingAxe = WoodCuttingAxe()
		rustedHook = RustedHook()
		spikeMaul = SpikeMaul()
		
		main_character.consumables.append(autumnHerbs)
		main_character.weapons.append(woodCuttingAxe)
		main_character.weapons.append(rustedHook)
		main_character.key_items.append(spikeMaul)
		
		# End removal section
		
		main_character.introduction()
		while True:
			command = raw_input("> ").lower()
			print ""
			if command == "menu":
				print """
status/stats 
	- Opens your characters stats menu.
	
map
	- Opens the map.
					
move/go/tavel [north/south/east/west]
	- Travel the desired direction.
				
equip [weapon/armor/accessory]
	- Equip a weapon, armor, or an accessory.
			
remove/unequip [weapon/armor/accessory]
	- Un-equip a weapon, armor, or an accessory.
				
use [consumable/key item]
	- Use a consumable item or key item.
					
exit/quit
	- Exit the game.
				"""
			elif command == "status" or command == "stats":
				main_character.stats()
			elif command == "map":
				main_character.map.use()
			elif "move" in command or "go" in command or "travel" in command:
				if "north" in command:
					main_character.map.move("north")
				elif "south" in command:
					main_character.map.move("south")
				elif "east" in command:
					main_character.map.move("east")
				elif "west" in command:
					main_character.map.move("west")
				else:
					print "That is not a direction we can take."
			elif "equip" in command:
				print "Finish implementing this section..."
				if "" in command:
					main_character.equip("")
				else:
					print "That is not something we can equip."
			elif "remove" in command or "unequip" in command:
				print "Finish implementing this section..."
				if "" in command:
					main_character.remove("")
				else:
					print "That is not something we can remove."
			elif "use" in command:
				if "autumn" in command or "herbs" in command:
					print "Use Autumn Herbs? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.consumables:
							if isinstance(item, AutumnHerbs):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Autumn Herbs to use."
					else:
						pass
				elif "spring" in command or "water" in command:
					print "Use Spring Water? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.consumables:
							if isinstance(item, SpringWater):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Spring Water to use."
					else:
						pass
				elif "garden" in command or "vegetables" in command:
					print "Use Garden Vegetables? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.consumables:
							if isinstance(item, GardenVegetables):
								found_item = True
								item.use(main_character)
						if not found_item:
							print "You have no Garden Vegetables to use."
					else:
						pass
				elif "braided" in command or "rope" in command:
					print "Use Braided Rope? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, BraidedRope):
								found_item = True
								item.use()
						if not found_item:
							print "You have no BraidedRope to use."
					else:
						pass
				elif "cowl" in command or "scared" in command or "crow" in command:
					print "Use Cowl the Scared Crow? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, CowlTheScaredCrow):
								found_item = True
								item.use()
						if not found_item:
							print "You have no Cowl the Scared Crow to use."
					else:
						pass
				elif "bundle" in command or "dynamite" in command:
					print "Use Bundle of Dynamite? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, BundleOfDynamite):
								found_item = True
								item.use()
						if not found_item:
							print "You have no Bundle of Dynamite to use."
					else:
						pass
				elif "malachite" in command or "crystal" in command:
					print "Use Malachite Crystal? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
						found_item = False
						for item in main_character.key_items:
							if isinstance(item, MalachiteCrystal):
								found_item = True
								item.use()
						if not found_item:
							print "You have no Malachite Crystal to use."
					else:
						pass
				elif "spike" in command or "maul" in command:
					print "Use Spike Maul? "
					choice = raw_input().lower()
					if choice == "yes" or choice == "y":
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
			elif command == "exit" or command == "quit":
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