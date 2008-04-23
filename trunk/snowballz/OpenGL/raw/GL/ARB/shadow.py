'''OpenGL extension ARB.shadow

Overview (from the spec)
	
	This extension clarifies the GL_SGIX_shadow extension.
	
	This extension supports comparing the texture R coordinate to a depth
	texture value in order to produce a boolean texture value.	This can
	be used to implement shadow maps.
	
	The extension is written in generic terms such that other texture
	comparison modes can be accomodated in the future.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/shadow.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_TEXTURE_COMPARE_MODE_ARB = constant.Constant( 'GL_TEXTURE_COMPARE_MODE_ARB', 0x884C )
GL_TEXTURE_COMPARE_FUNC_ARB = constant.Constant( 'GL_TEXTURE_COMPARE_FUNC_ARB', 0x884D )
GL_COMPARE_R_TO_TEXTURE_ARB = constant.Constant( 'GL_COMPARE_R_TO_TEXTURE_ARB', 0x884E )


def glInitShadowARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_ARB_shadow' )
