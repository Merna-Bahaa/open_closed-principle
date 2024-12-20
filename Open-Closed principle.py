class Shape (ABC):
    def _init_(self, shape_type):
        self.shape_type = shape_type
    @abstractmethod
    def calculate_area(self): 
        pass
class Circle(Shape):
    def _init_(self, radius):
        super()._init_("circle")
        self.radius =radius
    def calculate_area(self):
        return pi* self.radius** 2
class Rectangle(Shape):
    def _init(self, width, height):
        super().init("rectangle")
        self.width= width
        self.height= height
    def calculate_area(self):
        return self.width* self.height
class Square (Shape):
    def init_(self, side):
        super().init_("square")
        self.side = side
    def calculate_area(self):
        return self.side**2
