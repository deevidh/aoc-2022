from dave_utils import puzzle, chunker

interesting_signal_strengths = [20,60,100,140,180,220]

class CRT:
    def __init__(self):
        self.registers = [(1,"init")]
        self.screen = []

    def add_pixel(self):
        position = (len(self.registers)-1) % 40
        if position >= self.registers[-1][0]-1 and position <= self.registers[-1][0]+1:
            self.screen.append("#")
        else:
            self.screen.append(".")

    def process_instruction(self, instruction):
        existing_register=self.registers[-1]
        if instruction[0] == "noop":
            self.add_pixel()
            self.registers.append((existing_register[0],"noop"))
        elif instruction[0] == "addx":
            self.add_pixel()
            self.registers.append((existing_register[0],f"addx {instruction[1]} [1]"))
            self.add_pixel()
            self.registers.append((existing_register[0] + int(instruction[1]), f"addx {instruction[1]} [2]"))

    def process_instructions(self, instructions):
        for instruction in instructions:
            self.process_instruction(instruction)

    def get_signal_strengths(self, register_nums):
        return [self.registers[register_num-1][0]*register_num for register_num in register_nums]

    def get_picture(self):
        lines = chunker(self.screen, 40)
        return "\n"+str.join("\n", [str.join("", line) for line in lines])

def process_input(input):
    return [tuple(instr) for instr in [line.split() for line in input]]

def part1(input):
    crt=CRT()
    crt.process_instructions(process_input(input))
    return sum(crt.get_signal_strengths(interesting_signal_strengths))

def part2(input):
    crt=CRT()
    crt.process_instructions(process_input(input))
    return crt.get_picture()

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,13140)
my_puzzle.test(part1,13140)

## Part 2
my_puzzle.run(part2)