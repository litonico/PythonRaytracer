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
	
	def test_intersection(self):
		intersection_pt = self.sphere.intersect(self.ray)
		print intersection_pt
		self.assertEqual(intersection_pt, Point(1.0,0,0))

if __name__=='__main__':
	unittest.main()