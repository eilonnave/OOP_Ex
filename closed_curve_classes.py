from closed_curve import *
import math


class Ellipse(ClosedCurve):
    def __init__(self, start_location, a, b, color):
        self.a = a
        self.b = b
        self.color = color
        self.start_location = start_location
        self.locations = self.ellipse_locations()
        super(Ellipse, self).__init__(self.locations, color)

    def draw_me(self, canvas):
        canvas.create_oval(self.locations, fill=self.color)

    def ellipse_locations(self):
        locations = self.start_location
        locations.append(self.start_location[0]+self.a)
        locations.append(self.start_location[1]+self.b)
        return locations

    def calc_area(self):
        return self.a*self.b*math.pi

    def move_me(self, x, y):
        pass

    def animation_on(self):
        pass

    def animation_off(self):
        pass

    def set_fill_color(self):
        pass


class Circle(Ellipse):
    def __init__(self, start_location, r, color):
        self. r = r
        self.color = color
        super(Circle, self).__init__(start_location, r, r, color)