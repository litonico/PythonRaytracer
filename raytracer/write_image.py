class Image():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		# initialize the image with a black background
		self.image = [[Color(0,0,0) for h in range(height)] for h in range(width)]

		def getPixel(self, x, y):
			return self.image[x][y]

		def setPixel(self x, y, color):
			self.image[x][y] = color