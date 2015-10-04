#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Armor class~
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
from character import Character, Hero


class Armor(object):
	"""Armor"""
	def __init__(self, name, description, quantity, 
				max_hp, max_mp, strength, defense, speed, movement):
		self.name = name
		self.description = description
		self.quantity = quantity
		self.max_hp = max_hp
		self.max_mp = max_mp
		self.strength = strength
		self.defense = defense
		self.speed = speed
		self.movement = movement
		
	def stats(self):
		"""Prints the Armor's stats to the screen."""
		print """-*-^`|/`^\|/^`-* %s *-^`\|/`^\|^`-*-	\n
  Description: 
  \t%s
  Quantity: 
  \t%d\n
  Effect:
  \tMax HP: %s
  \tMax MP: %s
  \tStrength: %s
  \tDefense: %s
  \tSpeed: %s
  \tMovement: %s\n
		""" %  (self.name, self.description, self.quantity, self.max_hp, 
				self.max_mp, self.strength, self.defense, self.speed, 
				self.movement)
		
	def add(self, quantity):
		"""Add to the quantity of Armor"""
		self.quantity += quantity
		
	def delete(self, quantity):
		"""Delete from the quantity of Armor"""
		if(quantity==-1 or self.quantity < quantity):
			self.quantity = 0
		else:
			self.quantity -= quantity
			
	def activate(self, character):
		"""Activate the Armor's effects."""
		if isinstance(character, Hero):
			if self.max_hp[0] == '+':
				character.max_hp = character.max_hp + int(self.max_hp[1:])
				if character.hp > character.max_hp:
					character.hp = character.max_hp
			elif self.max_hp[0] == '-':
				character.max_hp = character.max_hp - int(self.max_hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.max_mp[0] == '+':
				character.max_mp = character.max_mp + int(self.max_mp[1:])
				if character.mp > character.max_mp:
					character.mp = character.max_mp
			elif self.max_mp[0] == '-':
				character.max_mp = character.max_mp - int(self.max_mp[1:])
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
			if self.max_hp[0] == '+':
				character.max_hp = character.max_hp + int(self.max_hp[1:])
				if character.hp > character.max_hp:
					character.hp = character.max_hp
			elif self.max_hp[0] == '-':
				character.max_hp = character.max_hp - int(self.max_hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.max_mp[0] == '+':
				character.max_mp = character.max_mp + int(self.max_mp[1:])
				if character.mp > character.max_mp:
					character.mp = character.max_mp
			elif self.max_mp[0] == '-':
				character.max_mp = character.max_mp - int(self.max_mp[1:])
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
	
	def deactivate(self, character):
		"""Deactivate the Armor's effects."""
		if isinstance(character, Hero):
			if self.max_hp[0] == '-':
				character.max_hp = character.max_hp + int(self.max_hp[1:])
				if character.hp > character.max_hp:
					character.hp = character.max_hp
			elif self.max_hp[0] == '+':
				character.max_hp = character.max_hp - int(self.max_hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.max_mp[0] == '-':
				character.max_mp = character.max_mp + int(self.max_mp[1:])
				if character.mp > character.max_mp:
					character.mp = character.max_mp
			elif self.max_mp[0] == '+':
				character.max_mp = character.max_mp - int(self.max_mp[1:])
				if character.mp < 0:
					character.mp = 0
		
			if self.strength[0] == '-':
				character.strength = character.strength + int(self.strength[1:])
			elif self.strength[0] == '+':
				character.strength = character.strength - int(self.strength[1:])
				if character.strength < 0:
					character.strength = 0
				
			if self.defense[0] == '-':
				character.defense = character.defense + int(self.defense[1:])
			elif self.defense[0] == '+':
				character.defense = character.defense - int(self.defense[1:])
				if character.defense < 0:
					character.defense = 0
				
			if self.speed[0] == '-':
				character.speed = character.speed + int(self.speed[1:])
			elif self.speed[0] == '+':
				character.speed = character.speed - int(self.speed[1:])
				if character.speed < 0:
					character.speed = 0
				
			if self.movement[0] == '-':
				character.movement = character.movement + int(self.movement[1:])
			elif self.movement[0] == '+':
				character.movement = character.movement - int(self.movement[1:])
				if character.movement <= 0:
					character.movement = 1
			
		elif isinstance(character, Enemy):
			if self.max_hp[0] == '-':
				character.max_hp = character.max_hp + int(self.max_hp[1:])
				if character.hp > character.max_hp:
					character.hp = character.max_hp
			elif self.max_hp[0] == '+':
				character.max_hp = character.max_hp - int(self.max_hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.max_mp[0] == '-':
				character.max_mp = character.max_mp + int(self.max_mp[1:])
				if character.mp > character.max_mp:
					character.mp = character.max_mp
			elif self.max_mp[0] == '+':
				character.max_mp = character.max_mp - int(self.max_mp[1:])
				if character.mp < 0:
					character.mp = 0
		
			if self.strength[0] == '-':
				character.strength = character.strength + int(self.strength[1:])
			elif self.strength[0] == '+':
				character.strength = character.strength - int(self.strength[1:])
				if character.strength < 0:
					character.strength = 0
				
			if self.defense[0] == '-':
				character.defense = character.defense + int(self.defense[1:])
			elif self.defense[0] == '+':
				character.defense = character.defense - int(self.defense[1:])
				if character.defense < 0:
					character.defense = 0
				
			if self.speed[0] == '-':
				character.speed = character.speed + int(self.speed[1:])
			elif self.speed[0] == '+':
				character.speed = character.speed - int(self.speed[1:])
				if character.speed < 0:
					character.speed = 0
					
		else:
			print "%s doesn't work that way." % self.name 
			
	def equip(self, character):
		"""Equip Armor."""
		# Unequip old item
		if character.armor != None:
			character.armors.append(character.armor)	
				
		# Equip new item	
		character.armor = self	
		self.activate(character)						
				
		# Remove equipped item from inventory
		if self in character.armors:
			character.armors.remove(self)	
			
	def unequip(self, character):
		"""Unequip Armor."""
		# Unequip old item
		if character.armor != None:
			character.armors.append(character.armor)	
				
			# Equip new item
			character.armor.deactivate(character)
			character.armor = None				

class AnimalCarcass(Armor):
	"""Animal Carcass."""
	def __init__(self):
		super(AnimalCarcass, self).__init__("Animal Carcass", 
				"The smell...", 1, "0", "-1", "0", "+1", "0", "0")
				
class ScarecrowClothes(Armor):
	"""Scarecrow Clothes."""
	def __init__(self):
		super(ScarecrowClothes, self).__init__("Scarecrow Clothes", 
				"Quite fashionable, for a stick and some hay.", 1, 
				"0", "0", "0", "+1", "0", "0")
				
class BizzleBeakArmor(Armor):
	"""Bizzle Beak Armor."""
	def __init__(self):
		super(BizzleBeakArmor, self).__init__("Bizzle Beak Armor", 
				"A murder of obsidian beaks and black feathers.", 1, 
				"+5", "0", "+2", "0", "0", "0")
		
		
		
		
## -------------------------Tests below-------------------------

animalCarcass = AnimalCarcass()
animalCarcass.stats()
animalCarcass.add(3)
animalCarcass.stats()
animalCarcass.delete(1)
animalCarcass.stats()

scarecrowClothes = ScarecrowClothes()
scarecrowClothes.stats()
scarecrowClothes.add(3)
scarecrowClothes.stats()
scarecrowClothes.delete(1)
scarecrowClothes.stats()

bizzleBeakArmor = BizzleBeakArmor()
bizzleBeakArmor.stats()
bizzleBeakArmor.add(3)
bizzleBeakArmor.stats()
bizzleBeakArmor.delete(1)
bizzleBeakArmor.stats()

newguy = Hero("Mememe")
newguy.stats()
newguy.armors.append(animalCarcass)
newguy.armors.append(scarecrowClothes)
newguy.armors.append(bizzleBeakArmor)

animalCarcass.equip(newguy)
newguy.stats()
animalCarcass.unequip(newguy)
newguy.stats()

scarecrowClothes.equip(newguy)
newguy.stats()
scarecrowClothes.unequip(newguy)
newguy.stats()

bizzleBeakArmor.unequip(newguy)
newguy.stats()
bizzleBeakArmor.unequip(newguy)
newguy.stats()
## -------------------------End Tests-------------------------