#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Accessory class~
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


class Accessory(object):
	"""Accessory"""
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
		"""Prints the Accessory's stats to the screen."""
		print """-*-^~|/~^\|/^~-* %s *-^~\|/~^\|^~-*-	\n
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
		"""Add to the quantity of an Accessory"""
		self.quantity += quantity
		
	def delete(self, quantity):
		"""Delete from the quantity of an Accessory"""
		if(quantity==-1 or self.quantity < quantity):
			self.quantity = 0
		else:
			self.quantity -= quantity
			
	def activate(self, character):
		"""Activate the accessory's effects."""
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
		"""Deactivate the accessory's effects."""
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
			elif self.max_hp[0] == '+':
				character.max_hp = character.max_hp - int(self.max_hp[1:])
				if character.hp <= 0:
					character.die()
			
			if self.max_mp[0] == '-' and character.mp < character.max_mp:
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
		"""Equip an Accessory."""
		# Unequip old item
		if character.accessory != None:
			character.accessories.append(character.accessory)	
				
		# Equip new item	
		character.accessory = self	
		self.activate(character)						
			
		# Remove equipped item from inventory
		if self in character.accessories:
			character.accessories.remove(self)	
		
	def unequip(self, character):
		"""Unequip an Accessory."""
		# Unequip old item
		if character.accessory != None:
			character.accessories.append(character.accessory)	
			
		# Equip new item
		character.accessory.deactivate(character)
		character.accessory = None	
			
class RottingBucket(Accessory):
	"""Rotting Bucket."""
	def __init__(self):
		super(RottingBucket, self).__init__("Rotting Bucket", 
				"A decayed, rotting wooden bucket.", 1, "0", "+2", "0", "-1", "0", "0")
				
class StoneUrn(Accessory):
	"""Stone Urn."""
	def __init__(self):
		super(StoneUrn, self).__init__("Stone Urn", 
				"A marble, stone urn.  The rim glimmers in the moonlight.", 1, 
				"0", "+5", "0", "0", "0", "0")
				
class OldMare(Accessory):
	"""Old Mare."""
	def __init__(self):
		super(OldMare, self).__init__("Old Mare", 
				"An old mare, found in the back of the barn.", 1, 
				"0", "0", "0", "0", "0", "+2")
		
		
		
		
## -------------------------Tests below-------------------------

rottingBucket = RottingBucket()
rottingBucket.stats()
rottingBucket.add(3)
rottingBucket.stats()
rottingBucket.delete(1)
rottingBucket.stats()

stoneUrn = StoneUrn()
stoneUrn.stats()
stoneUrn.add(3)
stoneUrn.stats()
stoneUrn.delete(1)
stoneUrn.stats()

oldMare = OldMare()
oldMare.stats()
oldMare.add(3)
oldMare.stats()
oldMare.delete(1)
oldMare.stats()

newguy = Hero("Mememe")
newguy.stats()
newguy.accessories.append(rottingBucket)
newguy.accessories.append(stoneUrn)
newguy.accessories.append(oldMare)

rottingBucket.equip(newguy)
newguy.stats()
rottingBucket.unequip(newguy)
newguy.stats()

stoneUrn.equip(newguy)
newguy.stats()
stoneUrn.unequip(newguy)
newguy.stats()

oldMare.equip(newguy)
newguy.stats()
oldMare.unequip(newguy)
newguy.stats()
## -------------------------End Tests-------------------------