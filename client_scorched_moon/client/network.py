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

import logging
import telnetlib

class Network:
    def __init__(self):
        logging.debug("")

    def connectserver(self):
        
        testdata = "test\n"
        testdata = testdata.encode('ascii')

        mytest = telnetlib.Telnet("127.0.0.1", 6112)
        #mytest.write(testdata)
        mytest.write(str("test\n").encode('ascii'))
        mytest.close()
