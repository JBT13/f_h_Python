class Shape:
    def __init__(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with area of {self.area:.2f} and perimeter of {self.perimeter:.2f}"
    
