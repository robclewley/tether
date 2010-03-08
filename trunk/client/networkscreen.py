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
import pygame
from pygame.locals import *
import gui
import logging 
import gettext

from twisted.internet import task

import mainmenu
from mappanel import *

#****************************************************************************
#
#****************************************************************************
class NetworkScreen:
    def __init__(self, client):

        self.client = client
        self.mapX = 90
        self.mapY = 90

#****************************************************************************
# screen for after being connected to server
#****************************************************************************
    def join(self):

        self.app = gui.Desktop()
        self.app.connect(gui.QUIT, self.app.quit, None)
        container = gui.Container(align=-1, valign=-1)
        table = gui.Table(width=300, height=220)

        table.add(gui.Widget(),0,0)

        self.message_label = gui.Label(("Join network game"))
        table.add(gui.Widget(width=1, height=5), 0, 0)

        nickname_label = gui.Label(("Username:"))
        table.add(nickname_label,0,1)

        playername_label = gui.Label((self.client.settings.playername))
        table.add(playername_label,1,1)
        table.add(gui.Widget(width=1, height=5), 0, 2)

        hostname_label = gui.Label(("Server address:"))
        table.add(hostname_label,0,2)
        self.hostname_input = gui.Input((self.client.settings.defaultIP))
        table.add(self.hostname_input,1,2)
        table.add(gui.Widget(width=1, height=5), 0, 3)

        connect_button = gui.Button(("Connect"))
        connect_button.connect(gui.CLICK, self.connect_callback, None)
        cancel_button = gui.Button(("Cancel"))
        cancel_button.connect(gui.CLICK, self.cancel_callback, None)

        table.add(gui.Widget(), 0, 4)
        sub_table = gui.Table(width=140, height=35)
        table.add(sub_table, 1, 4)
        sub_table.add(cancel_button, 0,0)
        sub_table.add(connect_button, 1,0)

        container.add(mainmenu.MenuBackground(client=self.client, width = self.client.screen.get_width(), height = self.client.screen.get_height()), 0, 0)
        container.add(table, self.client.screen.get_width() / 2 - 150, self.client.screen.get_height() / 2 - 120)
        container.add(self.message_label, self.client.screen.get_width() / 2 - 160, self.client.screen.get_height() * 0.315)
        self.app.run(container)

#****************************************************************************
# screen for setting up game and starting server, automatically joins server after launch
#****************************************************************************
    def start(self):

        self.app = gui.Desktop()
        self.app.connect(gui.QUIT, self.app.quit, None)
        container = gui.Container(align=-1, valign=-1)
        table = gui.Table(width=300, height=220)

        table.add(gui.Widget(),0,0)

        self.message_label = gui.Label(("Start network game"))
        table.add(gui.Widget(width=1, height=5), 0, 0)

        nickname_label = gui.Label(("Username:"))
        table.add(nickname_label,0,1)
        playername_label = gui.Label((self.client.settings.playername))
        table.add(playername_label,1,1)
        table.add(gui.Widget(width=1, height=5), 0, 2)

        connect_button = gui.Button(("Start Hosting"))
        connect_button.connect(gui.CLICK, self.host_callback, None)
        cancel_button = gui.Button(("Cancel"))
        cancel_button.connect(gui.CLICK, self.cancel_callback, None)

        table.add(gui.Widget(), 0, 3)
        sub_table = gui.Table(width=140, height=35)
        table.add(sub_table, 1, 3)
        sub_table.add(cancel_button, 0,0)
        sub_table.add(connect_button, 1,0)


        container.add(mainmenu.MenuBackground(client=self.client, width = self.client.screen.get_width(), height = self.client.screen.get_height()), 0, 0)
        container.add(table, self.client.screen.get_width() / 2 - 150, self.client.screen.get_height() / 2 - 120)
        container.add(self.message_label, self.client.screen.get_width() / 2 - 160, self.client.screen.get_height() * 0.315)

        self.app.run(container)


 
#****************************************************************************
#
#****************************************************************************
    def connect_callback(self, obj):
        self.client.moonaudio.sound("buttonclick.ogg")
        server = self.hostname_input.value
        nick = self.client.settings.playername
        self.client.settings.hostIP = server
        self.app.quit()
        self.client.connect_network_game(server, nick)

 
#****************************************************************************
#
#****************************************************************************
    def host_callback(self, obj):
        self.client.ishost = True
        logging.info("Hosting game")
        self.client.moonaudio.sound("buttonclick.ogg")
        nick = self.client.settings.playername
        self.app.quit()
        self.client.host_network_game("localhost", nick)
   
#****************************************************************************
#
#****************************************************************************
    def cancel_callback(self, obj):
        self.client.moonaudio.sound("buttonclick.ogg")
        self.app.quit()
        mainmenu.MainMenu(self.client)

#****************************************************************************
#
#****************************************************************************
class PregameScreen:
    def __init__(self, client):
        self.client = client
        self.show()

#****************************************************************************
#  
#****************************************************************************
    def show(self):
        width = 600
        height = 300
        self.app = gui.Desktop()
        self.app.connect(gui.QUIT, self.app.quit, None)
        container = gui.Container(align=-1, valign=-1)
        table = gui.Table(width=width, height=220)

        table.add(gui.Widget(),0,0)

        self.message_label = gui.Label(("Pregame setup"))
        table.add(gui.Widget(width=1, height=5), 0, 0)

        self.chat_table = gui.Table(width=width,height=height)

        self.chat_table.tr()
        self.lines = gui.Table()
        self.message_out = StringStream(self.lines)
        self.box = gui.ScrollArea(self.lines, width, height)

        self.chat_table.td(self.box) 

        self.chat_table.tr()
        self.line = gui.Input()
        self.line.style.width = width
        self.chat_table.td(self.line)

        self.chat_table.tr()
        self.chat_table.td(MySpacer(1,1, self.box))

        table.add(self.chat_table, 0, 1)

        table.add(gui.Widget(), 0, 2)
        sub_table = gui.Table(width=140, height=35)
        table.add(sub_table, 0, 3)

        cancel_button = gui.Button(("Cancel"))
        cancel_button.connect(gui.CLICK, self.cancel_callback)
        sub_table.add(cancel_button, 0,0)
        if self.client.ishost == True:
            connect_button = gui.Button(("Start Game"))
            connect_button.connect(gui.CLICK, self.start_callback)
            sub_table.add(connect_button, 1,0)
            

        container.add(mainmenu.MenuBackground(client=self.client, width = self.client.screen.get_width(), height = self.client.screen.get_height()), 0, 0)
        container.add(table, self.client.screen.get_width() / 2 - 300, self.client.screen.get_height() / 2 - 120)
        container.add(self.message_label, self.client.screen.get_width() / 2 - 160, self.client.screen.get_height() * 0.315)


        setup_table = gui.Table(width=50, height=50)
        self.map_size_label = gui.Label(("Map Size"))
        setup_table.add(self.map_size_label, 0, 0)
        self.map_size_setup = gui.Select(value=self.client.pregame_mapsize)
        self.map_size_setup.add("Large", "large")
        self.map_size_setup.add("Medium", "medium")
        self.map_size_setup.add("Small", "small")
        setup_table.add(self.map_size_setup, 0, 1)
        container.add(setup_table, self.client.screen.get_width() / 10, self.client.screen.get_height() / 3)

        self.message_out.write("Connected sucessfully to MoonPy server.")

        self.app.init(container)
        self.loop = task.LoopingCall(self.pregame_loop)
        self.loop.start(1/30)


#****************************************************************************
#  
#****************************************************************************
    def pregame_loop(self):
        for event in pygame.event.get():
            self.app.event(event)
            if event.type == KEYDOWN and event.key == K_RETURN:
                text = self.line.value
                self.line.value = ""
                self.client.netclient.send_chat(text)
                self.line.focus()
            if self.client.ishost == True:
                self.client.netclient.update_pregame_settings(self.map_size_setup.value)
            self.map_size_setup.value = self.client.pregame_mapsize
            self.app.repaint()
            self.app.update(self.client.screen)
            pygame.display.flip()

#****************************************************************************
#
#****************************************************************************
    def show_message(self, message):
        self.message_out.write(message)

#****************************************************************************
#
#****************************************************************************
    def cancel_callback(self):
        self.client.moonaudio.sound("buttonclick.ogg")
        self.client.netclient.disconnect()
        self.app.quit()
        mainmenu.MainMenu(self.client)

#****************************************************************************
#
#****************************************************************************
    def start_callback(self):
        self.client.moonaudio.sound("buttonclick.ogg")
        self.message_out.write("Please wait while starting a new game.")
        if self.map_size_setup.value == "small":
            self.mapX = 90
            self.mapY = 90
        elif self.map_size_setup.value == "medium":
            self.mapX = 135
            self.mapY = 135
        elif self.map_size_setup.value == "large":
            self.mapX = 180
            self.mapY = 180
        else:
            logging.critical("invalid map size detected")
            sys.exit(1)
        self.client.netclient.start_server_game()

#****************************************************************************
#
#****************************************************************************
    def start_game(self):
        self.client.moonaudio.end_music()
        self.loop.stop()
        self.app.quit()
        self.client.start_game()
