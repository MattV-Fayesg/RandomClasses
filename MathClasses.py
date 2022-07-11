class square:

    def __init__(self, side, perimeter=0, area=0):
        self.__side = side
        self.__area = area
        self.__perimeter = perimeter

    @property
    def side(self):
        return self.__side

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @area.setter
    def area(self, area):
        self.__area = area

    @perimeter.setter
    def perimeter(self, perimeter):
        self.__perimeter = perimeter

    def square_area(self):
        if self.side * self.side == self.__area:
            return f'square area is: {self.side * self.side}'
        else:
            self.area = self.side * self.side
            return f'actually square area is: {self.side * self.side}'

    def square_perimeter(self):
        if self.side * 4 == self.__perimeter:
            return f'square perimeter is : {self.side * 4}'
        else:
            self.perimeter = self.side * 4
            return f'actually square perimeter is {self.side * 4}'

    def show_square(self):
        return f'Square side: {self.side}\n' \
               f'Square Area: {self.area}\n' \
               f'Square Perimeter: {self.perimeter}\n'


class rectangle:

    def __init__(self, length, width, area=0, perimeter=0):
        self.__length = length
        self.__width = width
        self.__area = area
        self.__perimeter = perimeter

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @area.setter
    def area(self, area):
        self.__area = area

    @perimeter.setter
    def perimeter(self, perimeter):
        self.__perimeter = perimeter

    def rectangle_area(self):
        if (self.length * self.width) == self.area:
            return self.area
        else:
            self.area = (self.length * self.width)
            return self.area

    def rectangle_perimeter(self):
        if (2 * self.length) + (2 * self.width) == self.perimeter:
            return self.perimeter
        else:
            self.perimeter = (2 * self.length) + (2 * self.width)
            return self.perimeter

    def show_rectangle(self):
        return f'rectangle width: {self.width}\n' \
               f'rectangle length: {self.length}\n' \
               f'rectangle Area: {self.area}\n' \
               f'rectangle Perimeter: {self.perimeter}\n'


class circle:
    pi = 3.141516

    def __init__(self, ray, area=0, perimeter=0):
        self.__ray = ray
        self.__area = area
        self.__perimeter = perimeter

    @property
    def ray(self):
        return self.__ray

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @area.setter
    def area(self, area):
        self.__area = area

    @perimeter.setter
    def perimeter(self, perimeter):
        self.__perimeter = perimeter

    def circle_area(self):
        if circle.pi * (2 * self.ray) == self.area:
            return self.area
        else:
            self.area = circle.pi * (2 * self.ray)
            return self.area

    def circle_perimeter(self):
        if self.perimeter == 2 * circle.pi * self.ray:
            return self.perimeter
        else:
            self.perimeter = 2 * circle.pi * self.ray
            return self.perimeter

    def show_circle(self):
        return f'circle ray: {self.ray}\n' \
               f'rectangle Area: {self.area}\n' \
               f'rectangle Perimeter: {self.perimeter}\n'


# setting objects ----
ball = circle(5)
land = square(10)
scale = rectangle(30, 5)
# calculating
ball.circle_area()
ball.circle_perimeter()
land.square_area()
land.square_perimeter()
scale.rectangle_area()
scale.rectangle_perimeter()
# showing result
print(ball.show_circle())
print(land.show_square())
print(scale.show_rectangle())
