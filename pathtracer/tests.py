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
	
	def test_sphere_intersection(self):
		# ray-sphere intersection
		intersection_pt = self.sphere.intersect(self.ray)
		self.assertEqual(intersection_pt, Point(1.0,0,0))

	def test_sphere_normal(self):
		point = Point(0, 2, 0)
		assert isinstance(self.sphere.normal(point), Vector)
		self.assertEqual(self.sphere.normal(point), Vector(0,1,0) )

class TestPlane(unittest.TestCase):
	def setUp(self):
		self.origin = Point(0,0,0)
		self.ray = Ray(Point(0,1,0), Vector(1, -1, 0))
		self.plane = Plane(self.origin, Vector(0,1,0) )

	def test__plane_intersection(self):
		intersection_pt = self.plane.intersect(self.ray)
		self.assertEqual(intersection_pt, Point(1,0,0))

	def test_plane_normal(self):
		point = Point(0, 1, 0)
		assert isinstance(self.plane.normal(point), Vector)
		self.assertEqual(self.plane.normal(point), Vector(0,1,0) )

class TestTrace(unittest.TestCase):
	def setUp(self):
		self.origin = Point(0,0,0)
		self.plane = Plane(self.origin, Vector(0,1,0))
		self.sphere = Sphere(Point(0,1,0), 1)
		self.diffuse = Color(0.8, 0.8, 0.8)
		#scene.add(self.sphere, self.plane)



if __name__=='__main__':
	unittest.main()