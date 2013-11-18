from geometry import *

class Color:
	def __init__(self, red, green, blue):
		self.r = red
		self.g = green
		self.b = blue

	def __repr__(self):
		return str(self.r) + " " + str(self.g) +  " " + str(self.b)

	def __add__(self, other):
		return Color(self.r+other.r, self.g+other.g, self.b+other.b)

	def __sub__(self, other):
		return Color(self.r-other.r, self.g-other.g, self.b-other.b)
	
	def __mul__(self, other):
		return Color(self.r*other.r, self.g*other.g, self.b*other.b)

	def __div__(self, other):
		assert other != 0
		if isinstance(other, Color):
			return Color(self.r/other.r, self.g/other.g, self.b/other.b)
		else:
			return Color(self.r/other, self.g/other, self.b/other)
	
	def __eq__(self, other):
		return (self.r == other.r and self.g == other.g and self.b == other.b)

	def clamp(self, low, high):
		return Color(Clamp(self.r, low, high), 
					 Clamp(self.g, low, high),
					 Clamp(self.b, low, high)
			)
	def add(self, num):
		return Color(self.r + num, 
					 self.g + num,
					 self.b + num)

class Scene:
	def __init__(self, name, camera = None):
		self.name = name
		self.objects = []
		self.camera = camera
		self.background_color = Color(0,0,0)

class ImagePlane:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
class Camera:
	def __init__(self, position, lookat, imageplane, fov):

		self.position = position
		self.direction = Normalize(lookat - position)

		# construct a Vector perpendicular to direction, with y-component 0
		self.rightVector = Normalize(
			Vector(self.position.z, 0.0, 0.0-self.position.x)
			)
		# and an up-vector perpendicular to the other two
		self.upVector = Cross(self.direction, self.rightVector)

		self.imageplane = imageplane
		self.fov = fov
		self.pixelsWidth = fov/float(self.imageplane.width)
		self.pixelsHeight = fov/float(self.imageplane.height)

	def castRay(self, x, y):
		# @refactor: needs a way to deal with non-square images.

		# image plane is a 1x1 square, with imageplane.width divisons horizontally,
		# and imageplane.height divisions vertically
		x = x / float(self.imageplane.width)
		y = y / float(self.imageplane.height)

		x -= 0.5 # offset by half the image plane so that 0,0 is the top-left rather than the middle
		y -= 0.5 

		ray_target = Scalar_mul(self.rightVector, x) + Scalar_mul(self.upVector, y) + Scalar_mul(self.direction, self.fov)

		return Ray(
			self.position,
			ray_target - self.direction
			)

class Image:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		# image is a matrix of empty lists by default
		self.image = [[ Color(0, 0, 0) for i in range(height)] for j in range(width)]

	def getPixel(self, x, y):
		#returns a list of the samples at a pixel
		return self.image[x][y]

	def setPixel(self, x, y, color):
		assert isinstance(color, Color)
		self.image[x][y] += color
		
	def save(self, samples, filename):
		this_file = open(filename, 'w+')
		contents = 'P3\n{0} {1}\n255\n'.format(self.width, self.height)

		for y in range(self.height):
			for x in range(self.width):
				raw_pixel = self.image[x][y]/float(samples)
				assert isinstance(raw_pixel, Color)
				pixel = raw_pixel.clamp(0, 1)

				contents += '{0} {1} {2} '.format(int(255 * pixel.r), int(255 * pixel.g), int(255 * pixel.b))

			contents += '\n'

		this_file.write(contents)
		this_file.close()
