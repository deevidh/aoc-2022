from dave_utils import puzzle

def parse_stacks(input):
    stacks_input = [row for row in input if "[" in row]
    columns = int((len(stacks_input[0])+1)/4) # This logic supports a max of 9 columns
    stacks = [[] for i in range(columns)]
    for row in stacks_input:
        for column in range(columns):
            box = row[(column*4)+1]
            if box != " ": stacks[column].insert(0, box)
    return stacks

def parse_instructions(input):
    instructions = [[int(i) for i in row.split() if i.isdigit()] for row in input if "move" in row ]
    return instructions

def get_top_boxes(stacks):
    return "".join([stack.pop() for stack in stacks])

def part1(input):
    stacks = parse_stacks(input)
    instructions = parse_instructions(input)
    for num, frm, to in instructions:
        for num in range(num):
            stacks[to-1].append(stacks[frm-1].pop())
    return get_top_boxes(stacks)

def part2(input):
    stacks = parse_stacks(input)
    instructions = parse_instructions(input)
    for num, frm, to in instructions:
        get_boxes=stacks[frm-1][-num:]
        del stacks[frm-1][-num:]
        stacks[to-1].extend(get_boxes)
    return get_top_boxes(stacks)

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,"CMZ")
my_puzzle.test(part1,"CMZ")

## Part 2
#my_puzzle.test_and_submit(part2,"MCD")
my_puzzle.test(part2,"MCD")