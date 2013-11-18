'''
Adapted from NIKITA NIKISHIN's simple Python path tracer

-LitoNico (github.com/LitoNico)
'''

from geometry import *
from utility import *
import random as rand
from math import sqrt

epsilon = 0.0001

def Trace(ray, scene, bounces = 0):
	if bounces > 10:
		return scene.background_color

	closest_intersection = 1000000.0
	object_hit = False
	
	for obj in scene.objects:
		intersection_pt = obj.intersect(ray)
		
		assert isinstance(intersection_pt, float) or isinstance(intersection_pt, bool)

		if intersection_pt:
			if intersection_pt < closest_intersection: 
				closest_intersection = intersection_pt
				object_hit = obj
	
	if not object_hit:
		return scene.background_color

	point = ray.getPoint(closest_intersection)
	normal = object_hit.normal(point)

	rand_direction = RandHemisphereNormal(normal)
	recursive_ray = Ray(point, rand_direction)

	return (object_hit.diffuse * Trace(recursive_ray, scene, bounces+1)).add(object_hit.emittance)

def Render(scene, samples):
	image = Image(scene.camera.imageplane.width, scene.camera.imageplane.height)
	print "Rendering. . ."
	i = 1
	while i <= samples: 
		#rendering loop!
		print "Pass %s" % i

		for y in range(image.width):
			for x in range(image.height): 
				
				image.setPixel(x, y, 
					Trace(scene.camera.castRay(x,y), scene)
					)

		i += 1
	image.save(samples, scene.name + ".ppm")
	print "Finished!"