import unittest
from geometry import *
from shapes import *
from utility import *
from pathtracer import *
import os
from Scenes import simple_scene

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

		self.scene.background_color = Color(0.4, 0.4, 0.4)

		self.scene.camera = self.camera
		self.sphere = Sphere(Point(0,1,0), 1)
		self.sphere.emittance = 1
		self.sphere.diffuse = Color(0.5,1,1)
		self.plane = Plane(Point(0,0,0), Vector(0,1,0))
		self.plane.diffuse = Color(1,1,1)
		self.scene.objects += [self.sphere]

		self.image = Image(300, 300)

	def test_failure(self):
		self.assertTrue(1 + 1 == 3)

	def test_scene_creation(self):
		self.assertEqual(self.scene.objects, [self.sphere])
		self.assertTrue(self.scene.camera.direction, Vector(1,0,0))
		self.assertFalse(Sphere(Point(0,1,0), 1).intersect(self.scene.camera.castRay(0,0)))
		self.assertEqual(self.scene.camera.imageplane.width, 300)

	def test_check_simple_sphere_intersection(self):

		for x in range(self.image.width):
			for y in range(self.image.height):
				ray = self.scene.camera.castRay(x,y)
				for obj in self.scene.objects:
					self.assertTrue(obj.__class__.__name__ == "Sphere")
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

		Render(self.scene, 3)
		os.system("open test_scene.ppm")


if __name__=='__main__':
	unittest.main()