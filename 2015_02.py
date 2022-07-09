from puzzle.input import get_puzzle_input


class Box:

    def __init__(self, sides):
        self.sides = sides
        self.parse_sides()
        self.get_sm_sides()

    def parse_sides(self):
        [l, w, h] = self.sides.split('x')
        self.sides = [int(l), int(w), int(h)]

    def get_sm_sides(self):
        self.sm_sides = self.sides[:]
        self.sm_sides.remove(max(self.sm_sides))

    def surface_area(self):
        [l, w, h] = self.sides
        return 2*l*w + 2*w*h + 2*h*l

    def area(self):
        res = 1
        for i in self.sm_sides:
            res = res * i
        return res

    def perimeter(self):
        return sum([2*i for i in self.sm_sides])

    def volume(self):
        [l, w, h] = self.sides
        return l*w*h


if __name__ == '__main__':
    wrapping_paper = 0
    ribbon = 0

    # Test Data
    # dimensions = ['2x3x4']
    # dimensions = ['1x1x10']
    dimensions = get_puzzle_input(2015, 2).split('\n')

    for d in dimensions:
        box = Box(d)
        wrapping_paper += box.surface_area() + box.area()
        ribbon += box.perimeter() + box.volume()
    print(f'part 1:\n{wrapping_paper}')
    print(f'part 2:\n{ribbon}')
