import math
class Point2D():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def coordinates(self):
        return (self.x,self.y)
    def distance(self,p:"Point2D"):
        return math.sqrt(((self.x-p.x)**2-(self.y-p.y)**2))
    def anglTo(self,p:"Point2D"):
        slope=(self.y-p.y)/(self.x-p.x)
        return math.atan(slope)
    def __gt__(self,other):
        if(self.coordinates()>other.coordinates()):
            return True
        else:
            False
    def __str__(self):
        return f"{(self.x,self.y)}"
class Line():
    def __init__(self,p1:Point2D,p2:Point2D):
        
        self.slope=(p2.y-p1.y)/(p2.x-p1.x)
        self.points=[p1,p2]
    def addPoint(self,p:Point2D):
        start=self.points[0]
        slope=(start.y-p.y)/(start.x-p.x)
        if (slope==self.slope):
            self.points.append(p)
            self.points.sort()
        else:
            print(f"{p.coordinates} cannot be added as slope is different")
    def length(self):
        return self.points[0].distance(self.points[-1])
    def displayPoints(self):
        for point in self.points:
            print(f"{point.coordinates()} ",end="")
    def __str__(self):
        s=""
        for point in self.points:
            s+=str(point)+" "
        return f'{s}\nslope = {self.slope}'
    def __len__(self):
        return len(self.points)
