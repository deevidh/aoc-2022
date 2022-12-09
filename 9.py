from dave_utils import puzzle

tail_log = []

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}

class Rope:
    def __init__(self, knots=2):
        self.knots = [(0,0) for i in range(knots)]
        self.tail_log = []

    def all_moves(self, instructions):
        for direction, distance in instructions:
            self.move(direction, int(distance))

    def move(self, direction, distance):
        for step in range(distance):
            self.move_head(direction)
            for tail in range(1,len(self.knots)):
                self.move_tail(tail)
            self.log_tail()

    def move_head(self, direction):
        self.knots[0] = tuple(map(lambda x, y: x + y, self.knots[0], directions[direction]))

    def move_tail(self, tail):
        dtail = [0,0]
        dx = self.knots[tail-1][0] - self.knots[tail][0]
        dy = self.knots[tail-1][1] - self.knots[tail][1]

        if abs(dx) > 1 or abs(dy) > 1:
            dtail[0] = dx if abs(dx) == 1 else dx / 2
            dtail[1] = dy if abs(dy) == 1 else dy / 2

        self.knots[tail] = tuple(map(lambda x, y: x + y, self.knots[tail], dtail))

    def log_tail(self):
        self.tail_log.append(self.knots[-1])

def parse_input(input):
    return [tuple(line.split()) for line in input]

def part1(input):
    rope = Rope()
    instructions = parse_input(input)
    rope.all_moves(instructions)
    return len(set(rope.tail_log))

def part2(input):
    rope = Rope(knots=10)
    instructions = parse_input(input)
    rope.all_moves(instructions)
    return len(set(rope.tail_log))

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,13)
my_puzzle.test(part1,88)

## Part 2
#my_puzzle.test_and_submit(part2,36)
my_puzzle.test(part2,36)