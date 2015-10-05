#!/usr/bin/env python
#
# - level I - 
#
# Valley of Ithmas
#
# ~Toolkit module~
# 
__author__     = "Brandon Griffin"
__copyright__  = "Copyright 2015"
__credits__    = "Brandon Griffin"
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Brandon Griffin"
__email__      = "brandon.k.griffin@gmail.com"
__status__     = "Development"

import re

def find_word(search, text):
	"""Find the exact term searched in the text provided.
		Prevents false positives on words that are substrings of words:
			i.e. if "move" in "remove" == true
				 if find_word("move", "remove") == false"""
	result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
	if len(result) > 0:
		return True
	else:	
		return False