class figure:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color


class triangle(figure):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height / 2

    def __repr__(self):
        return "This figure is {} and total area is {}".format(
            self.__class__.__name__, self.calculate_area()
        )


class rectangle(figure):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height

    def __repr__(self):
        return "This figure is {} and total area is {}".format(
            self.__class__.__name__, self.calculate_area()
        )


class circle(figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    def calculate_area(self):
        pi = 3.141592653589793
        return self._radius * self._radius * pi

    def __repr__(self):
        return "This figure is {} and total area is {}".format(
            self.__class__.__name__, self.calculate_area()
        )
