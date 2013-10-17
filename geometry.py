

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
        
        
class Point:
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

class Basis:
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz
        
std_basis = Basis(Vector(1,0,0),
                  Vector(0,1,0),
                  Vector(0,0,1)
                  )
        
class RGBColor:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue
         
# Vector methods
def Distance(vec1, vec2):
    return sqrt()
    
def Dot(vec1, vec2):
    return Vector(vec1.x * vec2.x, 
                  vec1.y * vec2.y, 
                  vec1.z * vec2.z)
                  
def Cross(vec1, vec2):
    return Vector(vec1.y * vec2.z - vec1.z * vec2.y,
                  vec1.z * vec2.x - vec1.x * vec2.z,
                  vec1.x * vec2.y - vec1.y * vec2.x)

def Scalar_mul(vec1, scalar):
        return Vector(self.x * scalar,
                      self.y * scalar,
                      self.z * scalar)

def Normalize(vec1):
    return Scalar_mul(vec1, 1.0/vec1.magnitude())
