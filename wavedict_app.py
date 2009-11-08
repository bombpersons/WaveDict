import urllib, re

from waveapi import events
from waveapi import model
from waveapi import robot

from google.appengine.api import urlfetch
import logging

from dictParsers import yahoo

# DEFS -----------------------------------------------------------------
dict_url = "http://dic.yahoo.co.jp/dsearch?enc=UTF-8&p=%(search)s&stype=1&dtype=0"
REGEX = r".*define:\s(\S+)\s*"

def OnRobotAdded(properties, context):
	"""Invoked when the robot has been added."""
	root_wavelet = context.GetRootWavelet()
	root_wavelet.CreateBlip().GetDocument().SetText("""
To get a definition, simply type into a blip:
							define(colon) word 

Replace (colon) with a ":". Click done, and waveDict will get the definition for you!
For more information go to http://wavedict.appspot.com
	""")

def OnBlipSubmitted(properties, context):
	"""Called when someone adds a blip to the wave."""
	# Get the blip
	blip = context.GetBlipById(properties['blipId'])
	wavelet = context.GetWaveletById(blip.GetWaveletId())
	doc = blip.GetDocument()
	content = doc.GetText()
	
	# Check whether or not there are any things to look up in this blip
	matchs = re.finditer(REGEX, content, re.U | re.IGNORECASE)
	if matchs:
		for match in matchs:
			# Work out the word we need to look up.
			word = match.group(1)
			
			# Look up the word in contents
			result = urlfetch.fetch(dict_url % {'search': urllib.quote(word.encode('utf-8'))})
			
			# If that worked, continue
			if result.status_code == 200:
				# Now get the definition.
				parser = yahoo.YahooParser()
				definition = parser.getDefinition(result.content)
				
				if definition != None:
					# Add a reply to this blip with definition
					logging.debug(definition)
					doc.AppendInlineBlip().GetDocument().SetText(word + ":\n" + definition)
				else:
					logging.debug("No definition found")
					doc.AppendInlineBlip().GetDocument().SetText("WaveDict:\nNo definitions found.")
					
			else:
				logging.debug("Couldn't get the page...")
				doc.AppendInlineBlip().GetDocument().SetText("WaveDict:\nAn error occurred. http://dic.yahoo.co.jp is most likley down")
	
	else:
		logging.debug("No Matches")
		
	logging.debug("End")

if __name__ == '__main__':
	# Make the robot.
	waveDict = robot.Robot('wavedict', 
			image_url='http://wavedict.appspot.com/media/icon.png',
			version='2',
			profile_url='http://wavedict.appspot.com/')
	
	# Register functions to be called when things happen.
	waveDict.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded) # When the robot is added.
	waveDict.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted) # When someone submits a blip.
	
	# Let's go =)
	waveDict.Run()
