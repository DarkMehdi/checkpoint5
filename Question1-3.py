class Point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def points (self):
        return self.x,self.y,self.z
mypoint=Point3D(9,10,5)
mypoint.points()

class rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def perimiter (self):
        rr=(self.height+self.width)*2
        print(rr)
    def area (self):
        sr=self.height*self.width
        print(sr)
myrec=rectangle(9,6)
myrec.perimiter()
myrec.area()

class circle:
    def __init__(self,radius):
        self.radius=radius
    def cperimiter (self):
        rc=self.radius*2*3.14
        print(rc)
    def carea (self):
        sc=self.radius*self.radius*3.14
        print(sc)
    def isinside (self):
        print("x=")
        x=int(input())
        print("y=")
        y=int(input())
        if self.radius**2 == x**2 +y**2 :
            print("point is in circle")
        else:
            print("point is not in circle")
mycircle=circle(4)
mycircle.cperimiter()
mycircle.carea()
mycircle.isinside()