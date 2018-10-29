from Tkinter import *
PARALLELOGRAM = 'Parallelogram'
RECTANGLE = 'Rectangle'
SQUARE = 'Square'
RIGHT_ANGLE_TRIANGLE = 'Right Angle Triangle'
ISOSCELES_TRIANGLE = 'Isosceles Triangle'
EQUILATERAL_TRIANGLE = 'Equilateral Triangle'
ELLIPSE = 'Ellipse'
CIRCLE = 'Circle'
BUTTONS_COLOR = 'black'
L1_INSTRUCTION = 'Enter the first length'
WIDTH = 600
HEIGHT = 200


class Screen(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.shapes = []

    def initialize(self):
        b1 = Button(self, text=PARALLELOGRAM, fg=BUTTONS_COLOR
                    , command=self.parallelogram_button)
        b1.grid(row=0, pady=20, padx=10)
        b2 = Button(self, text=RECTANGLE, fg=BUTTONS_COLOR)
        b2.grid(row=1, column=0, pady=20, padx=10)
        b3 = Button(self, text=SQUARE, fg=BUTTONS_COLOR)
        b3.grid(row=2, column=0, pady=20, padx=10)
        b4 = Button(self, text=RIGHT_ANGLE_TRIANGLE, fg=BUTTONS_COLOR)
        b4.grid(row=0, pady=20, padx=10, column=1)
        b5 = Button(self, text=ISOSCELES_TRIANGLE, fg=BUTTONS_COLOR)
        b5.grid(row=1, pady=20, padx=10, column=1)
        b6 = Button(self, text=EQUILATERAL_TRIANGLE, fg=BUTTONS_COLOR)
        b6.grid(row=2, pady=20, padx=10, column=1)
        b7 = Button(self, text=ELLIPSE, fg=BUTTONS_COLOR)
        b7.grid(row=0, pady=20, padx=10, column=2)
        b8 = Button(self, text=CIRCLE, fg=BUTTONS_COLOR)
        b8.grid(row=1, pady=20, padx=10, column=2)
        canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        canvas.grid(column=3)

    def parallelogram_button(self):
        """
        start_location, l1, l2, alpha, color
        """
        l1 = Label(self, text=L1_INSTRUCTION)
        l1.grid(row=3, padx=10)





