#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Map class~
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
from room import *

class Map(object):
	"""Map
	A Map contains room objects.  
	These are the rooms in which your Hero can traverse."""
	def __init__(self):
		self.rooms = [A4, B4, C4, D4, D3, D2, D1, C2, B2, B1]
		#rooms left: [E4, F5, F6, D5, D6, C6, B6, C7, C8, D8, B7, B8, A8]
		self.location = globals()['A4']
		self.goal = globals()['B1'] #really, ['F6']
	
	def use(self):
		print """
		Location: %s
		Goal: %s
		""" % (self.location, self.goal)
		
		
		"""Opens the world map."""
		print """ \n\n
		\---------------Valley of Ithmas----------------/
		|-----------------------------------------------|
		|                                               |
		|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
                |-----------------------------------------------|
                |-----|/////|////^|/^//^|     |     |^//^/|/////|
              F |-----|///^/|//^//|^////|        !  |/^///|/////|
              	|~~~~~|-----|-----|///^/|     |     |^////|^////|
                |---------------------- .. ---------------------|
                |-----|~~~~~|~~~~~|     |^/^/^|///^/|^////|////^|
              E |\'`\\\\'|-----|~~~~~|     |/^/^/|/////|//^//|^////|
              	|\\\\\`\\|\`\\\\\|-----|     |/////|/^///|//^//|/////|
                |-------------------- --------------------------|	
                |     |     |     |     |     |     |^////|     |
              D |                                   |/////|     |
              	|     |     |     |     |     |     |/////|     |
                |-------- ----------- ----------- ----------- --|
                |'`\'`\'|     |\'`\\``|     |/////|     |     |     |
              C |\\\'`\\'|     |`\\\\\\\\|     |~~~~~|     |           |
              	|\\\\\'`'|     |\`\'`\|     |\'`\``|     |     |     |
                |-------- ----------- ----------- ---- .. ------|
                |     |     |\\\\\'`\|     |\\`\'`\|     |     |     |
              B |     :     |\\\\\\\\\|     |'`'`\|                 |
              	|     |     |\\\\\'`\|     |\\\\\\\\\|     |     |     |
                |-------------------- ----------------------- --|
                |\\\\\\\\\|\\`\\\\\\|`\\\\`\|     |\\\\\\\\\|\\\\\\\\\|~~~~~|     |
              A |\\\\\\\\\|\\\\\\\\\|\\\\\\\\\|  *  |\\\\\\\\\|\\\\\\\\\|-----|     |
              	|\\\\\\\\\|\\\\\\\\\|\\\\\\\\\|     |\\\\\\\\\|\\\\\\\\\|\\\\\\\\\|     |
                |-----------------------------------------------|
		/-----------------------------------------------\\
		
		|-LEGEND---------------|
		|    *  YOU ARE HERE   |
		|    .. OBSTACLE       |
		|    !  GOAL           |
		|----------------------|
		     \n\n"""
	
	def move(self, direction):
		"""Move the location."""
		current_room = self.location
		if direction == "north" or direction == "North":
			if current_room.north == None:
				print "There's nothing there..."
			else:
				self.location = globals()[current_room.north]
				self.location.enter()
		elif direction == "south" or direction == "South":
			if current_room.south == None:
				print "There's nothing there..."
			else:
				self.location = globals()[current_room.south]
				self.location.enter()
		elif direction == "east" or direction == "East":
			if current_room.east == None:
				print "There's nothing there..."
			else:
				self.location = globals()[current_room.east]
				self.location.enter()
		elif direction == "west" or direction == "West":
			if current_room.west == None:
				print "There's nothing there..."
			else:
				self.location = globals()[current_room.west]
				self.location.enter()
		else:
			print "Is %s a direction?" % direction