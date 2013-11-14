from geometry import *
from math import sqrt
class Shape:
    def __init__(self):
        self.emittance = 0

    def intersect(self, ray):
        raise Exception("Unimplemented intersect() Method")
        # each Shape should implement its own intersect method
    def normal(self, point):
        raise Exception("Unimplemented normal() Method")



class Sphere(Shape):
    def __init__(self, center, radius):
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
            ''' - B - sqrt(discriminant) returns the distance along the ray where the intersection occurs. This transforms that into an instance of Point'''
            return ray.origin + ray.direction.scalar_mul((- B - sqrt(discriminant))) # what about -B + sqrt(D)? A and B are always positive, so this will give the closest root
        else: 
            return False # a hit did not occur

    def normal(self, point):
        return Normalize(point - self.center)
                        
class Box(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def intersect(self, ray):
        pass #uhhh...
    
class Plane(Shape):
    def __init__(self, center, upvector):
        self.center = center
        self.upvector = Normalize(upvector)
        
    def intersect(self, ray):
        distance = self.center - ray.origin
        A = Dot(ray.direction, self.upvector)
        if A != 0:
            return ray.origin + ray.direction.scalar_mul(Dot(distance, self.upvector)/A)

    def normal(self, point):
        return self.upvector
