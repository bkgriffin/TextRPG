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
from random import randint
from character import Character, Hero, Enemy, NPC, DireWolf


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
		
class BraidedRope(KeyItem):
	"""Braided Rope"""
	def __init__(self):
		super(BraidedRope, self).__init__("Braided Rope", "Braided rope from the well.")
		
	def unlock_effect(self):
		"""Unlock the first time a Hero uses this Key Item."""
		self.effect = "The braided rope is...finish implementing this"
		

		
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
			
class SpringWater(ConsumableItem):
	"""Spring Water"""
	def __init__(self):
		super(SpringWater, self).__init__("Spring Water", 
			"Water, scooped from a natural spring.", "0", "+5", "0", "0", "0", "0")
			
class GardenVegetables(ConsumableItem):
	"""Garden Vegetables"""
	def __init__(self):
		super(GardenVegetables, self).__init__("Garden Vegetables", 
			"Garden vegetables, pulled from the Earth.", 
			"0", "0", "0", "0", "0", "0")
		
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
## -------------------------End Tests-------------------------