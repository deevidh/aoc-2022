from dave_utils import puzzle

def part1(puzzle_input):
    shape_scores = {
        'X':1,
        'Y':2,
        'Z':3
    }
    round_scores = {
        'A X': 3,
        'A Y': 6,
        'A Z': 0,
        'B X': 0,
        'B Y': 3,
        'B Z': 6,
        'C X': 6,
        'C Y': 0,
        'C Z': 3
    }
    return sum([ round_scores[round] + shape_scores[round[2]] for round in puzzle_input ])

def part2(puzzle_input):
    shape_scores = {
        'A':1,
        'B':2,
        'C':3
    }
    winners = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
    losers = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
    score=0
    for round in puzzle_input:
        match round[2]:
            case "X": # Lose
                must_play=losers[round[0]]
                score+=0+shape_scores[must_play]
            case "Y": # Draw
                must_play=round[0]
                score+=3+shape_scores[must_play]
            case "Z": # Win
                must_play=winners[round[0]]
                score+=6+shape_scores[must_play]
    return score

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,15)
my_puzzle.test(part1,15)

## Part 2
#my_puzzle.test_and_submit(part2,12)
my_puzzle.test(part2,12)