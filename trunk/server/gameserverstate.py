# OpenRTS - Copyright (C) 2006 The OpenRTS Project
#
# OpenRTS is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# OpenRTS is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

import logging
from twisted.internet import task, reactor
from twisted.cred.portal import Portal
from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse
from twisted.spread import pb
from twisted.cred.portal import IRealm

from common.map import * 
from common.game import * 
from common.mapgen import *
from common.settings import *
from connectionhandler import *


#****************************************************************************
#
#****************************************************************************
class ServerState:
  def __init__(self):
    self.settings = GameSettings();
    self.game = None; 
    self.currentplayer = 1;
    self.skippedplayers = 0;
 
#****************************************************************************
#Starts a new game, loads the map, adds starting hubs
#****************************************************************************
  def setup_new_game(self):

    if not self.game:
      self.map = Map(self);
      self.game = Game(self.map);

      MapGen(self.map, self.game);

      #FIXME: Need some sort of randomization for the starting hubs

      self.game.create_unit('hub', (20,22), 1, 0);
      self.game.create_unit('hub', (75,52), 2, 0);

      #Initialize main loop callback.
      self.loop = task.LoopingCall(self.mainloop);
      self.loop.start(1.0);


#****************************************************************************
# This method is called every second.
#****************************************************************************
  def mainloop(self):
    #place code here to find out if a player has lost all units and if so declare them dead
    self.connections.remote_all('network_sync');

#****************************************************************************
#add a unit
#****************************************************************************
  def add_unit(self, unit_type, unit_loc, playerID, parentID):
    self.game.create_unit(unit_type, unit_loc, playerID, parentID);

#****************************************************************************
#find and remove all units without any HP remaining
#****************************************************************************
  def process_death(self):
    """This function searches for units without any HP remaining, removes them from the game, then sets the HP of any dependent units connected to them to 0. This function then repeats the process until all dependent units are found and removed"""
    notclear = True; 
    while notclear:
        notclear = False;
        for unit in self.map.unitstore.values():
            if (unit.hp < 1 and unit.typeset != "doodad"):
                notclear = True; 
                self.game.remove_unit(unit);
                #this code is to find and remove all units dependent on the most recently killed unit. This has been disabled as currently parent units are not recognized during unit creation. 
                """for unit2 in self.map.unitstore.values(): 
                    if unit2.parent == unit.id:
                        unit2.hp == 0;"""

#****************************************************************************
#server determines round is over and unskips all units
#****************************************************************************
  def round_over(self):
    self.skippedplayers = 0;

#****************************************************************************
#Find out if a unit is hit or not
#****************************************************************************
  def determine_hit(self, unit, pos):
    x, y = pos;
    power = self.game.get_unit_power(unit);
    for target in self.map.unitstore.values():
        if target.x == x and target.y == y and target.typeset != "doodad":
            target.hp = target.hp - power;

#****************************************************************************
#calculate the number of players currently connected to the game
#****************************************************************************
  def max_players(self, clients):
    q = 0;
    placeholder = 0
    for q in clients:
        placeholder = placeholder + 1;
    return placeholder
#****************************************************************************
#
#****************************************************************************
  def setup_network(self):
    self.connections = ConnectionHandler(self)
    portal = Portal(self.connections);
    checker = InMemoryUsernamePasswordDatabaseDontUse();
    checker.addUser("guest", "guest");
    portal.registerChecker(checker);
    reactor.listenTCP(6112, pb.PBServerFactory(portal));

#****************************************************************************
#
#****************************************************************************
  def run_network(self):

    reactor.run();

