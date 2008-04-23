'''OpenGL extension EXT.gpu_program_parameters

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/gpu_program_parameters.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes

glProgramEnvParameters4fvEXT = platform.createExtensionFunction( 
	'glProgramEnvParameters4fvEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glProgramEnvParameters4fvEXT( GLenum(target), GLuint(index), GLsizei(count), GLfloatArray(params) ) -> None',
	argNames = ('target', 'index', 'count', 'params',),
)

glProgramLocalParameters4fvEXT = platform.createExtensionFunction( 
	'glProgramLocalParameters4fvEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glProgramLocalParameters4fvEXT( GLenum(target), GLuint(index), GLsizei(count), GLfloatArray(params) ) -> None',
	argNames = ('target', 'index', 'count', 'params',),
)


def glInitGpuProgramParametersEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_gpu_program_parameters' )
