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

import os
import sys
import gvars
from time import sleep
import pygame
from pygame.locals import *
import settings
import gooeypy as gui
from gooeypy.const import *
import solo_setup
import multi_setup
import editor


def main():
	gvars.clock = pygame.time.Clock()
	pygame.init()
	pygame.display.set_caption("MoonPy")
	drawSplashScreen()
	settings.load_settings()
	pygame.mouse.set_visible(1)
	gui.init(800,600)
    	if gvars.FULLSCREEN == True:
        	pygame.display.set_mode(gvars.WINDOW_SIZE, pygame.FULLSCREEN)
	gvars.appRunning = True
	gvars.moonPyApp = gui.App(gvars.theme, width=800, height=600)
	while gvars.appRunning:
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

def drawSplashScreen():
	image = "images/Enceladus.png"
	screen = pygame.display.set_mode((550,550))
	try:
		splashScreen = pygame.image.load(image)
	except pygame.error, message:
		print 'Cannot load splash image'
		raise SystemExit, message
	splashScreen = splashScreen.convert()
	screen.blit(splashScreen, (0,0))
	pygame.display.flip()
	sleep(2)

def mainMenu():
	mainMenuScreen = gui.Container(width=800, height=600)
	debug = gui.Button("Debug", x=20, y=30)
	solo = gui.Button("Solo", x=20, y=130)
	multi = gui.Button("Multi", x=20, y=180)
	settings = gui.Button("Settings", x=20, y=230)
	editor = gui.Button("Editor", x=20, y=280)
	quit = gui.Button("quit", x=20, y=330)
	mainMenuScreen.add(solo, multi, settings, debug, editor, quit)
	debug.connect(CLICK, debugButton)
	solo.connect(CLICK, soloButton)
	multi.connect(CLICK, multiButton)
	settings.connect(CLICK, settingsButton)
	editor.connect(CLICK, editorButton)
	quit.connect(CLICK, quitButton)
	return mainMenuScreen

def soloButton():
	gvars.moonPyApp.remove(gvars.activeScreen)
	solo_setup.menu()


def multiButton():
	gvars.moonPyApp.remove(gvars.activeScreen)
	multi_setup.menu()


def settingsButton():
	gvars.moonPyApp.remove(gvars.activeScreen)
	settings.settings_menu()


def debugButton():
	if gvars.debug == False:
		gvars.debug = True
		pygame.display.set_caption("MoonPy Debug")
	else:
		gvars.debug = False
		pygame.display.set_caption("MoonPy")


def editorButton():
	gvars.moonPyApp.remove(gvars.activeScreen)
	editor.menu()


def quitButton():
	gvars.appRunning = False