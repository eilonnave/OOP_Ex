from polygon import *
import math


class RightAngleTriangle(Polygon):
    def __init__(self, start_location, l1, l2, color):
        self.l1 = l1
        self.l2 = l2
        self.start_location = start_location
        self.color = color
        locations = self.triangle_locations()
        super(RightAngleTriangle, self).__init__(locations, color)

    def triangle_locations(self):
        locations = self.start_location
        x = self.start_location[0]
        y = self.start_location[1]+self.l1
        locations.append(x)
        locations.append(y)
        x = x+self.l2
        locations.append(x)
        locations.append(y)
        return locations

    def calc_area(self):
        return self.l1 * self.l2 / 2

    def move_me(self, x, y):
        pass

    def animation_on(self):
        pass

    def animation_off(self):
        pass

    def set_fill_color(self):
        pass


class IsoscelesTriangle(Polygon):
    def __init__(self, start_location, l, alpha, color):
        self.l = l
        self.alpha = math.radians(alpha)
        self.start_location = start_location
        locations = self.triangle_locations()
        super(IsoscelesTriangle, self).__init__(locations, color)

    def triangle_locations(self):
        locations = self.start_location
        x = self.start_location[0]+self.l*math.sin(self.alpha/2)
        y = self.start_location[1]+self.l*math.cos(self.alpha/2)
        locations.append(x)
        locations.append(y)
        x = self.start_location[0]-self.l*math.sin(self.alpha/2)
        locations.append(x)
        locations.append(y)
        return locations

    def calc_area(self):
        return self.l * self.l * math.sin(self.alpha)/2

    def move_me(self, x, y):
        pass

    def animation_on(self):
        pass

    def animation_off(self):
        pass

    def set_fill_color(self):
        pass


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, start_location, l, color):
        self.l = l
        self.start_location = start_location
        self.color = color
        super(EquilateralTriangle, self).__init__(self.start_location, l,
                                                  60, self.color)