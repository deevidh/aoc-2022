from dave_utils import puzzle

def parse_input(input):
    pairs = []
    for pair in input:
        elf1, elf2 = pair.split(",")
        set1 = set(range(int(elf1.split("-")[0]),int(elf1.split("-")[1])+1))
        set2 = set(range(int(elf2.split("-")[0]),int(elf2.split("-")[1])+1))
        pairs.append((set1,set2))
    return pairs

def part1(input):
    pairs = parse_input(input)
    return sum(pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]) for pair in pairs)

def part2(input):
    pairs = parse_input(input)
    return sum(len(pair[0] & pair[1]) > 0 for pair in pairs)

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,2)
my_puzzle.test(part1,2)

## Part 2
#my_puzzle.test_and_submit(part2,4)
my_puzzle.test(part2,4)