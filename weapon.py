#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Weapon class~
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


class Weapon(object):
	"""Weapon"""
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
		"""Prints the Weapons's stats to the screen."""
		print """-*-^^|/^^\|/^^-* %s *-^^\|/^^\|^^-*-	\n
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
		"""Add to the quantity of a Weapon"""
		self.quantity += quantity
		
	def delete(self, quantity):
		"""Delete from the quantity of a Weapon"""
		if(quantity==-1 or self.quantity < quantity):
			self.quantity = 0
		else:
			self.quantity -= quantity
			
	def activate(self, character):
		"""Activate the weapon's effects."""
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
		"""Deactivate the weapon's effects."""
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
		"""Equip a Weapon."""
		# Unequip old item
		if character.weapon != None:
			character.weapons.append(character.weapon)	
			
		# Equip new item	
		character.weapon = self	
		self.activate(character)						
		
		# Remove equipped item from inventory
		if self in character.weapons:
			character.weapons.remove(self)	
			
	def remove(self, character):
		"""Remove a Weapon."""
		# Unequip old item
		if character.weapon != None:
			character.weapons.append(character.weapon)	
			
			# Equip new item
			character.weapon.deactivate(character)
			character.weapon = 	None

class WoodCuttingAxe(Weapon):
	"""Wood-cutting Axe."""
	def __init__(self):
		super(WoodCuttingAxe, self).__init__("Wood-cutting Axe", 
				"An old, weathered axe found in a stump", 1, "0", "0", "+2", "0", "0", "0")
				
class RustedHook(Weapon):
	"""Rusted Hook."""
	def __init__(self):
		super(RustedHook, self).__init__("Rusted Hook", 
				"A flattened, rusted hook, found holding a bucket in the well.", 1, 
				"0", "0", "+3", "-1", "0", "0")
				
class WornWarAxe(Weapon):
	"""Worn War Axe."""
	def __init__(self):
		super(WornWarAxe, self).__init__("Worn War Axe", 
				"An axe fashioned from a wood-cutting axe and a rusted hook.", 1, 
				"0", "0", "+3", "+2", "0", "0")
		
		
		
## -------------------------Tests below-------------------------

woodCuttingAxe = WoodCuttingAxe()
woodCuttingAxe.stats()
woodCuttingAxe.add(3)
woodCuttingAxe.stats()
woodCuttingAxe.delete(1)
woodCuttingAxe.stats()

rustedHook = RustedHook()
rustedHook.stats()
rustedHook.add(3)
rustedHook.stats()
rustedHook.delete(1)
rustedHook.stats()

wornWarAxe = WornWarAxe()
wornWarAxe.stats()
wornWarAxe.add(3)
wornWarAxe.stats()
wornWarAxe.delete(1)
wornWarAxe.stats()

newguy = Hero("Mememe")
newguy.stats()
newguy.weapons.append(woodCuttingAxe)
newguy.weapons.append(rustedHook)
newguy.weapons.append(wornWarAxe)

woodCuttingAxe.equip(newguy)
newguy.stats()
woodCuttingAxe.remove(newguy)
newguy.stats()

rustedHook.equip(newguy)
newguy.stats()
rustedHook.remove(newguy)
newguy.stats()

wornWarAxe.equip(newguy)
newguy.stats()
wornWarAxe.remove(newguy)
newguy.stats()
## -------------------------End Tests-------------------------