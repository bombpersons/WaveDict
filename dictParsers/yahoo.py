# -*- coding: utf-8 -*-
# This file parses the definitions at http://dic.yahoo.co.jp

import logging

from scrapemark import scrape

class YahooParser:
	# GET DEFINITION
	def getDefinition(self, html):
		definition  = scrape(""" 
		<table border=0 cellspacing=10 cellpadding=0 width=100%> 
			<tr> 
				<td> 			
					{{ }}
				</td> 
			</tr> 
		</table> 
		""", html)
		
		return definition
