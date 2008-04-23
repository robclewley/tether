'''OpenGL extension EXT.shared_texture_palette

Overview (from the spec)
	
	EXT_shared_texture_palette defines a shared texture palette which may be
	used in place of the texture object palettes provided by
	EXT_paletted_texture. This is useful for rapidly changing a palette
	common to many textures, rather than having to reload the new palette
	for each texture. The extension acts as a switch, causing all lookups
	that would normally be done on the texture's palette to instead use the
	shared palette.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/shared_texture_palette.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_SHARED_TEXTURE_PALETTE_EXT = constant.Constant( 'GL_SHARED_TEXTURE_PALETTE_EXT', 0x81FB )


def glInitSharedTexturePaletteEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_shared_texture_palette' )
