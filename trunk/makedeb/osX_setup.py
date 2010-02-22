#!/usr/bin/python
 
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


import sys
import os
import subprocess
import logging

def main():
    #this is to verify compatible python version is in use
    if sys.version_info < (2, 4):
        print("MoonPy requires python2.5 or higher")
        logging.error("Python version incompatibility: python < 2.5")
        sys.exit(1)
    if not sys.version_info < (3, 0):
        print("MoonPy is not compatible with python3.x yet")
        logging.error("Python version incompatibility: python >= 3.0")
        sys.exit(1)
    try:
        import pygame
        print"Pygame version " + pygame.version.ver + " already installed"
    except:
        if os.name == "nt":
            print"Installing pygame"
            subprocess.Popen([r"msiexec", "/i", "windows_deps\pygame-1.9.1.win32-py2.6.msi"]).wait()
        elif os.name == "mac":
            print"automatic osX pygame installation not yet implemented"
        else:
            print"Unknown OS, PIL will need to be installed manually"
    try:
        import Image
        print"PIL version " + Image.version + " already installed"
    except:
        if os.name == "nt":
            print"installing PIL"
            subprocess.Popen([r"windows_deps\PIL-1.1.7.win32-py2.6.exe"]).wait()
        elif os.name == "mac":
            print"automatic osX PIL installation not yet implemented"
        else:
            print"Unknown OS, PIL will need to be installed manually"
    print"end of dependency script"

main()
