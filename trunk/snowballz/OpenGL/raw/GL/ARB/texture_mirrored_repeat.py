'''OpenGL extension ARB.texture_mirrored_repeat

Overview (from the spec)
	
	ARB_texture_mirrored_repeat extends the set of texture wrap modes to
	include a mode (GL_MIRRORED_REPEAT_ARB) that effectively uses a texture
	map twice as large at the original image in which the additional half,
	for each coordinate, of the new image is a mirror image of the original
	image.
	
	This new mode relaxes the need to generate images whose opposite edges
	match by using the original image to generate a matching "mirror image".

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_mirrored_repeat.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_MIRRORED_REPEAT_ARB = constant.Constant( 'GL_MIRRORED_REPEAT_ARB', 0x8370 )


def glInitTextureMirroredRepeatARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_ARB_texture_mirrored_repeat' )
