# phoneOpperationHelper: An Add-on for nvda.
#Copyright (C) 2017 derek Riemer
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""phoneOpperationHelper:
A global plugin 
"""
import globalPluginHandler
import speechDictHandler
import re

oldProcessText = None
RE_NUMBERS_SPLIT = re.compile(r"(\d)(?=\d)")
RE_FIVE_DIGITS_OR_MORE = re.compile(r"\d{5,}")

def newProcessText(text):
	text = oldProcessText(text)
	newText = ""
	items = (item.span() for item in  RE_FIVE_DIGITS_OR_MORE.finditer(text))
	try:
		minimum, maximum = next(items)
	except StopIteration:
		minimum, maximum = len(text), len(text)
	for i in range(len(text)):
		if i < minimum:
			newText+= text[i]
		elif minimum <= i < maximum:
			newText += text[i]+" "
		else:
			try:
				minimum, maximum = next(items)
			except StopIteration:
				minimum, maximum = len(text), len(text)
			newText += text[i]
	return newText

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		global oldProcessText
		super(GlobalPlugin, self).__init__()
		oldProcessText = speechDictHandler.processText
		speechDictHandler.processText = newProcessText
	
	__gestures = {
		#Fill me in please. If you don't need me, delete me.
	}
	
