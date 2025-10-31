import math
class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[[ {self.x} {self.y} {self.z} ]]"

    def __abs__(self):
        self.length = math.sqrt(self.x**2 + self.y**2 + self.z**2) 
        return self.length
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vector(x, y, z) 

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector(x,y,z)
    
    def __eq__(self, other):
        return  self.x == other.x and self.y == other.y and self.z == other.z

    def __mul__(self, num: int):
        x = self.x * num
        y = self.y * num
        z = self.z * num

        return Vector(x,y,z)

    def __rmul__(self, other):
        return self * other
    
    def __repr__(self):
        return f"Vector{self.x,self.y,self.z}"
    
    def __gt__(self, other):
        # if not isinstance(other, Vector):
        #     # raise TypeError(f"> not supported between instances of " \
        #     # f"Vector' and {type(other)}")
        length = abs(self)
        other = abs(other)
        return length > other
    
    def __ge__(self, other):
        length = abs(self)
        other = abs(other)
        return length >= other
    
    def __lt__(self, other):
        length = abs(self)
        other = abs(other)
        return length < other
    
    def __le__(self, other):
        length = abs(self)
        other = abs(other)
        return length <= other

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x 
        return Vector(x,y,z)
    

if "__main__" == __name__:
    v = Vector(12, 3, 4)
    u = Vector(0, 10, -14)
    w = u + v
    print(w)
    q = abs(v)
    print(q)
    v > 1
