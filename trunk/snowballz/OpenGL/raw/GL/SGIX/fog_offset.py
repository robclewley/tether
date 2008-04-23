'''OpenGL extension SGIX.fog_offset

Overview (from the spec)
	
	This extension allows fragments to look brighter in a foggy
	environment, by biasing the fragment eye-coordinate distance prior
	to fog computation. A reference point in eye space (rx ry rz) and an offset
	amount toward the viewpoint (f_o) are specified. When fog offset is
	enabled, the offset amount will be subtracted from the fragment
	distance, making objects appear less foggy.
	
	If fog computation is done in screen-space coordinates under
	perspective projection, the reference point is used in adjusting the
	fog offset to be correct for fragments whose depth is close to that
	point. The reference point should be redefined when it becomes too
	far away from the primitives being drawn. Under orthographic
	projection, or if fog computation is done in eye-space coordinates,
	the reference point is ignored.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/fog_offset.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_FOG_OFFSET_SGIX = constant.Constant( 'GL_FOG_OFFSET_SGIX', 0x8198 )
GL_FOG_OFFSET_VALUE_SGIX = constant.Constant( 'GL_FOG_OFFSET_VALUE_SGIX', 0x8199 )


def glInitFogOffsetSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGIX_fog_offset' )
