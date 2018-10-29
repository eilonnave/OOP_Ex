# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    def __init__(self, locations, color):
        self.locations = locations
        self.animation = False
        self.color = color

    @abstractmethod
    def draw_me(self, canvas):
        """
        the function draws the shape on the screen
        :canvas: the canvas that the shape will be on
        """
        pass

    @abstractmethod
    def calc_area(self):
        """
        the function calculates the shape's area
        """
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





