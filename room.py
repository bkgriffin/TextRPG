#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Room class~
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

class Room(object):
	"""Room
	    A Room is a four sided square.  They may contain objects 
	    (i.e. Hero, Enemies, ConsumableItems, etc.).  
	    Every room has adjacent room objects (north, south, east, west), 
	    or None, if there is nothing adjacent.
	    Room. 
	    NOTE:  The coordinate of any room can be derived by X, Y where:
	    		coordinate = XY
	    		character movement north = X + 1 character in the alphabet
	    		character movement south = X - 1 character in the alphabet
	    		character movement east = Y + 1 number 
	    		character movement west = Y - 1 number
	    """
	def __init__(self, name, coordinate, description, objects, north, south, east, west):
		self.name = name
		self.coordinate = coordinate
		self.description = description
		self.objects = []
		self.north = north
		self.south = south
		self.east = east
		self.west = west
		
	def stats(self):
		"""Prints the Room's stats to the screen."""
		print """-%s\'s Stats-
  Coordinate: 
  \t%s\n
  Description: 
  \t%s\n
  Objects: 
  \t%s\n
  North:
  \t%s
  South: 
  \t%s
  East: 
  \t%s
  West:
  \t%s
  """ % (self.name, self.coordinate, self.description, 
  		[', '.join(str(a.name) for a in self.objects)], 
  		self.north, self.south, self.east, self.west)
	
	def enter(self):
		"""Enter the Room."""
		print "This method is not yet configured.  Subclass it and implement enter()."
		exit(1)
		
	def exit(self):
		"""Exit the Room."""
		print "This method is not yet configured.  Subclass it and implement exit()."
		exit(1)


class A4(Room):
	"""Room A4"""
	def __init__(self):
		super(A4, self).__init__("Entrance", "A4", "The entrance to the valley.", 
				None, "B4", None, None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """You peer over the landscape after climbing through 
the entrance to the valley."""
		
	def exit(self):
		"""Exit the Room."""
		print "A white lights shears through you.  You awaken..."
		exit(1)
		
		
class B4(Room):
	"""Room B4"""
	def __init__(self):
		super(B4, self).__init__("Second Room", "B4", "The second room of the valley.", 
				None, "C4", "A4", None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B4"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B4"
		
class C4(Room):
	"""Room C4"""
	def __init__(self):
		super(C4, self).__init__("Third Room", "C4", "The third room of the valley.", 
				None, "D4", "B4", None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter C4"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit C4"
		
class D4(Room):
	"""Room D4"""
	def __init__(self):
		super(D4, self).__init__("Fourth Room", "D4", "The fourth room of the valley.", 
				None, "E4", "C4", "D5", "D3")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D4"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D4"
		
class D3(Room):
	"""Room D3"""
	def __init__(self):
		super(D3, self).__init__("Another Room", "D3", "Another room of the valley.", 
				None, None, None, "D4", "D2")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D3"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D3"
		
class D2(Room):
	"""Room D2"""
	def __init__(self):
		super(D2, self).__init__("Another Room", "D2", "Another room of the valley.", 
				None, None, "C2", "D3", "D1")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D2"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D2"
		
class D1(Room):
	"""Room D1"""
	def __init__(self):
		super(D1, self).__init__("Another Room", "D1", "Another room of the valley.", 
				None, None, None, "D2", None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D1"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D1"
		
class C2(Room):
	"""Room C2"""
	def __init__(self):
		super(C2, self).__init__("Another Room", "C2", "Another room of the valley.", 
				None, "D2", "B2", None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter C2"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit C2"
		
class B2(Room):
	"""Room B2"""
	def __init__(self):
		super(B2, self).__init__("Another Room", "B2", "Another room of the valley.", 
				None, "C2", None, None, "B1")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B2"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B2"
		
class B1(Room):
	"""Room B1"""
	def __init__(self):
		super(B1, self).__init__("Another Room", "B1", "Another room of the valley.", 
				None, None, None, "B2", None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B1"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B1"


## -------------------------Tests below-------------------------

A4 = A4()
A4.stats()
A4.enter()
#A4.exit()

B4 = B4()
B4.stats()
B4.enter()
B4.exit()

C4 = C4()
C4.stats()
C4.enter()
C4.exit()

D4 = D4()
D4.stats()
D4.enter()
D4.exit()

D3 = D3()
D3.stats()
D3.enter()
D3.exit()

D2 = D2()
D2.stats()
D2.enter()
D2.exit()

D1 = D1()
D1.stats()
D1.enter()
D1.exit()

C2 = C2()
C2.stats()
C2.enter()
C2.exit()

B2 = B2()
B2.stats()
B2.enter()
B2.exit()

B1 = B1()
B1.stats()
B1.enter()
B1.exit()

## -------------------------End Tests-------------------------