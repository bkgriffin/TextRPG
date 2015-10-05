#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Item class~
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

class Item(object):
	"""Item"""
	def __init__(self, name, description, quantity):
		self.name = name
		self.description = description
		self.quantity = quantity
	
	def stats(self):
		print "This method is not yet coded. Subclass it and implement stats()."


class KeyItem(Item):
	"""Key Item"""
	def __init__(self, name, description):
		super(KeyItem, self).__init__(name, description, 1)
		self.effect = "???"
		
	def stats(self):
		"""Prints the Key Items's stats to the screen."""
		print """-*-\|/|\|/|-* %s *-|\|/|\|/-*-	\n
  Description: 
  \t%s
  Quantity: 
  \t%d\n
  Effect: 
  \t%s\n
		""" %  (self.name, self.description, self.quantity, self.effect)
	
	def unlock_effect(self):
		print "This method is not yet coded. Subclass it and implement unlock_effect()."
		
	def use(self):
		"""Use the item."""
		if (self.effect == "???"):
			print self.effect
			print "......"
			self.unlock_effect()
			print self.effect
		else:
			print self.effect
		
class BraidedRope(KeyItem):
	"""Braided Rope"""
	def __init__(self):
		super(BraidedRope, self).__init__("Braided Rope", "Braided rope from the well.")
		
	def unlock_effect(self):
		"""Unlock the first time a Hero uses this Key Item."""
		self.effect = "The braided rope is...finish implementing this"
		
	def use(self):
		"""Use the item."""
		super(BraidedRope, self).use()
		print "Braided Rope: Finish implementing this..."
		
class CowlTheScaredCrow(KeyItem):
	"""Cowl, the Scared Crow"""
	def __init__(self):
		super(CowlTheScaredCrow, self).__init__("Cowl, the Scared Crow", 
			"A creature sheltered by the scarecrow.")
		
	def unlock_effect(self):
		"""Unlock the first time a Hero uses this Key Item."""
		self.effect = """Cowl, the Scared Crow breaks the wind around your shoulder, 
climbing upwards.  He steadies himself, and examines 
the lay of the land..."""
							
	def use(self):
		"""Use the item."""
		super(CowlTheScaredCrow, self).use()
		self.map()
		
	def map(self):
		"""Opens the world map."""
		print """ \n\n
		|---------------Valley of Ithmas----------------|
		|-----------------------------------------------|
		|                                               |
		|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
                |-----------------------------------------------|
              F |     |     |     |     |     |  !  |     |     |
                |-----------------------------------------------|
              E |     |     |     |     |     |     |     |     |
                |-----------------------------------------------|	
              D |     |     |     |     |     |     |     |     |
                |-----------------------------------------------|
              C |     |     |     |     |     |     |     |     |
                |-----------------------------------------------|
              B |     |     |     |     |     |     |     |     |
                |-----------------------------------------------|
              A |     |     |     |  *  |     |     |     |     |
                |-----------------------------------------------|
		|-----------------------------------------------| 
		     * YOU ARE HERE                ! GOAL\n\n"""
		     
class BundleOfDynamite(KeyItem):
	"""Bundle of Dynamite"""
	def __init__(self):
		super(BundleOfDynamite, self).__init__("Bundle of Dynamite", 
			"A bundle of dynamite, recovered from the rail cart.")
		
	def unlock_effect(self):
		"""Unlock the first time a Hero uses this Key Item."""
		self.effect = """The bundle of dynamite hisses as the fuse curls
upon itself in an ember lit haze of smoke."""
							
	def use(self):
		"""Use the item."""
		super(BundleOfDynamite, self).use()
		print "Bundle of Dynamite: Finish implementing this..."
		
class MalachiteCrystal(KeyItem):
	"""Malachite Crystal"""
	def __init__(self):
		super(MalachiteCrystal, self).__init__("Malachite Crystal", 
			"A crystal of Malachite, found at the bottom of the well.")
		
	def unlock_effect(self):
		"""Unlock the first time a Hero uses this Key Item."""
		self.effect = """The malachite shines in the sunlight."""
							
	def use(self):
		"""Use the item."""
		super(MalachiteCrystal, self).use()
		self.compass()
		
	def compass(self):
		print "--------This points somewhere--------"
		
class SpikeMaul(KeyItem):
	"""Spike Maul"""
	def __init__(self):
		super(SpikeMaul, self).__init__("Spike Maul", 
			"An old spike maul, obtained from the old mine.")
		
	def unlock_effect(self):
		"""Unlock the first time a Hero uses this Key Item."""
		self.effect = """You turn the spike maul over in your hands..."""
				
	def use(self, character):
		"""Use the item."""
		super(SpikeMaul, self).use()
		isWoodCuttingAxePresent = False
		isHookPresent = False
		for weapon in character.weapons:
			if isinstance(weapon, WoodCuttingAxe):
				isWoodCuttingAxePresent = True
			elif isinstance(weapon, RustedHook):
				isRustedHookPresent = True
		answer = raw_input("Would you like to combine your Wood-cutting Axe and Rusted Hook? ").lower()
		if answer == "yes" or answer == "y":
			time.sleep(1)
			print "*DINK*"
			time.sleep(1)
			print "*DINK* *DINK*"
			time.sleep(1)
			print "*DINK* *DINK* *DINK!*"
			self.craft(character)
			print "You crafted the Worn War Axe!!"
		else:
			print "Well, that's really unfortunate..."
		
	def craft(self, character):
		"""Craft an item for the Hero.
			- Worn War Axe = Wood-cutting Axe + Rusted Hook """
		for weapon in character.weapons:
			if isinstance(weapon, WoodCuttingAxe):
				character.weapons.remove(weapon)
		for weapon in character.weapons:
			if isinstance(weapon, RustedHook):
				character.weapons.remove(weapon)
		wornWarAxe = WornWarAxe()
		character.weapons.append(wornWarAxe)
		
class ConsumableItem(Item):
	"""Consumable Item"""
	def __init__(self, name, description, hp, mp, strength, defense, speed, movement):
		super(ConsumableItem, self).__init__(name, description, 1)
		self.hp = hp
		self.mp = mp
		self.strength = strength
		self.defense = defense
		self.speed = speed
		self.movement = movement
		
	def stats(self):
		"""Prints the Key Items's stats to the screen."""
		print """-*-\_/^\_/|-* %s *-|\_/^\_/-*-\n
  Description: 
  \t%s
  Quantity: 
  \t%d\n
  Effect:
  \tHP: %s
  \tMP: %s
  \tStrength: %s
  \tDefense: %s
  \tSpeed: %s
  \tMovement: %s\n
		""" %  (self.name, self.description, self.quantity, self.hp, self.mp, 
				self.strength, self.defense, self.speed, self.movement)
			
	def add(self, quantity):
		"""Add to the quantity of an Item"""
		self.quantity += quantity
		
	def delete(self, quantity):
		"""Delete from the quantity of an Item"""
		if(quantity==-1 or self.quantity < quantity):
			self.quantity = 0
		else:
			self.quantity -= quantity
			
	def use(self, character):
		"""Use the item."""
		if isinstance(character, Hero):
			if self.hp[0] == '+':
				character.hp = character.hp + int(self.hp[1:])
				if character.hp > character.max_hp:
					character.hp = character.max_hp
			elif self.hp[0] == '-':
				character.hp = character.hp - int(self.hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.mp[0] == '+' and character.mp < character.max_mp:
				character.mp = character.mp + int(self.mp[1:])
				if character.mp > character.max_mp:
					character.mp = character.max_mp
			elif self.mp[0] == '-':
				character.mp = character.mp - int(self.mp[1:])
				if character.mp < 0:
					character.mp = 0
		
			if self.strength[0] == '+':
				character.strength = character.strength + int(self.strength[1:])
			elif self.strength[0] == '-':
				character.strength = character.strength - int(self.strength[1:])
				if character.strength < 0:
					character.strength = 0
				
			if self.defense[0] == '+':
				character.defense = character.defense + int(self.defense[1:])
			elif self.defense[0] == '-':
				character.defense = character.defense - int(self.defense[1:])
				if character.defense < 0:
					character.defense = 0
				
			if self.speed[0] == '+':
				character.speed = character.speed + int(self.speed[1:])
			elif self.speed[0] == '-':
				character.speed = character.speed - int(self.speed[1:])
				if character.speed < 0:
					character.speed = 0
				
			if self.movement[0] == '+':
				character.movement = character.movement + int(self.movement[1:])
			elif self.movement[0] == '-':
				character.movement = character.movement - int(self.movement[1:])
				if character.movement <= 0:
					character.movement = 1
			
		elif isinstance(character, Enemy):
			if self.hp[0] == '+':
				character.hp = character.hp + int(self.hp[1:])
				if character.hp > character.max_hp:
					character.hp = character.max_hp
			elif self.hp[0] == '-':
				character.hp = character.hp - int(self.hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.mp[0] == '+' and character.mp < character.max_mp:
				character.mp = character.mp + int(self.mp[1:])
				if character.mp > character.max_mp:
					character.mp = character.max_mp
			elif self.mp[0] == '-':
				character.mp = character.mp - int(self.mp[1:])
				if character.mp < 0:
					character.mp = 0
		
			if self.strength[0] == '+':
				character.strength = character.strength + int(self.strength[1:])
			elif self.strength[0] == '-':
				character.strength = character.strength - int(self.strength[1:])
				if character.strength < 0:
					character.strength = 0
				
			if self.defense[0] == '+':
				character.defense = character.defense + int(self.defense[1:])
			elif self.defense[0] == '-':
				character.defense = character.defense - int(self.defense[1:])
				if character.defense < 0:
					character.defense = 0
				
			if self.speed[0] == '+':
				character.speed = character.speed + int(self.speed[1:])
			elif self.speed[0] == '-':
				character.speed = character.speed - int(self.speed[1:])
				if character.speed < 0:
					character.speed = 0
					
		else:
			print "%s doesn't work that way." % self.name 
		
class AutumnHerbs(ConsumableItem):
	"""Autumn Herbs"""
	def __init__(self):
		super(AutumnHerbs, self).__init__("Autumn Herbs", 
			"Herbs, crisp from the Autumn air.", "+5", "0", "0", "0", "0", "0")
			
	def use(self, character):
		"""Use the item."""
		super(AutumnHerbs, self).use(character)
		print "Autumn Herbs: Finish implementing this..."
			
class SpringWater(ConsumableItem):
	"""Spring Water"""
	def __init__(self):
		super(SpringWater, self).__init__("Spring Water", 
			"Water, scooped from a natural spring.", "0", "+5", "0", "0", "0", "0")
			
	def use(self, character):
		"""Use the item."""
		super(SpringWater, self).use(character)
		print "Spring Water: Finish implementing this..."
			
class GardenVegetables(ConsumableItem):
	"""Garden Vegetables"""
	def __init__(self):
		super(GardenVegetables, self).__init__("Garden Vegetables", 
			"Garden vegetables, pulled from the Earth.", 
			"0", "0", "0", "0", "0", "0")
			
	def use(self, character):
		"""Use the item."""
		super(GardenVegetables, self).use(character)
		print "They don't seem to have any effect on you..."
		
## -------------------------Tests below-------------------------

braided_rope = BraidedRope()
braided_rope.stats()
braided_rope.unlock_effect()
braided_rope.stats()

autumn_herbs = AutumnHerbs()
autumn_herbs.add(2)
autumn_herbs.stats()
autumn_herbs.delete(-1)
autumn_herbs.stats()
newguy = Hero("j")
newguy.stats()
autumn_herbs.use(newguy)
newguy.stats()

spring_water = SpringWater()
spring_water.add(2)
spring_water.stats()
spring_water.delete(-1)
spring_water.stats()
newguy = Hero("j")
newguy.stats()
spring_water.use(newguy)
newguy.stats()

garden_vegetables = GardenVegetables()
garden_vegetables.add(2)
garden_vegetables.stats()
garden_vegetables.delete(-1)
garden_vegetables.stats()
newguy = Hero("j")
newguy.stats()
garden_vegetables.use(newguy)
newguy.stats()

newdude = NPC("dude", "he has a plan.")
garden_vegetables.use(newdude)

dire_wolf = DireWolf()
dire_wolf.stats()
autumn_herbs.use(dire_wolf)
dire_wolf.stats()

cowl = CowlTheScaredCrow()
print "Use it the first time"
cowl.use()
print "Use it the second time"
cowl.use()

bundleOfDynamite = BundleOfDynamite()
bundleOfDynamite.use()
bundleOfDynamite.use()

malachiteCrystal = MalachiteCrystal()
malachiteCrystal.use()
malachiteCrystal.use()
## -------------------------End Tests-------------------------