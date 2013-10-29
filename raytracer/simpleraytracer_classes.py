from math import sqrt
from subprocess import call


Epsilon = 0.0001

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
    def init(self, origin, direction, mint, maxt, depth):
        self.origin = origin
        self.direction = direction
        self.depth = depth
        self.mint = mint
        self.maxt = maxt
    # parenting rays?
    
    
def DiscriminantCheck(A,B,C):
    discriminant = B*B - 4.0*A*C
    if discriminant <= 0.0:
        return False
    else:
        return True
        
def Quadratic(A, B, C):
    discriminant = B*B - 4.0*A*C
    rootDiscriminant = sqrt(discriminant)
    if B < 0:
        q = -0.5*(B - rootDiscriminant)
    else:
        q = -0.5*(B + rootDiscriminant)
    root1 = q/A
    root2 = C/q
    if root1 < root2:
        root1, root2 = root2, root1
    return root1, root2
        
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
        '''
    def intersect(self, ray):
        A = ray.direction.x**2 + ray.direction.y**2 + ray.direction.z**2
        B = 2 * (ray.direction.x*ray.origin.x + ray.direction.y*ray.origin.y + ray.direction.z*ray.origin.z)
        C = ray.origin.x**2 + ray.origin.y**2 - ray.origin.z**2 self.radius**2
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
        '''
                        
class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#### BxDFs ####

class BxDF:
    pass#stuff
    
    
class BRDF(BxDF):
    pass



class ppmBitmap:
    def __init__(self, width, height, name, ls_img_data):
        self.width = width
        self.height = height
        self.name = name
        filename = name + '.ppm'
        self.filename = filename
        self.ls_img_data = ls_img_data # as a list
        self.s_img_data = ' '.join(x for x in ls_img_data) # transforms the list into a space-delimited string
        self.img_file = open(filename, 'w') #creates file with name "name", overwrites if it exists
    
    def write(self):
        self.img_file.write('P6\n%d %d\n255\n' %(self.width, self.height) #basic ppm file format info
        self.img_file.write('')
        #myfile.close()
        
    def view(self):
        displayimg = Image.open(self.filename) 
        displayimg.show()
    
        
class Camera:
    def __init__(position = Point(0,0,0), lookat = Point(1,0,0) ):
        self.lookat = lookat
        self.position = position
        # rotation?
        self.FOV = 45
        
    def setFOV(self, value):
        self.FOV = value


class Scene:
    def __init__(obj_list, lights_list, camera, depth):
        self.obj_list = obj_list
        self.lights_list = lights_list
    
    
    def render(self, canvas):
        pass
        # Compute FOV
        # Render
        
        #for each surface, this is the general rendering loop
        #for light in range(len(lights_list)):
        #    if not is_blocked(lights_list[light]): #should is_blocked be a method of light or of scene?
        #        incident_light = light.L(point)
        #        amount_reflected = 
        #        L += amount_reflected*incident_light
                
'''   
s = Scene(
    [Sphere(Point(2,0,0), 2), ],
    [Light(Point(0.5, 1, 0)) ],
    Camera(Point(0, 0.5, 0), Point(1, 0.5, 0)), 
    3
    )
    
s.render 
'''

### tests ###
#try:
ppmtest_image_data = [255, 0, 0, 
                          0, 255, 0, 
                          0, 0, 255, 
                          255, 255, 0,
                          255, 255, 255,
                          0, 0, 0,
                          0, 255, 255,
                          75, 75, 75,
                          127, 127, 127,
                          150, 150, 150,
                          150, 150, 150,
                          150, 150, 150]
ppmtest_image = ppmBitmap(3, 4, "PPM Test", ppmtest_image_data)
ppmtest_image.write()
ppmtest_image.view()
    
print "bitmap-writing test: passed!"
#except:
print "bitmap-writing test: failed."