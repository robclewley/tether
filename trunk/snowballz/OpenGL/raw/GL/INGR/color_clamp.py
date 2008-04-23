'''OpenGL extension INGR.color_clamp

Overview (from the spec)
	
	Various RGBA color space conversions require clamping to values
	in a more constrained range than [0, 1].  This extension allows
	the definition of independent color clamp values for each of the
	four color components as part of the Final Conversion in the pixel
	transfer path for draws, reads, and copies.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/INGR/color_clamp.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_RED_MIN_CLAMP_INGR = constant.Constant( 'GL_RED_MIN_CLAMP_INGR', 0x8560 )
glget.addGLGetConstant( GL_RED_MIN_CLAMP_INGR, (1,) )
GL_GREEN_MIN_CLAMP_INGR = constant.Constant( 'GL_GREEN_MIN_CLAMP_INGR', 0x8561 )
glget.addGLGetConstant( GL_GREEN_MIN_CLAMP_INGR, (1,) )
GL_BLUE_MIN_CLAMP_INGR = constant.Constant( 'GL_BLUE_MIN_CLAMP_INGR', 0x8562 )
glget.addGLGetConstant( GL_BLUE_MIN_CLAMP_INGR, (1,) )
GL_ALPHA_MIN_CLAMP_INGR = constant.Constant( 'GL_ALPHA_MIN_CLAMP_INGR', 0x8563 )
glget.addGLGetConstant( GL_ALPHA_MIN_CLAMP_INGR, (1,) )
GL_RED_MAX_CLAMP_INGR = constant.Constant( 'GL_RED_MAX_CLAMP_INGR', 0x8564 )
glget.addGLGetConstant( GL_RED_MAX_CLAMP_INGR, (1,) )
GL_GREEN_MAX_CLAMP_INGR = constant.Constant( 'GL_GREEN_MAX_CLAMP_INGR', 0x8565 )
glget.addGLGetConstant( GL_GREEN_MAX_CLAMP_INGR, (1,) )
GL_BLUE_MAX_CLAMP_INGR = constant.Constant( 'GL_BLUE_MAX_CLAMP_INGR', 0x8566 )
glget.addGLGetConstant( GL_BLUE_MAX_CLAMP_INGR, (1,) )
GL_ALPHA_MAX_CLAMP_INGR = constant.Constant( 'GL_ALPHA_MAX_CLAMP_INGR', 0x8567 )
glget.addGLGetConstant( GL_ALPHA_MAX_CLAMP_INGR, (1,) )


def glInitColorClampINGR():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_INGR_color_clamp' )
