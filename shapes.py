class Shape:
    def intersect(self, ray):
        assert "Unimplemented Intersect Method"
        #each Shape should implement its own intersect method

class Sphere():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def intersect(self, ray):
        A = ray.direction.x**2 + ray.direction.y**2 + ray.direction.z**2
        B = 2 * (ray.direction.x*ray.origin.x + ray.direction.y*ray.origin.y + ray.direction.z*ray.origin.z)
        C = ray.origin.x**2 + ray.origin.y**2 - ray.origin.z**2 - self.radius**2
        if not DiscriminantCheck(A,B,C):
            return False
        root1, root2 = Quadratic(A,B,C)
        if root1 > ray.maxt or root2 < ray.mint:
            return False
        thit = root1
        if root1 < ray.mint:
            thit = root2
            if thit > ray.maxt:
                return False
        return thit
        
                        
class Box(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def intersect(self, ray):
        pass #uhhh...
        