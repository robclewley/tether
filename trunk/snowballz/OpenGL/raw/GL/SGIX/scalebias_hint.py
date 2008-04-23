'''OpenGL extension SGIX.scalebias_hint

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/scalebias_hint.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_SCALEBIAS_HINT_SGIX = constant.Constant( 'GL_SCALEBIAS_HINT_SGIX', 0x8322 )


def glInitScalebiasHintSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGIX_scalebias_hint' )
