class Shape:
    def __init__(self, kind, width = None, height = None, length = None):
        self.kind = kind
        self.height = height
        self.width = width

    def printer(self):
        print(self.__dict__)

    def area(self):
        if self.kind == 'triangle':
            return 1/2 * self.height * self.width

triangle = Shape('triangle', width = 10, height = 15)
triangle.printer()

print(triangle.area())


