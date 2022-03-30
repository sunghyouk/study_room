# Stack 객체 구현하기

class Stack(object):
    def __init__(self):
        self.stack = []

    def get_stack_elements(self):
        return self.stack.copy()

    def add_one(self, item):
        self.stack.append(item)

    def add_many(self, item, n):
        for i in range(n):
            self.stack.append(item)

    def remove_one(self):
        self.stack.pop()

    def remove_many(self, n):
        for i in range(n):
            self.stack.pop()

    def size(self):
        return len(self.stack)

    def prettyprint(self):
        for thing in self.stack[::-1]:
            print('|_ ', thing, ' _|')

    def add_list(self, L):
        for e in L:
            self.stack.append(e)

# from q31_1


class Circle(object):
    def __init__(self):
        self.radius = 0

    def change_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self, radius):
        return 3.14 * radius ** 2

# from q31_2


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
