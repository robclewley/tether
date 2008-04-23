'''OpenGL extension SGIX.list_priority

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.list_priority to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIX.list_priority import *
### END AUTOGENERATED SECTION