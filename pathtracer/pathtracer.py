from geometry import *
import random as rand
from math import sqrt

def generate_random_hemisphere_normal(v):
	v2 = normalize(Vector(rand.uniform(-1,1), rand.uniform(-1,1), rand.uniform(-1,1)))

black = Color(0,0,0)

def Trace(ray, scene, bounces = 0):
	if n > 10:
		return black

	result = 1000000.0
	hit = False
	for object in scene.objects:
		test = object.intersect(ray)
		if test and 0 < test < result
			result = test
			hit = object

		if not hit:
			return black
		