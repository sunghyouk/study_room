
class Circle(object):
    def __init__(self):
        self.radius = 0

    def change_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self, radius):
        return 3.14 * radius ** 2


area = Circle()
area.get_area(3)
