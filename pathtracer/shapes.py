from geometry import *
from math import sqrt
from utility import Color

class Shape(object):
	def __init__(self):
		self.emittance = 0
		self.diffuse = Color(0.5, 0.5, 0.5)

	def intersect(self, ray):
		raise Exception("Unimplemented intersect() Method")
		# each Shape should implement its own intersect method
	def normal(self, point):
		raise Exception("Unimplemented normal() Method")



class Sphere(Shape):
	def __init__(self, center, radius):
		super(Sphere, self).__init__()
		assert isinstance(center, Point)
		self.center = center
		self.radius = radius
	
	def intersect(self, ray):
		# returns the point along the ray where the ray hits the sphere
		distance = ray.origin - self.center
		assert isinstance(distance, Vector)
		B = Dot(distance, ray.direction)
		C = Dot(distance, distance) - self.radius**2
		discriminant = B*B - C

		if discriminant > 0:
			root_1 = (- B - sqrt(discriminant)) 
			root_2 = (- B + sqrt(discriminant)) 

			# returns the position on the ray where the intersection occurs
			if root_1 < root_2:
				return root_1
			else: return root_2

		else: 
			return False # a hit did not occur

	def normal(self, point):
		return Normalize(point - self.center)
						
class Box(Shape):
	def __init__(self, width, height):
		super(Box, self).__init__()
		self.width = width
		self.height = height
	
	def intersect(self, ray):
		pass #uhhh...

		

class Plane(Shape):
	def __init__(self, center, upvector):
		super(Plane, self).__init__()
		self.center = center
		self.upvector = Normalize(upvector)
		
	def intersect(self, ray):
		distance = self.center - ray.origin
		A = Dot(ray.direction, self.upvector)
		if A != 0:
			return (Dot(distance, self.upvector)/A)
		else:
			return False

	def normal(self, point):
		return self.upvector
