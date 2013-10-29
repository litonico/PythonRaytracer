import unittest
from geometry import *
from shapes import *

class TestSphere(unittest.TestCase):
	def setUp(self):
		self.origin = Point(0,0,0)
		self.ray = Ray(Point(4,0,0), Vector(-1,0,0))
		self.sphere = Sphere(
			self.origin, 1.0
			)
	
	def test__sphere_intersection(self):
		# ray-sphere intersection
		intersection_pt = self.sphere.intersect(self.ray)
		self.assertEqual(intersection_pt, Point(1.0,0,0))

class TestPlane(unittest.TestCase):
	def setUp(self):
		self.origin = Point(0,0,0)
		self.ray = Ray(Point(0,1,0), Vector(1, -1, 0))
		self.plane = Plane(self.origin, Vector(0,1,0) )

	def test__plane_intersection(self):
		intersection_pt = self.plane.intersect(self.ray)
		self.assertEqual(intersection_pt, Point(1,0,0))


if __name__=='__main__':
	unittest.main()