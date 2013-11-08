from math import sqrt
Epsilon = 0.0001

class Vector:
	def __init__(self, xx, yy, zz):
		self.x = xx
		self.y = yy
		self.z = zz
		self.isVector = True
	
	#str, repr, etc
	def __repr__(self):
		return str((self.x, self.y, self.z))
	
	
	def magnitude(self):
		return sqrt(self.x**2+self.y**2+self.z**2)
	
	def __add__(self, other):
		#if point, return point
		return Vector(self.x + other.x, 
					  self.y + other.y, 
					  self.z + other.z)
					  
	def dot(self, other): # dot product
		return (self.x * other.x + self.y * other.y + self.z * other.z)
	
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
		return Scalar_mul(self, 1.0/self.magnitude())
		
	def negate(self):
		return Vector(self.x * -1.0,
					  self.z * -1.0,
					  self.z, * 1.0
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
	def __repr__(self):
		return str((self.x, self.y, self.z))
	
	
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
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = Normalize(direction)

	# parenting rays?
		
null_Vector = Vector(0,0,0)
origin = Point(0,0,0)

class Basis:
	def __init__(self, xx, yy, zz):
		self.x = xx
		self.y = yy
		self.z = zz
		
std_basis = Basis(Vector(1,0,0),
				  Vector(0,1,0),
				  Vector(0,0,1)
				  )
		 
# Vector methods
def Distance(vec1, vec2):
	return sqrt(vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z)
	
def Dot(vec1, vec2):
	return (vec1.x * vec2.x+ 
			vec1.y * vec2.y+
			vec1.z * vec2.z)
				  
def Cross(vec1, vec2):
	return Vector(vec1.y * vec2.z - vec1.z * vec2.y,
				  vec1.z * vec2.x - vec1.x * vec2.z,
				  vec1.x * vec2.y - vec1.y * vec2.x)

def Scalar_mul(vec1, scalar):
	return Vector(vec1.x * scalar,
				  vec1.y * scalar,
				  vec1.z * scalar)

def Normalize(vec1):
	return Scalar_mul(vec1, 1.0/vec1.magnitude() )

# other utility methods
def Clamp(n, low, high):
	if n > high:
		return high
	elif n < low:
		return low
	else: return n



