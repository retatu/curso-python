class Line(object):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
    def distancia(self):
        return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
    def distanciaV2(self):
        x1,x2 = self.c1
        y1,y2 = self.c2
        return ((x1-y1)**2 + (x2-y2)**2)**0.5
    def slope(self):
        x1,x2 = self.c1
        y1,y2 = self.c2
        return (y2-x2)/(y1-x1)

class Cylinder(object):
    def __init__(self, heigh=1, radius=1):
        self.heigh = heigh
        self.radius = radius
    volume = lambda self : 3.14*(self.radius**2)*self.heigh
    surface_area = lambda self : 2 * 3.14 * (self.radius**2) + 2 * 3.14 * self.radius * self.heigh



c1 = (3,2)
c2 = (8,10)
l1 = Line(c1,c2)
print(l1.distancia())
print(l1.distanciaV2())
print(l1.slope())

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
