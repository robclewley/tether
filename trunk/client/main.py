"""Copyright 2010:
    Kevin Clement

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
import platform
import sys
import os
import time
from gameclient import *

#****************************************************************************
# The Main class of the client. 
#****************************************************************************
class Main:
    def __init__(self, debug):
        pygame.init()
        savedir = os.getenv("HOME")
        if str(savedir) == "None":
            savedir = os.getenv("USERPROFILE")
            savedir = os.path.join(savedir, "scorchedmoon")
        else:
            savedir = os.path.join(savedir, ".scorchedmoon")
        if not os.path.exists(savedir):
            os.mkdir(savedir)
        logfile = os.path.join(savedir, "scorchedmoon.log")
        if os.path.exists(logfile):
            os.remove(logfile)
        if debug == True:
            logLevel = logging.INFO
            logging.basicConfig(level=logging.DEBUG)
        else:
            LOG_FILENAME = logfile
            logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

        logging.info("Platform: " + platform.platform())
        logging.info("Python version " + sys.version)
        logging.info("Pygame version: " + pygame.version.ver)

        self.client = GameClient()
        self.client.debug = debug
        logging.info("Scorched Moon version: " + self.client.settings.stringversion)
        print "loaded main and then quit!"
