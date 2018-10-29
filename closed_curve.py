from shape import *


class ClosedCurve(Shape):
    def __init__(self, locations, color):
        super(ClosedCurve, self).__init__(locations, color)

    @abstractmethod
    def draw_me(self, canvas):
        pass

    @abstractmethod
    def calc_area(self):
        pass

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
