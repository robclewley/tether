"""Copyright 2009:
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


import logging
import pygame
import gettext
import platform
import sys
import os

import introscreen  

from networkclient import *
from gameclientstate import *
from mainmenu import *

from common.translation import *


#****************************************************************************
# The Main class of the client. 
#****************************************************************************
class Main:

    def __init__(self, debug):
        pygame.init()

        tetherdir = os.getenv("HOME")
        if str(tetherdir) == "None":
            tetherdir = os.getenv("USERPROFILE")
        tetherdir = os.path.join(tetherdir, ".tether")
        if not os.path.exists(tetherdir):
            os.mkdir(tetherdir)
        logfile = os.path.join(tetherdir, "MoonPy.log")
        if os.path.exists(logfile):
            os.remove(logfile)
        if debug == True:
            logLevel = logging.INFO
            common.log.setUpLogging(logLevel)
        else:
            LOG_FILENAME = logfile
            logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

        self.dependencyCheck()
        self.client = GameClientState()    
        logging.info("MoonPy version %s" % (self.client.settings.string_version))

        self.initialize_locale()

        self.create_main_window()
        self.client.moonaudio.intro()
        self.intro = introscreen.IntroScreen(self.client.screen)

        mainmenu = MainMenu(self.client)

#****************************************************************************
#
#****************************************************************************
    def initialize_locale(self):
        translation = Translation()
        translation.setLanguage(self.client.settings.language)

#****************************************************************************
#
#****************************************************************************
    def create_main_window(self):
        screen_width = self.client.settings.screen_width 
        screen_height = self.client.settings.screen_height 
        screen_mode = 0
        screen = pygame.display.set_mode((500, 500), screen_mode)

        pygame.display.set_caption("Welcome to MoonPy")
        self.client.screen = screen

#****************************************************************************
# Check dependencies (Pygame).
#****************************************************************************
    def dependencyCheck(self):
        #verify that all dependencies are met
        logging.info('Platform: ' + platform.platform())
        logging.info('Python version ' + sys.version)
        try:
            import pygame
            logging.info('Pygame version: ' + pygame.version.ver)
        except ImportError, err:
            print"missing pygame depency"
            logging.error('Loading dependency "pygame" failed: ' + str(err))
            sys.exit(1)
        try :
            import PIL.Image as Image
            logging.info('Python Image Library version ' + Image.VERSION)
        except ImportError, err:
            print"missing PIL dependency"
            logging.info('Loading dependency "PIL" failed: ' + str(err))
            sys.exit(1)
        try:
            import twisted
            if hasattr(twisted, '__version__'):
                logging.info('Twisted version ' + twisted.__version__)
            else:
                logging.info('Twisted version unknown (probably old)')
        except ImportError, err:
            print"missing twisted dependency"
            logging.error('Loading dependency "twisted" failed: ' + str(err))
            sys.exit(1)


