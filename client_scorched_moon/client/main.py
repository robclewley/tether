"""Copyright 2015:
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

import sys
import logging
import os
import platform
import threading
from time import sleep
from . import gameclient

class Main:
    def __init__(self, debug, loglevel, skip):
        version = 0.015
        stringversion = "0.01.5"

        #figuring out directory for logs, settings, and save files
        tetherdir = os.getenv("HOME")
        if str(tetherdir) == "none":
            tetherdir = os.getenv("USERPROFILE")
            tetherdir = os.path.join(tetherdir, "scorched_moon")
        else:
            tetherdir = os.path.join(tetherdir, ".scorched_moon")
        if not os.path.exists(tetherdir):
            os.mkdir(tetherdir)
        if os.name == "nt":
            logdir = os.path.join(tetherdir, "logs\\")
        else:
            logdir = os.path.join(tetherdir, "logs/")
        if not os.path.exists(logdir):
            os.mkdir(logdir)

        # breaking up sessions in logfile
        logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.DEBUG,format='%(message)s')
        logging.critical("----------------------------------------------------------------------------------------------------------------------------")
        logging.critical("----------------------------------------------------------------------------------------------------------------------------")

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler) # clears out handler to prepare for next logging session

        logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.ERROR,format='%(levelname)s - %(asctime)s -- %(message)s') #default logging configuration until we can load custom settings

        logging.critical("Initializing Scorched Moon Client")

        if sys.version_info < (3, 0): #checking for dependencies
            logging.critical("Scorched Moon requires python3 or higher")
            sys.exit(1)
        try:
            import pygame
        except:
            logging.critical("Unable to find pygame, please install pygame for python3")
            sys.exit(1)

        self.client = gameclient.ClientState()
        self.client.settings.version = version
        self.client.settings.stringversion = stringversion
        self.client.settings.tetherdir = tetherdir

        if loglevel != 0: #arguments override settings file for logging
            self.client.settings.loglevel = loglevel
        else: # loglevel 0 means no argument used so we go with settings file
            loglevel = self.client.settings.loglevel

        if debug == True: # arguments override settings file for debug
            self.client.settings.debug = True

        if self.client.settings.debug == True: #debug overrides loglevels
            loglevel = 1

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler) # clears out handler again so we can use custom logging settings
        
        if loglevel == 1:
            logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.DEBUG,format='%(levelname)s - %(asctime)s - %(module)s:%(funcName)s:%(lineno)s -- %(message)s')
        elif loglevel == 2:
            logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.INFO,format='%(levelname)s - %(asctime)s -- %(message)s')
        elif loglevel == 3:
            logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.WARNING,format='%(levelname)s - %(asctime)s -- %(message)s')
        elif loglevel == 4:
            logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.ERROR,format='%(levelname)s - %(asctime)s -- %(message)s')
        elif loglevel == 5:
            logging.basicConfig(filename=logdir+'scorched_moon_client.log',level=logging.CRITICAL,format='%(levelname)s - %(asctime)s -- %(message)s')
        else: #invalid loglevel
            logging.critical("Invalid loglevel {}" .format(loglevel))
            logging.critical("Unable to start logging")
            sys.exit()

        # confirming startup status and logging
        if self.client.settings.debug:
            logging.critical("Scorched Moon client ver. {} running in debug mode" .format(stringversion))
            logging.critical("Log level forced to {}" .format(loglevel))
        else:
            logging.critical("Scorched Moon client ver. {}" .format(stringversion))
            logging.critical("Log level is set to {}" .format(loglevel))
        logging.critical("Platform: {}" .format(platform.platform()))
        logging.critical("Python version: {}" .format(sys.version))
        logging.critical("Pygame version: {}" .format(pygame.version.ver))

        #splashscreen
        image = "data/graphics/misc/intro_splash.png"
        screen = pygame.display.set_mode((550,550))
        try:
            splashScreen = pygame.image.load(image)
        except pygame.error as message:
            logging.warning("unable to open splash image")
            skip = True
        if skip == False:
            pygame.display.set_caption("Scorched Moon {}" .format(self.client.settings.stringversion))
            splashScreen = splashScreen.convert()
            screen.blit(splashScreen, (0,0))
            pygame.display.flip()
            sleep(2)
            pygame.display.quit()


        netthread = threading.Thread(target=self.checknet)
        netthread.daemon = True
        netthread.start()

        self.client.load_main_menu() #load main menu
        pygame.display.set_caption("Scorched Moon ver. {}" .format(self.client.settings.stringversion))
        while self.client.runclient: # main client loop
            self.client.display.desktop.loop()
            if self.client.network.buffer != "":
                print(self.client.network.buffer)
                self.client.network.buffer = ""


        logging.info("Quit command received")
        if self.client.network.connected == "True":
            self.client.network.send("exit")

        logging.critical("Scorched Moon client successfully shutdown")
        logging.shutdown()
        sys.exit(0) # final shutdown confirmation

    def checknet(self):
        while self.client.runclient == "True":
            if self.client.network.connected:
                self.client.network.receive()
            else:
                pass
