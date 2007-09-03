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
import pygame
import moon

WINDOW_SIZE = WINDOW_XSIZE,WINDOW_YSIZE = 550,550

def change_resolution(game):
    text = game.showtext("Enter X dimension", (0,0))
    global WINDOW_XSIZE
    WINDOW_XSIZE = int(game.input())
    game.erasetext(text)
    text = game.showtext("Enter Y dimension", (0,0))
    global WINDOW_YSIZE
    WINDOW_YSIZE = int(game.input())
    global WINDOW_SIZE
    WINDOW_SIZE = WINDOW_XSIZE,WINDOW_YSIZE
    pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.flip()

