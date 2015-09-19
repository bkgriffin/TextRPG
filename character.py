#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Character class~
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


class Character(object):
	"""Character"""
	def __init__(self, name):
		self.name = name
	
	def stats(self):
		print "This method is not yet configured.  Subclass it and implement stats()."
		exit(1)


class Hero(Character):
	"""The Hero of our Story.  One who ceaselessly slumbers."""
	def __init__(self, name):
		super(Hero, self).__init__(name)
		self.hp = 10
		self.max_hp = 10
		self.mp = 5
		self.max_mp = 5
		self.strength = 2
		self.defense = 1
		self.speed = 1
		self.level = 1
		self.weapon = None
		self.armor = None
		self.accessory = None
		self.key_items = []
		self.consumables = []
		self.movement = 1
		self.experience = 0
		
	def introduction(self):
		"""Introduction"""
		print """
--------------------------------------------------------------------
Hero appears...finish implementing this.
--------------------------------------------------------------------
		"""	
	
	def attack(self, enemy):
		"""
		Attack a Character
		- Damage = Your Strength / (Their Defense * 0.7)
		"""
		if isinstance(enemy, Enemy):
			damage = int(self.strength / (enemy.defense * 0.7))
			print "%s did %d damage to %s!" % (self.name, damage, enemy.name)
			if(enemy.hp > damage):	
				enemy.hp -= damage
			else:
				self.win(enemy.die())
		else:
			print "You cannot attack that."
	
	def defend(self, enemy, attacked=True):
		"""
		Defend against a Character's Attack
		- Damage = Damage / 2
		"""
		if isinstance(enemy, Enemy):
			if attacked:
				original_damage = int(enemy.strength / (self.defense * 0.7))
				damage = int(original_damage / 2)
			else:
				original_damage = 0
				damage = 0
			print "%s defended! %d damage taken." % (self.name, damage)
			if(self.hp > damage):
				self.hp += original_damage	
				self.hp -= damage
			else:
				enemy.win()
				self.die()
		else:
			print "You cannot defend against that."
			
	def flee(self, strength, defense):
		"""
		Flee from a Character encounter
		- Enemy has greater Strength and Defense = 25% chance to flee.
		- Enemy has greater Strength or Defense = 50% chance to flee.
		- Enemy has equal or lesser Strength and/or Defense = 75% to flee.
		"""
		flee = randint(1, 4)
		if (strength > self.strength and defense > self.defense):
			chance_to_flee = [1]
		elif (strength > self.strength or defense > self.defense):
			chance_to_flee = [1, 2]
		else:
			chance_to_flee = [1, 2, 3]	
			
		for chance in chance_to_flee:	
			if chance == flee:
				print "You fled from battle!"
				return True
		print "You couldn't flee from battle!"
		return False
	
	def win(self, experience):
		"""
		Win a battle against an Enemy.
		  +x levels = (total experience gained / 500) - (experience gained before win / 500)
		"""
		current_level = self.experience / 500
		self.experience +=	experience
		new_level = self.experience / 500
		levels_gained = new_level - current_level
		if(levels_gained == 1 and new_level > current_level):
			print "%s gained %d level!!  Maximum HP +%d!  Maximum MP +%d!" % (
					self.name, levels_gained, levels_gained, levels_gained)
			self.level += levels_gained
			self.max_hp += levels_gained
			self.hp = self.max_hp
			self.max_mp += levels_gained
			self.mp = self.max_mp
		else:
			print "%s gained %d levels!!  Maximum HP +%d!  Maximum MP +%d!" % (
					self.name, levels_gained, levels_gained, levels_gained)
			self.level += levels_gained
			self.max_hp += levels_gained
			self.hp = self.max_hp
			self.max_mp += levels_gained
			self.mp = self.max_mp
		
			
	def die(self):
		"""Die"""
		ending = [
			"You died.  It's over.",
			"This must mean something...",
			"So many clicks, so much wasted time.",
			"Well, it's not so bad.",
			"Your future doesn't look so...oh..."
		]
		print ending[randint(0, len(ending)-1)]
		exit(1)
		
	def stats(self):
		"""Prints the Hero's stats to the screen."""
		print """-%s\'s Stats-
  Level: %d
  HP: %d / %d
  MP: %d / %d
  Strength: %d
  Defense: %d
  Speed: %d
  Weapon: %s
  Armor: %s
  Accessory: %s
  Key Items: %s
  Consumables: %s
  Movement: %s
  Experience Gained: %s\n
	""" % (self.name, self.level, self.hp, self.max_hp, self.mp, self.max_mp, 
		self.strength, self.defense, self.speed, self.weapon, self.armor, 
		self.accessory, self.key_items, self.consumables, self.movement, 
		self.experience)
	
	def talk(self, npc):
		"""Talks to the Hero."""
		if isinstance(npc, NPC):
			npc.talk(self)
		else:
			print "Your voice falls on deaf ears."
		
class Enemy(Character):
	"""Enemy Character"""
	def __init__(self, name, hp, max_hp, mp, max_mp, strength, defense, 
					speed, experience):
		super(Enemy, self).__init__(name)
		self.hp = hp
		self.max_hp = max_hp
		self.mp = mp
		self.max_mp = max_mp
		self.strength = strength
		self.defense = defense
		self.speed = speed
		self.experience = experience
		
	def attack(self, character):
		"""
		Attack a Character
		- Damage = Your Strength / (Their Defense * 0.7)
		"""
		if isinstance(character, Hero):
			damage = int(self.strength / (character.defense * 0.7))
			print "%s did %d damage to %s!" % (self.name, damage, character.name)
			if(character.hp > damage):	
				character.hp -= damage
			else:
				self.win()
				character.die()
		else:
			print "%s cannot attack that." % self.name
	
	def defend(self, character, attacked=True):
		"""
		Defend against a Character's Attack
		- Damage = Damage / 2
		"""
		if isinstance(character, Hero):
			if attacked:
				original_damage = int(character.strength / (self.defense * 0.7))
				damage = int(original_damage / 2)
			else:
				original_damage = 0
				damage = 0
			print "%s defended! %d damage taken." % (self.name, damage)
			if(self.hp > damage):
				self.hp += original_damage	
				self.hp -= damage
			else:
				character.win(self.die())
		else:
			print "%s cannot defend against that." % self.name
			
	def die(self):
		"""Die"""
		print "This method is not yet coded. Subclass it and implement die()."
		
	def win(self):
		"""Win a battle against a Character."""
		print "This method is not yet coded. Subclass it and implement win()."
		
	def stats(self):
		"""Prints the Enemy's stats to the screen."""
		print """-%s\'s Stats-
  HP: %d / %d
  MP: %d / %d
  Strength: %d
  Defense: %d
  Speed: %d
  Experience: %s\n
	""" % (self.name, self.hp, self.max_hp, self.mp, self.max_mp, 
			self.strength, self.defense, self.speed, self.experience)
		
class DireWolf(Enemy):
	"""Dire Wolf, Fervor of the Forest"""
	def __init__(self):
		max_hp = randint(4, 7)
		max_mp = randint(1, 2)
		super(DireWolf, self).__init__("Dire Wolf, Fervor of the Forest", 
			max_hp, max_hp, max_mp, max_mp, randint (1, 3), randint(1, 2), 
			randint(1, 2), randint(500, 700))
		
	def introduction(self):
		"""Introduction"""
		print """
--------------------------------------------------------------------
The Dire Wolf appears...finish implementing this.
--------------------------------------------------------------------
		"""
		
	def die(self):
		"""Die"""
		print """
--------------------------------------------------------------------
The Dire Wolf limps backwards, dragging its front right paw in a 
slow retreat against the long blades of the grass.  A tatter of 
blood-soaked pelt leaves a trail of iron in the dew of the forest
floor.  Slowly, without blinking, it bends its scarred face 
downwards, focus unwavering.  Watching your eyes, it slowly closes 
its own eyelids, as if acknowledging your veracity in the face of 
confrontation.  Its bushy long tail points skywards, then whips into 
a frenzy.  A pang of guilt runs through your being as you slowly 
conclude the true nature of the beast.  With steeled resolve, you 
set forth to end the creatures pain.  
'FWWWPP' 'FWWP'
Before you can lift your foot, a suddenly flash followed by a quip of 
blue ignites in the air.
'FWWWWPP' 'FWWWPP' 'FWWWWPP'
You stare in amazement at entire portions of the Dire Wolf as they 
dissolve into the wind, plant life, and surrounding mounds of moss 
in an ignition of blue flame.
'FWWWWWPPP!'
As the creature hits the forest floor, its body fans out in all 
directions in one brilliant burst of blue flame, illuminating all 
and suddenly evaporating into nothingness.  The forest is quiet.  
A chirp...then the long howl of the wind against the tree leaves.
---------------------------------------------------------------------		
		"""
		print "%s was slain!  Gained %d experience!!" % (self.name, self.experience)
		return self.experience
		
	def win(self):
		"""Win a battle against a Character."""
		print """
--------------------------------------------------------------------
The Dire Wolf circles your tattered body...a slight tug on your.....


A blinding light fills your eyes once again.
---------------------------------------------------------------------		
		"""
		
class SandCreeper(Enemy):
	"""Sand Creeper, Watcher of the Mine"""
	def __init__(self):
		max_hp = randint(6, 10)
		max_mp = randint(2, 4)
		super(SandCreeper, self).__init__("Sand Creeper, Watcher of the Mine", 
			max_hp, max_hp, max_mp, max_mp, randint (2, 4), randint(3, 5), 
			randint(2, 3), randint(1200, 1700))
		
	def introduction(self):
		"""Introduction"""
		print """
--------------------------------------------------------------------
The Sand Creepers gleams...finish implementing this.
--------------------------------------------------------------------
		"""	
		
	def die(self):
		"""Die"""
		print """
--------------------------------------------------------------------
The Sand Creeper scurries away, furiously attempting to burrow 
itself deep within the desert floor.  Its hind legs turn upward as 
its head dips down, its body resembling a shining tobacco-stained 
obelisk standing in the sand.  Suddenly, the swift arid winds coming 
from it's flailing legs halt.  The air around the creature becomes 
heavy and without movement...as a solitary chirp escapes its 
spiracles.  The noise intensifies, followed in unison by a loud 
creaking as the weight of the Sand Creepers tailed-body pulls 
downward on its tattered abdomen.  As it's rigid brown shell pulls 
with gravitational intensity to become parallel with the sloping 
plains of the dunes a sudden crack is heard, followed by a thick 
viscous gurgle.  The creatures tattered abdomen collapses in upon 
itself, letting loose all sights hitherto unseen by its Earthly 
vessel.
---------------------------------------------------------------------		
		"""
		print "%s was slain!  Gained %d experience!!" % (self.name, self.experience)
		return self.experience
		
	def win(self):
		"""Win a battle against a Character."""
		print """
--------------------------------------------------------------------
A flurry of silicate minerals tears into the flesh of your cheek as 
you skid horizontally across the rugged path.  The steady beat of 
wind on carapace sounds from the wings of the enemy above you, as 
its shadow blankets the arid heat beating upon you.  Respite is only 
felt for a moment as the darkness from above lands upon your chest, 
pinning you under its obsidian gleam.  A swift whistling is heard as 
the Sand Creepers left-most appendage sails through the air, 
followed by an immense jolt of agony within your rib cage.  A soft 
gelatinous 'SHHHLLLK' is heard as the dark brown appendage is pulled 
out, then another whistle cuts the air, followed by a third.  Two 
more sickening 'SHHHLLLK's are heard as the creature lurches 
backwards, retracting its arms to examine its prey.  You flail 
endlessly against the Earth, hands digging for ground amongst an 
ocean of sand.  As you attempt to stand, the creature pounces upon 
your punctured remains.  You feel your head falls backwards and 
darkness begins to fill your eyes.  You peer upwards in hopes of 
seeing light one last time, only to be greeted with the thick visage 
of a blotted black mandible above.  In an instant, the jaw clamps 
down like a vice upon your upper torso.  Your entire body shudders 
against it's immense force for only a moment, then a sound akin to 
the felling of a forest echoes across the desolate land in one 
momentous 'CRRRRKKKK!'.  In vain, you gasp for air as your lungs are 
pierced by the crumbling shards of your rib cage.  


Darkness fills your eyes once more.
---------------------------------------------------------------------		
		"""
		
class TwinCyclops(Enemy):
	"""Twin Cyclops, Guardians of the Valley"""
	def __init__(self):
		max_hp = randint(30, 40)
		max_mp = randint(10, 15)
		super(TwinCyclops, self).__init__("Twin Cyclops, Guardians of the Valley", 
			max_hp, max_hp, max_mp, max_mp, randint (8, 10), randint(8, 10), 
			0, randint(5200, 6700))
		
	def introduction(self):
		"""Introduction"""
		print """
--------------------------------------------------------------------
Two Pillars against the Sky...the Twin Cyclops stand...finish 
implementing this.
--------------------------------------------------------------------
		"""		
		
	def die(self):
		"""Die"""
		print """
--------------------------------------------------------------------
The Twin Cyclops dying
---------------------------------------------------------------------		
		"""
		print "%s was slain!  Gained %d experience!!" % (self.name, self.experience)
		return self.experience
		
	def win(self):
		"""Win a battle against a Character."""
		print """
--------------------------------------------------------------------
The Twin Cyclops winning
---------------------------------------------------------------------		
		"""
		
class Khanth(Enemy):
	"""Khanth, Old God of Ithmas"""
	def __init__(self):
		max_hp = randint(75, 99)
		super(Khanth, self).__init__("Khanth, Old God of Ithmas", 
			max_hp, max_hp, 0, 0, randint (15, 19), randint(4, 6), 0, 100000)
		
	def introduction(self):
		"""Introduction"""
		print """
--------------------------------------------------------------------
There are tales of creation that are whispered through this realm, 
one of which treads through the valley by the inhabitants that dare 
speak it.  Their meek utterances speak of a titan, wombed from the 
Northwestern Cliffside.  Upon its birth its massive bulk swayed in 
the Sun, swinging its pendulum arms in the fury towards the newly 
wrought light of life.  When the creature finally knew an end to its 
rage, it slowly came to peer over the creation that had been carved 
from its actions.  This new "womb", a dip downwards into the Earth, 
with veins running South and Southeastern through the old 
mountainside, was a realm the beast recognized as his own.  He 
climbed downward, to once again slumber.
 ...finish implementing this.
--------------------------------------------------------------------
		"""	
		
	def die(self):
		"""Die"""
		print """
--------------------------------------------------------------------
Khanth dying
---------------------------------------------------------------------		
		"""
		print "%s was slain!  Gained %d experience!!" % (self.name, self.experience)
		return self.experience
		
	def win(self):
		"""Win a battle against a Character."""
		print """
--------------------------------------------------------------------
Khanth winning
---------------------------------------------------------------------		
		"""
	
			
class NPC(Character):
	"""NPC Character"""
	def __init__(self, name, description):
		super(NPC, self).__init__(name)
		self.description = description
		
	def stats(self):
		"""Prints the NPC's stats to the screen."""
		print "%s, %s" % (self.name, self.description)
	
	def talk(self, hero):
		"""Talks to the Hero."""
		if isinstance(hero, Hero):
			print "%s doesn't seemed to be interested in speaking right now." % (
					self.name)
		
		
## -------------------------Tests below-------------------------

brandon = Hero("Brandon")
dire_wolf = DireWolf()
sand_creeper = SandCreeper()
twin_cyclops = TwinCyclops()
khanth = Khanth()
npcGuy = NPC("Guy", "just some NPC.")

brandon.stats()
dire_wolf.stats()
sand_creeper.stats()
twin_cyclops.stats()
khanth.stats()
npcGuy.stats()

print "Battle Start - Brandon HP: %d" % brandon.hp
print "Battle Start - Dire Wolf HP: %d" % dire_wolf.hp

# defend() called with 'False' argument means that you defend without being attacked first.
# defend() called without boolean argument means you defend against an attack.
# NOTE: Not sure if I like this implementation....
brandon.defend(dire_wolf, False)
brandon.attack(dire_wolf)
dire_wolf.defend(brandon)
dire_wolf.attack(brandon)
brandon.defend(dire_wolf)
brandon.attack(dire_wolf)
brandon.attack(dire_wolf)
brandon.attack(dire_wolf)
brandon.attack(dire_wolf)
brandon.stats()
dire_wolf.stats()
sand_creeper.die()
sand_creeper.win()
dire_wolf.die()
dire_wolf.win()

brandon.introduction()
khanth.introduction()	
twin_cyclops.introduction()
sand_creeper.introduction()
dire_wolf.introduction()

print "Battle Start - Brandon HP: %d" % brandon.hp
print "Battle End - Dire Wolf HP: %d" % dire_wolf.hp

brandon.flee(dire_wolf.strength, dire_wolf.defense)

brandon.talk(npcGuy)
brandon.talk(dire_wolf)

# should fail
brandon.attack(npcGuy)
dire_wolf.attack(npcGuy)
brandon.defend(npcGuy)
dire_wolf.defend(npcGuy)

## -------------------------End Tests-------------------------