from geometry import Clamp

class RGBColor:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

class Color:
    def __init__(self, red, green, blue):
        self.r = Clamp(red, 1, 0)
        self.g = Clamp(green, 1, 0)
        self.b = Clamp(green, 1, 0)

    def __repr__(self):
    	return str(self.r) + " " + str(self.g) +  " " + str(self.b)

    def __add__(self, other):
        return Color(self.r+other.r, self.g+other.g, self.b+other.b)

    def __sub__(self, other):
        return Color(self.r-other.r, self.g-other.g, self.b-other.b)
    
    def __mul__(self, other):
        return Color(self.r*other.r, self.g*other.g, self.b*other.b)
    
    def __eq__(self, other):
    	return (self.r == other.r and self.g == other.g and self.b == other.b)

class Scene:
	def __init__(self, objects, camera):
		self.objects = objects
		self.camera = camera
		self.background_color = Color(0,0,0)

class ImagePlane:
	def __init__(self, width, height, offset, pixel_density):
		super(ImagePlane, self).__init__()
		self.width = width
		self.height = height
		self.offset = offset
		self.pixel_density = pixel_density
		self.canvas_width = int(self.width * self.pixel_density)
		self.canvas_height = int(self.height * self.pixel_density)
		

class Camera:
	def __init__(self, position, lookat, imageplane):
		self.position = position
		self.direction = Normalize(position - lookat)
		self.imageplane = imageplane
'''
	def castRay(self):
		x = Vector(x * (self.imageplane.width)/float(self.imageplane.canvas_width)
		return Ray(self.position, 
			)
'''

class Image:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		# image is a matrix of empty lists by default
		self.image = [[ [] for i in range(height)] for j in range(width)]

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
				raw_pixel = self.image[x][y]
				if not raw_pixel: #if the pixel is empty
					pixel = Color(0,0,0)
				else: 
					pixel = sum(raw_pixel)/float(samples)
				# pixel = Clamp(self.image[x][self.height - 1 - y] / float(samples)).list() # I don't understand this line

				contents += '{0} {1} {2} '.format(int(255 * pixel.r), int(255 * pixel.g), int(255 * pixel.b))
			contents += '\n'

		this_file.write(contents)
		this_file.close