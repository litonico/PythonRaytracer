import unittest
from geometry import *
from shapes import *
from utility import *
from pathtracer import *
import os
from Scenes import simple_scene


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
		self.assertEqual(self.ray.getPoint(intersection_pt), Point(1.0,0,0))

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
		self.assertEqual(self.ray.getPoint(intersection_pt), Point(1,0,0))

	def test_plane_normal(self):
		point = Point(0, 1, 0)
		self.assertTrue(isinstance(self.plane.normal(point), Vector))
		self.assertEqual(self.plane.normal(point), Vector(0,1,0) )

class TestColor(unittest.TestCase):
	def setUp(self):
		self.color = Color(1,0,0)

	#def test_range(self):
	#	self.out_of_range = Color(2.5, 133, -5)
	#	self.assertEqual(self.out_of_range, Color(1, 1, 0))

class TestImage(unittest.TestCase):

	def setUp(self):
		self.image = Image(10, 10)

	def test_getting_and_setting_colors_one_sample(self):
		self.image.setPixel(5, 5, Color(0.5, 0.4, 0.5))
		self.assertEqual(self.image.getPixel(5, 5), Color(0.5, 0.4, 0.5))
		self.assertEqual(self.image.getPixel(4, 4), Color(0, 0, 0))
		#check every value for correctness
		for x in range(self.image.width):
			for y in range(self.image.height):
				if x == 5 and y == 5:
					self.assertEqual(self.image.getPixel(x,y), Color(0.5,0.4,0.5))
				else:
					self.assertEqual(self.image.getPixel(x,y), Color(0,0,0))
	
	def xtest_writing_image(self):
		self.image.setPixel(5,5, Color(1, 1, 1))
		self.image.save(1, 'test_writing_image.ppm')
		os.system("open test_writing_image.ppm")

class xTestCamera(unittest.TestCase):
	def setUp(self):
		pass
		

class TestTracing(unittest.TestCase):
	def setUp(self):
		self.camera = Camera(
			Point(-6, 0, 0), #position
			Point(0,0,0),	#lookat
			ImagePlane(300, 300), #image plane
			2	#focal length
			)

		self.scene = Scene(
			"test_scene", 
			self.camera
		)

		self.scene.camera = self.camera
		self.sphere = Sphere(Point(0,1,0), 1)
		self.sphere.emittance = 1
		self.sphere.diffuse = Color(0.5,1,1)
		self.plane = Plane(Point(0,0,0), Vector(0,1,0))
		self.plane.diffuse = Color(1,1,1)
		self.plane.emittance = 1
		self.scene.objects += [self.sphere]

		self.image = Image(300, 300)

	def test_scene_creation(self):
		self.assertEqual(self.scene.objects, [self.sphere])
		self.assertTrue(self.scene.camera.direction, Vector(1,0,0))
		self.assertFalse(Sphere(Point(0,1,0), 1).intersect(self.scene.camera.castRay(0,0)))
		self.assertEqual(self.scene.camera.imageplane.width, 300)
		print "Dir, Right, Up"
		print self.scene.camera.direction
		print self.scene.camera.rightVector
		print self.scene.camera.upVector



	def xtest_check_simple_sphere_intersection(self):

		for x in range(self.image.width):
			for y in range(self.image.height):
				ray = self.scene.camera.castRay(x,y)
				for obj in self.scene.objects:
					self.assertTrue(obj.__class__.__name__ == "Sphere")
					#print obj.intersect(ray)
					if obj.intersect(ray):
						hit =  Color(1,1,1)
					else: hit = Color(0,0,0)
					self.image.setPixel(x, y, hit)
					#if x == 150 and y == 150:
					#	self.assertTrue(obj.intersect(ray))

		self.image.save(1, 'test_intersecting.ppm')
		os.system("open test_intersecting.ppm")

	def test_simple_render(self):

		self.camera = Camera(
			Point(-6, 4, 0), #position
			Point(0,1,0),	#lookat
			ImagePlane(300, 300), #image plane
			2	#focal length
			)

		self.scene.camera = self.camera
		self.scene.objects += [self.plane]

		self.scene.objects = [self.plane, self.sphere]
		print self.scene.objects
			

		Render(self.scene, 1)
		os.system("open test_scene.ppm")

class TestUtilities(unittest.TestCase):
	def setUp(self):
		self.vector = Vector(0,1,0)

	def test_random_normals_in_hemisphere(self):
		for i in range(1000):
			randvector = RandHemisphereNormal(self.vector)
			self.assertTrue(randvector.y >= 0)

if __name__=='__main__':
	unittest.main()