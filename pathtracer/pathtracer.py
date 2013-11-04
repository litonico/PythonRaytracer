'''
Adapted from NIKITA NIKISHIN's simple Python path tracer
'''

from geometry import *
import random as rand
from math import sqrt

def generate_random_hemisphere_normal(v):
	v2 = normalize(Vector(rand.uniform(-1,1), rand.uniform(-1,1), rand.uniform(-1,1)))

def Trace(ray, scene, bounces = 0):
	if n > 10:
		return scene.background_color

	closest_intersection = 1000000.0
	
	for object in scene.objects:

		intersection_pt = object.intersect(ray)

		if intersection_pt and intersection_pt < closest_intersection:
			assert (intersection_pt > 0)
			closest_intersection = intersection_pt
			object_hit = object

		else:
			return scene.background_color

		point = closest_intersection
		normal = object_hit.normal(point)

		rand_direction = generate_random_hemisphere_normal(normal)
		recursive_ray = Ray(point, rand_direction)

		return object_hit.diffuse  * (Trace(recursive_ray, scene, n+1) + object_hit.emittance)