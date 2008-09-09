"""Copyright 2007:
    Isaac Carroll, Kevin Clement, Jon Handy, David Carroll, Daniel Carroll

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
"""

import gvars
import gooeypy as gui
from gooeypy.const import *


def menu():
	gvars.activeScreen = mainMenu()
	gvars.moonPyApp.add(gvars.activeScreen)
	gvars.screenRunning = True
	while gvars.screenRunning:
		if gvars.appRunning == False:
			gvars.screenRunning = False
		gvars.clock.tick(30)

		events = pygame.event.get()

		for event in events:
			if event.type == QUIT:
				gvars.appRunning = False

		gvars.moonPyApp.run(events)
		gvars.moonPyApp.draw()

		gui.update_display()


def mainMenu():
	mainMenuScreen = gui.Container(width=800, height=600)
	backButton = gui.Button("Back", x=20, y=400)
	incompleteError = gui.Label(value="Single player game not implemented yet!", x=20, y=200, font_size=30)
	mainMenuScreen.add(backButton, incompleteError)
	backButton.connect(CLICK, cancel)
	return mainMenuScreen


def cancel():
	gvars.moonPyApp.remove(gvars.activeScreen)
	gvars.screenRunning = False
	