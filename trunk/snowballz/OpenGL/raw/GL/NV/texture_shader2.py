'''OpenGL extension NV.texture_shader2

Overview (from the spec)
	
	This extension extends the NV_texture_shader functionality to
	support texture shader operations for 3D textures.
	
	See the NV_texture_shader extension for information about the
	texture shader operational model.
	
	The two new texture shader operations are:
	
	<conventional textures>
	
	22.  TEXTURE_3D - Accesses a 3D texture via (s/q,t/q,r/q).
	
	<dot product textures>
	
	23.  DOT_PRODUCT_TEXTURE_3D_NV - When preceded by two DOT_PRODUCT_NV
	     programs in the previous two texture shader stages, computes a
	     third similar dot product and composes the three dot products
	     into (s,t,r) texture coordinate set to access a 3D non-projective
	     texture.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_shader2.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_DOT_PRODUCT_TEXTURE_3D_NV = constant.Constant( 'GL_DOT_PRODUCT_TEXTURE_3D_NV', 0x86EF )


def glInitTextureShader2NV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_NV_texture_shader2' )
