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
				["SpringWater"], "E4", "C4", "D5", "D3")
				
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
				["BraidedRope", "RustedHook", "RottingBucket", "MalachiteCrystal"], 
				None, None, "D4", "D2")
				
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
				["WoodCuttingAxe"], None, "C2", "D3", "D1")
				
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
				["GardenVegetables", "ScarecrowClothes", "CowlTheScaredCrow"], 
				None, None, "D2", None)
				
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
				["DireWolves"], "D2", "B2", None, None)
				
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
				["OldMare", "AnimalCarcass"], None, None, "B2", None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B1"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B1"
		
class E4(Room):
	"""Room E4"""
	def __init__(self):
		super(E4, self).__init__("Another Room", "E4", "Another room of the valley.", 
				None, "F5", "D4", None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter E4"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit E4"
		
class F5(Room):
	"""Room F5"""
	def __init__(self):
		super(F5, self).__init__("Another Room", "F5", "Another room of the valley.", 
				["TwinCyclops"], None, "E4", None, "F6")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter F5"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit F5"
		
class F6(Room):
	"""Room F6"""
	def __init__(self):
		super(F6, self).__init__("Another Room", "F6", "Another room of the valley.", 
				None, None, None, None, "F5")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter F6"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit F6"
		
class D5(Room):
	"""Room D5"""
	def __init__(self):
		super(D5, self).__init__("Another Room", "D5", "Another room of the valley.", 
				["BizzleBeakArmor"], None, None, "D6", "D4")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D5"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D5"
		
class D6(Room):
	"""Room D6"""
	def __init__(self):
		super(D6, self).__init__("Another Room", "D6", "Another room of the valley.", 
				["AutumnHerbs"], None, "C6", None, "D5")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D6"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D6"
		
class C6(Room):
	"""Room C6"""
	def __init__(self):
		super(C6, self).__init__("Another Room", "C6", "Another room of the valley.", 
				None, "D6", "B6", None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter C6"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit C6"
		
class B6(Room):
	"""Room B6"""
	def __init__(self):
		super(B6, self).__init__("Another Room", "B6", "Another room of the valley.", 
				None, "C6", None, "B7", None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B6"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B6"
		
class B7(Room):
	"""Room B7"""
	def __init__(self):
		super(B7, self).__init__("Another Room", "B7", "Another room of the valley.", 
				None, "C7", None, "B8", "B6")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B7"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B7"
		
class B8(Room):
	"""Room B8"""
	def __init__(self):
		super(B8, self).__init__("Another Room", "B8", "Another room of the valley.", 
				None, None, "A8", None, "B7")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter B8"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit B8"
		
class A8(Room):
	"""Room A8"""
	def __init__(self):
		super(A8, self).__init__("Another Room", "A8", "Another room of the valley.", 
				["StoneUrn"], "B8", None, None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter A8"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit A8"
		
class C7(Room):
	"""Room C7"""
	def __init__(self):
		super(C7, self).__init__("Another Room", "C7", "Another room of the valley.", 
				["SandCreedpers"], None, "B7", "C8", None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter C7"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit C7"
		
class C8(Room):
	"""Room C8"""
	def __init__(self):
		super(C8, self).__init__("Another Room", "C8", "Another room of the valley.", 
				["SpikeMaul"], "D8", None, None, "C7")
				
	def enter(self):
		"""Enter the Room."""
		print """Enter C8"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit C8"
		
class D8(Room):
	"""Room D8"""
	def __init__(self):
		super(D8, self).__init__("Another Room", "D8", "Another room of the valley.", 
				["BundleOfDynamite"], None, "C8", None, None)
				
	def enter(self):
		"""Enter the Room."""
		print """Enter D8"""
		
	def exit(self):
		"""Exit the Room."""
		print "Exit D8"


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

D5 = D5()
D5.stats()
D5.enter()
D5.exit()

D6 = D6()
D6.stats()
D6.enter()
D6.exit()

C6 = C6()
C6.stats()
C6.enter()
C6.exit()

B6 = B6()
B6.stats()
B6.enter()
B6.exit()

C7 = C7()
C7.stats()
C7.enter()
C7.exit()

C8 = C8()
C8.stats()
C8.enter()
C8.exit()

D8 = D8()
D8.stats()
D8.enter()
D8.exit()

B7 = B7()
B7.stats()
B7.enter()
B7.exit()

B8 = B8()
B8.stats()
B8.enter()
B8.exit()

A8 = A8()
A8.stats()
A8.enter()
A8.exit()

## -------------------------End Tests-------------------------