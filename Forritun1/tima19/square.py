from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def get_area(self):
        return super().get_area()
    
    def get_perimeter(self):
        return super().get_perimeter()






