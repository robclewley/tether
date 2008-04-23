'''OpenGL extension SGIS.point_line_texgen

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIS/point_line_texgen.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_EYE_DISTANCE_TO_POINT_SGIS = constant.Constant( 'GL_EYE_DISTANCE_TO_POINT_SGIS', 0x81F0 )
GL_OBJECT_DISTANCE_TO_POINT_SGIS = constant.Constant( 'GL_OBJECT_DISTANCE_TO_POINT_SGIS', 0x81F1 )
GL_EYE_DISTANCE_TO_LINE_SGIS = constant.Constant( 'GL_EYE_DISTANCE_TO_LINE_SGIS', 0x81F2 )
GL_OBJECT_DISTANCE_TO_LINE_SGIS = constant.Constant( 'GL_OBJECT_DISTANCE_TO_LINE_SGIS', 0x81F3 )
GL_EYE_POINT_SGIS = constant.Constant( 'GL_EYE_POINT_SGIS', 0x81F4 )
GL_OBJECT_POINT_SGIS = constant.Constant( 'GL_OBJECT_POINT_SGIS', 0x81F5 )
GL_EYE_LINE_SGIS = constant.Constant( 'GL_EYE_LINE_SGIS', 0x81F6 )
GL_OBJECT_LINE_SGIS = constant.Constant( 'GL_OBJECT_LINE_SGIS', 0x81F7 )


def glInitPointLineTexgenSGIS():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGIS_point_line_texgen' )
