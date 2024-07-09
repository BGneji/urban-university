class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = [sides[0]] * self.sides_count if len(sides) == 1 else [1] * self.sides_count
        self.__color = color
        self.filled = False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    @property
    def get_color(self):
        return self.__color

    @property
    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = list(args)

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            return True
        else:
            return False

    def __len__(self):
        return self.__sides[0]


class Circle(Figure):
    sides_count = 1
    PI = 3.14

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = sides
        self.__radius = self.get_sides[0] / (2 * self.PI)

    def get_square(self):
        return 2 * self.PI * self.__radius ** 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = [sides[0]] * self.sides_count if len(sides) == len([self.sides_count]) \
            else [1] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 200), 10, 1)
circle1.set_color(55, 66, 77)
circle1.set_sides(15)  # Изменится
print(circle1.get_color)
print(circle1.get_sides)
print(len(circle1))
print('*' * 12)
cube1 = Cube((222, 35, 130), 6)
cube1.set_color(300, 70, 15)
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_color)
print(cube1.get_sides)
print(cube1.get_volume())
