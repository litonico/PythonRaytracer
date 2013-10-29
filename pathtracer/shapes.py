from geometry import *
from math import sqrt
class Shape:
    def intersect(self, ray):
        assert "Unimplemented Intersect Method"
        # each Shape should implement its own intersect method



class Sphere(Shape):
    def __init__(self, center, radius):
        assert isinstance(center, Point)
        self.center = center
        self.radius = radius
        
    def intersect(self, ray):
        # returns the point along the ray where the ray hits the sphere
        distance = ray.origin - self.center
        assert isinstance(distance, Vector)
        B = distance.dot(ray.direction)
        C = distance.dot(distance) - self.radius**2
        discriminant = B*B - C

        if discriminant > 0:
            return ray.origin + ray.direction.scalar_mul((- B - sqrt(discriminant))) # what about -B + sqrt(D)?
        else: 
            return False

        
                        
class Box(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def intersect(self, ray):
        pass #uhhh...
    
class Plane(Shape):
    def __init__(self, center, normal):
        self.center = center
        self.normal = normal
        self