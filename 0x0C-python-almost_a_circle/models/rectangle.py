#!/usr/bin/python3
"""
    Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    '''
        Rectangle class
        Inherits from:
            Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            __width getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setting private attribute
        '''
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            __height getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            set private attribute
        '''
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            __x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            set private attribute
        '''
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            __y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            set private attribute
        '''
        self.validator("y", value)
        self.__y = value

    def area(self):
        '''
            method that returns the area of the rectangle
        '''
        return (self.width * self.height)

    def display(self):
        '''
            method that prints the rectangle area
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + '\n'
        print(rectangle, end="")

    def __str__(self):
        '''
            overloading the str method.
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y,
            self.width, self.height
        )

    def update(self, *args, **kwargs):
        '''
            assigns an argument to each attribute
        '''
        args_len = len(args)
        if args_len == 0 and kwargs is not None:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
            converts the class to a dictionary
        '''
        return {
            "id": self.id, "width": self.width,
            "height": self.height, "x": self.x,
            "y": self.y
        }
