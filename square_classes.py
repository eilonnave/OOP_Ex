from polygon import *
import math


class Parallelogram(Polygon):
    def __init__(self, start_location, l1, l2, alpha, color):
        self.l1 = l1
        self.l2 = l2
        self.alpha = math.radians(alpha)
        self.start_location = start_location
        self.color = color
        locations = self.square_locations()
        super(Parallelogram, self).__init__(locations, color)

    def square_locations(self):
        locations = self.start_location
        x1 = self.start_location[0]+self.l1
        y1 = self.start_location[1]
        locations.append(x1)
        locations.append(y1)
        x3 = self.start_location[0]+self.l2*math.cos(
            self.alpha)
        y3 = self.start_location[1]+self.l2*math.sin(
            self.alpha)
        x2 = x3+self.l1
        y2 = y3
        locations.append(x2)
        locations.append(y2)
        locations.append(x3)
        locations.append(y3)
        return locations

    def calc_area(self):
        return self.l1 * self.l2 * math.sin(self.alpha)

    def move_me(self, x, y):
        pass

    def animation_on(self):
        pass

    def animation_off(self):
        pass

    def set_fill_color(self):
        pass


class Rectangle(Parallelogram):
    def __init__(self, start_location, l1, l2, color):
        self.l1 = l1
        self.l2 = l2
        super(Rectangle, self).__init__(start_location, l1, l2, 90, color)


class Square(Rectangle):
    def __init__(self, start_location, l, color):
        self.l = l
        super(Square, self).__init__(start_location, l, l, color)