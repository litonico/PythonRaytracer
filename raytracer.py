from math import sqrt
import geometry
import shapes
        

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
        self.s_img_data = ' '.join(chr(x) for x in ls_img_data) # transforms the list into a space-delimited list of hex doubles
        self.img_file = open(filename, 'w') #creates file with name "name", overwrites if it exists
    
    def write(self):
        self.img_file.write('P6\n%d %d\n255\n%s' %(self.width, self.height, self.s_img_data))
        
    def view(self):
        displayimg = Image.open(self.filename) 
        displayimg.show()
    
        
class Camera:
    def __init__(position = Point(0,0,0), lookat = Point(1,0,0) ):
        self.direction = direction
        self.position = position
        # rotation?
        self.FOV = 45
        
    def setFOV(self, value):
        self.FOV = value
    
    def lookat(self, point):
        pass

class Sampler:
    def __init__(self, arg):
        self.arg = arg
        

class Scene:
    def __init__(obj_list, lights_list, depth, rays_per_px = 1):
        self.obj_list = obj_list
        self.lights_list = lights_list
    
  
  
  
    
def render(canvas, scene, camera):
    obj_list = scene.obj_list
    camera_direction = camera.direction
    upvector = std_basis.y #always
    
    # Compute FOV
    # Render
    background_color = Color(0,0,0)
    
    for x in range(canvas.width, 0, -1):
        for y in range(canvas.height, , 0, -1): # For each pixel in the image,
            for obj in enumerate(obj_list): # check if a ray shot through that pixel
                hit = obj.intersect(ray)    # intersects an object.
                if hit is not False:        # if it does, 
                    distance = Distance(camera.position, hit)
        
            #for r in range(rays_per_px):
            
            
    
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