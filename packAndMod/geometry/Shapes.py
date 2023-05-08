class Rectangle():
    def __init__(self,l:float,b:float):
        self.l=l
        self.b=b
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b
    def __str__(self):
        return f"length : {self.l}\nbreadth : {self.b}"
    def __gt__(self,other:"Rectangle"):
        return self.area()>other.area()
    def __lt__(self,other:"Rectangle"):
        return self.area()<other.area()
    def __eq__(self, __value: "Rectangle") -> bool:
        return self.area()==__value.area()
class Circle():
    pi=(22/7)
    def __init__(self,radius:float):
        self.r=radius
    def perimeter(self)->float:
        return 2*self.pi*self.r
    def area(self):
        return self.pi*self.r**2
    def __str__(self):
        return f"Radius : {self.r}\nArea : {self.area()}"
    def __gt__(self,other):
        return self.r>other.r
    def __lt__(self,other):
        return self.r<other.r
    def __len__(self):
        return self.perimeter
    def __eq__(self,other):
        return self.r==other.r