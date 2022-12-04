from dave_utils import puzzle
import string

def get_common(rucksacks):
    return [ list(
                set(rucksack[0:int(len(rucksack)/2)]) &
                set(rucksack[int(len(rucksack)/2):])
            )[0] for rucksack in rucksacks ]

def get_priorities(items):
    return sum([string.ascii_letters.index(item)+1 for item in items])

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def part1(input):
    return get_priorities(get_common(input))

def part2(input):
    groups=chunker(input,3)
    badges=[]
    for group in groups:
        common = set(group[0]) & set(group[1]) & set(group[2])
        badges.append(list(common)[0])
    return get_priorities(badges)

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,157)
my_puzzle.test(part1,157)

## Part 2
#my_puzzle.test_and_submit(part2,70)
my_puzzle.test(part2,70)