from dave_utils import puzzle

def get_calories(puzzle_input):
    elves = []
    while "" in puzzle_input:
        tmp_index = puzzle_input.index("")
        elf, puzzle_input = puzzle_input[:tmp_index], puzzle_input[tmp_index+1:]
        elves.append(elf)
    elves.append(puzzle_input)
    return [sum(list(map(int, x))) for x in elves]

def part1(puzzle_input):
    return max(get_calories(puzzle_input))

def part2(puzzle_input):
    return sum(sorted(get_calories(puzzle_input))[-3:])

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,15)
my_puzzle.test(part1,24000)

## Part 2
#my_puzzle.test_and_submit(part2,12)
my_puzzle.test(part2,45000)