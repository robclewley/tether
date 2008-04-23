'''OpenGL extension ARB.multisample

Overview (from the spec)
	
	This extension provides a mechanism to antialias all GL primitives:
	points, lines, polygons, bitmaps, and images.  The technique is to
	sample all primitives multiple times at each pixel.  The color
	sample values are resolved to a single, displayable color each time
	a pixel is updated, so the antialiasing appears to be automatic at
	the application level.  Because each sample includes depth and
	stencil information, the depth and stencil functions perform
	equivalently to the single-sample mode.
	
	An additional buffer, called the multisample buffer, is added to
	the framebuffer.  Pixel sample values, including color, depth, and
	stencil values, are stored in this buffer.	When the framebuffer
	includes a multisample buffer, it does not also include separate
	depth or stencil buffers, even if the multisample buffer does not
	store depth or stencil values.  Color buffers (left/right, front/
	back, and aux) do coexist with the multisample buffer, however.
	
	Multisample antialiasing is most valuable for rendering polygons,
	because it requires no sorting for hidden surface elimination, and
	it correctly handles adjacent polygons, object silhouettes, and
	even intersecting polygons.  If only points or lines are being
	rendered, the "smooth" antialiasing mechanism provided by the base
	GL may result in a higher quality image.  This extension is
	designed to allow multisample and smooth antialiasing techniques
	to be alternated during the rendering of a single scene.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/multisample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_MULTISAMPLE_ARB = constant.Constant( 'GL_MULTISAMPLE_ARB', 0x809D )
glget.addGLGetConstant( GL_MULTISAMPLE_ARB, (1,) )
GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = constant.Constant( 'GL_SAMPLE_ALPHA_TO_COVERAGE_ARB', 0x809E )
glget.addGLGetConstant( GL_SAMPLE_ALPHA_TO_COVERAGE_ARB, (1,) )
GL_SAMPLE_ALPHA_TO_ONE_ARB = constant.Constant( 'GL_SAMPLE_ALPHA_TO_ONE_ARB', 0x809F )
glget.addGLGetConstant( GL_SAMPLE_ALPHA_TO_ONE_ARB, (1,) )
GL_SAMPLE_COVERAGE_ARB = constant.Constant( 'GL_SAMPLE_COVERAGE_ARB', 0x80A0 )
glget.addGLGetConstant( GL_SAMPLE_COVERAGE_ARB, (1,) )
GL_SAMPLE_BUFFERS_ARB = constant.Constant( 'GL_SAMPLE_BUFFERS_ARB', 0x80A8 )
glget.addGLGetConstant( GL_SAMPLE_BUFFERS_ARB, (1,) )
GL_SAMPLES_ARB = constant.Constant( 'GL_SAMPLES_ARB', 0x80A9 )
glget.addGLGetConstant( GL_SAMPLES_ARB, (1,) )
GL_SAMPLE_COVERAGE_VALUE_ARB = constant.Constant( 'GL_SAMPLE_COVERAGE_VALUE_ARB', 0x80AA )
glget.addGLGetConstant( GL_SAMPLE_COVERAGE_VALUE_ARB, (1,) )
GL_SAMPLE_COVERAGE_INVERT_ARB = constant.Constant( 'GL_SAMPLE_COVERAGE_INVERT_ARB', 0x80AB )
glget.addGLGetConstant( GL_SAMPLE_COVERAGE_INVERT_ARB, (1,) )
GL_MULTISAMPLE_BIT_ARB = constant.Constant( 'GL_MULTISAMPLE_BIT_ARB', 0x20000000 )
glSampleCoverageARB = platform.createExtensionFunction( 
	'glSampleCoverageARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLclampf, constants.GLboolean,),
	doc = 'glSampleCoverageARB( GLclampf(value), GLboolean(invert) ) -> None',
	argNames = ('value', 'invert',),
)


def glInitMultisampleARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_ARB_multisample' )
