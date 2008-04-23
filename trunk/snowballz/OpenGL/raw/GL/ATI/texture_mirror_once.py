'''OpenGL extension ATI.texture_mirror_once

Overview (from the spec)
	
	ATI_texture_mirror_once extends the set of texture wrap modes to 
	include two modes (GL_MIRROR_CLAMP_ATI, GL_MIRROR_CLAMP_TO_EDGE_ATI) 
	that effectively use a texture map twice as large as the original image 
	in which the additional half of the new image is a mirror image of the 
	original image.
	
	This new mode relaxes the need to generate images whose opposite edges
	match by using the original image to generate a matching "mirror image".
	This mode allows the texture to be mirrored only once in the negative
	s, t, and r directions.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ATI/texture_mirror_once.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_MIRROR_CLAMP_ATI = constant.Constant( 'GL_MIRROR_CLAMP_ATI', 0x8742 )
GL_MIRROR_CLAMP_TO_EDGE_ATI = constant.Constant( 'GL_MIRROR_CLAMP_TO_EDGE_ATI', 0x8743 )


def glInitTextureMirrorOnceATI():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_ATI_texture_mirror_once' )
