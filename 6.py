from dave_utils import puzzle

def find_packet_marker(marker_length, buffer):
    for i in range(marker_length,len(buffer)+1):
        if len(set(buffer[i-marker_length:i])) == marker_length:
            return i

def part1(input):
    return find_packet_marker(4, input[0])

def part2(input):
    return find_packet_marker(14, input[0])

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,7)
my_puzzle.test(part1,7)

## Part 2
#my_puzzle.test_and_submit(part2,19)
my_puzzle.test(part2,19)