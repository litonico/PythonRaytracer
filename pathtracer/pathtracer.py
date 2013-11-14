'''
Adapted from NIKITA NIKISHIN's simple Python path tracer

-LitoNico (github.com/LitoNico)
'''

from geometry import *
from utility import *
import random as rand
from math import sqrt


def Trace(ray, scene, bounces = 10):
	if bounces > 10:
		return scene.background_color

	closest_intersection = 1000000.0
	
	for obj in scene.objects:

		intersection_pt = obj.intersect(ray)
		if intersection_pt and (intersection_pt < closest_intersection):
			#try:
			#	assert (intersection_pt > 0)
			#except:
			#	print object
			closest_intersection = intersection_pt
			object_hit = obj

		else:
			return scene.background_color

		point = closest_intersection
		normal = object_hit.normal(point)

		rand_direction = RandHemisphereNormal(normal)
		recursive_ray = Ray(point, rand_direction)
		
		return object_hit.diffuse  * (Trace(recursive_ray, scene, bounces+1).add(object_hit.emittance))

def Render(scene, samples):
	this_camera = scene.camera
	image = Image(this_camera.imageplane.width, this_camera.imageplane.height)
	print "Rendering. . ."
	i = 1
	while i <= samples: 
		#rendering loop!
		print "Pass %s" % i
		for y in range(image.width):
			for x in range(image.height):
				image.setPixel(x, y, 
					Trace(
						this_camera.castRay(x,y), scene
					))
		i += 1
	image.save(samples, scene.name + ".ppm")
	print "Finished!"