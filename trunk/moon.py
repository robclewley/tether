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

from __future__ import division

import pygame
from pygame.locals import *
import threading
from threading import Thread
from Queue import Queue

WINDOW_SIZE = WINDOW_XSIZE,WINDOW_YSIZE = 800,800

CALL = USEREVENT + 0

def main(game):
    game.showimage("images/600px-Jupiter.jpg")
    text = game.input()
    print text

class Game:
    def __init__(self, mainfn):
        pygame.display.init()
        pygame.font.init()

        pygame.key.set_repeat(250, 50)
        self.keylistener = None

        pygame.display.set_caption("Moonbase Thingy")
        self.window = pygame.display.set_mode(WINDOW_SIZE)

        self.window.fill(color.black)
        pygame.display.update()

        self.mainfn = mainfn
        self.gamelogic = Thread(target=self._go)
        self.gamelogic.start()

        while True:
            e = pygame.event.wait()
            if e.type == KEYDOWN:
                if self.keylistener:
                    self.keylistener(e)
            elif e.type == CALL:
                result = e.fn(*e.args)
                e.respond(result)
            elif e.type == QUIT:
                break

    def _go(self):
        self.mainfn(self)
        pygame.event.post(pygame.event.Event(QUIT))

    def showimage(self, filename):
        call(self._showimage, filename)

    def _showimage(self, filename):
        image = pygame.image.load(filename).convert()
        self.window.blit(image, (0,0))
        pygame.display.update()

    def input(self):
        inputbox = call(InputBox, self.window)
        old = self.keylistener
        self.keylistener = inputbox.key
        text = inputbox.result()
        self.keylistener = old
        return text

def call(fn, *args):
    q = Queue()
    e = pygame.event.Event(CALL, fn=fn, args=args, respond=q.put)
    pygame.event.post(e)
    return q.get()

class InputBox(object):
    def __init__(self, window, rect=None, text=""):
        self.window = window
        self.rect = rect
        if self.rect is None:
            self.rect = Rect(0, WINDOW_YSIZE-50, WINDOW_XSIZE, 50)

        self.background = pygame.Surface(self.rect.size)
        self.background.blit(window, (0,0), self.rect)

        self.font = pygame.font.Font(None, self.rect.height)
        self._text = text

        self.cursor = self.font.render("|", True, color.green)
        self.textwidth = self.rect.width - self.cursor.get_width()

        self.done = threading.Event()

        self.update()

    def _get_text(self):
        return self._text

    def _set_text(self, text):
        self._text = text
        self.update()

    text = property(_get_text, _set_text)

    def key(self, key):
        if key.key == K_BACKSPACE:
            self._text = self._text[:-1]
        elif key.key == K_RETURN:
            self.close()
        else:
            self._text += key.unicode

        self.update()

    def update(self):
        surface = self.font.render(self._text, True, color.white)
        overage = max(0, surface.get_width() - self.textwidth)

        draw = Rect(overage, 0, self.rect.width, self.rect.height)

        self.window.blit(self.background, self.rect)
        drawn = self.window.blit(surface, self.rect, draw)
        self.window.blit(self.cursor, drawn.topright)

        pygame.display.update(self.rect)

    def close(self):
        self.window.blit(self.background, self.rect)
        pygame.display.update(self.rect)
        self.done.set()

    def result(self):
        self.done.wait()
        return self._text

class color:
    def __getattr__(self, name):
        return pygame.Color(name)
    __getitem__ = __getattr__
color = color()

if __name__ == "__main__":
    Game(main)
