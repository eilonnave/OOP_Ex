from shape import *


class Polygon(Shape):
    __metaclass__ = ABCMeta

    def __init__(self, locations, color):
        super(Polygon, self).__init__(locations, color)
        self.locations = locations
        self.color = color

    def draw_me(self, canvas):
        canvas.create_polygon(self.locations, fill=self.color)

    @abstractmethod
    def calc_area(self):
        return

    @abstractmethod
    def move_me(self, x, y):
        pass

    @abstractmethod
    def animation_on(self):
        pass

    @abstractmethod
    def animation_off(self):
        pass

    @abstractmethod
    def set_fill_color(self):
        pass
