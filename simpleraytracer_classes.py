from math import sqrt

class Vector:
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz
        self.isVector = True
    
    #str, repr, etc
    
    def magnitude(self):
        return sqrt(self.x+self.y+self.z)
    
    def __add__(self, other):
        #if point, return point
        return Vector(self.x + other.x, 
                      self.y + other.y, 
                      self.z + other.z)
                      
    def dot(self, other): # dot product
        return Vector(self.x * other.x, 
                      self.y * other.y, 
                      self.z * other.z)
    
    def __sub__(self, other): 
        return Vector(self.x - other.x, 
                      self.y - other.y, 
                      self.z - other.z)
                      
    def scalar_mul(self, scalar):
        return Vector(self.x * scalar,
                      self.y * scalar,
                      self.z * scalar)
    
    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)
                      
    def normalize(self):
        return scalar_mul(self, 1.0/self.magnitude())
        
    def negate(self):
        return Vector(scalar_mul(self.x, -1.0),
                      scalar_mul(self.z, -1.0),
                      scalar_mul(self.z, -1.0)
        )
    
    def face_out(self, other): #for normals calculation
        if dot(self, other) < 0.0:
            return negate(self)
        else:
            return(self)
        
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)
        
        
class Point: # why not use vectors for everything 
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz
        self.isPoint = True
    
    #str, repr, etc
    
    def __add__(self, other):
        assert other.isVector == True
        return Point(self.x + other.x, 
                      self.y + other.y, 
                      self.z + other.z)
                      
    def __sub__(self, other): # subtracting points gives a vector
        return Vector(self.x - other.x, 
                      self.y - other.y, 
                      self.z - other.z)
                      
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)
        
class Ray:
    def init(self, origin, direction, depth):
        self.origin = origin
        self.direction = direction
        self.depth = depth
    # parenting rays?
        
        
null_Vector = Vector(0,0,0)
null_Point = Point(0,0,0)

class std_basis: # does this need to be a class?
    def __init__(self):
        self.x = Vector(1,0,0)
        self.y = Vector(0,1,0)
        self.z = Vector(0,0,1)

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
        def intersect(self, ray):
            pass
            
class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#### BxDFs ####

class BxDF:
    #stuff
    
    
class BRDF(BxDF):
    



class ppmBitmap:
    def __init__(width, height, name):
        self.width = width
        self.height = height
        self.name = name
    
    def writeBitmap(self):
        myfile.write('P6/n%d %d/n255/n' %(self.width, self.height)) # pixelmap from 0 to 255
        myfile.write()
    
class Camera:
    def __init__(position = Point(0,0,0), lookat = Point(1,0,0) ):
        self.lookat = lookat
        self.position = position
        # rotation?
        self.FOV = 45
        
    def setFOV(self, value):
        self.FOV = value


class Scene:
    def __init__(obj_list = [], lights_list = [], camera, depth):
        self.obj_list = obj_list
        self.lights_list = lights_list
    
    
    def render(self, canvas):
        # Compute FOV
        # Render
        
        #for each surface
        for light in range(len(lights_list)):
            if not is_blocked(lights_list[light]): #should is_blocked be a method of light or of scene?
                incident_light = light.L(point)
                amount_reflected = 
                L += amount_reflected*incident_light
                
            
    
    
    

def viewimage():
    from PIL import Image
    displayimg = Image.open('myfile.ppm')
    displayimg.show()
    print "All Done!"
    
    
    
s = Scene(
    [Sphere(Point(2,0,0), 2), ],
    [Light(Point(0.5, 1, 0)) ],
    Camera(Point(0, 0.5, 0), Point(1, 0.5, 0)), 
    3
    )