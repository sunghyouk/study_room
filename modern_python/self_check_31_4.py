from sympy import factor


class Door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False

    def change_state(self):
        self.open = not self.open

    def scale(self):
        self.height *= factor
        self.width *= factor
