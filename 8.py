from dave_utils import puzzle
import numpy as np
import itertools
import math

def get_forest(input):
    return np.array([[int(char) for char in row] for row in input])

# Get the views in each direction from point x, y
def get_views(forest, x, y):
    return {
        "up":    np.flip(forest[:x,y]),
        "down":  forest[x+1:,y],
        "left":  np.flip(forest[x,:y]),
        "right": forest[x,y+1:]
    }

def is_visible(my_height, views):
    return next((True for view in views.values() if len(view) == 0 or my_height > max(view)), False)

def get_scenic_score(my_height, views):
    return math.prod([next((index+1 for index, height in enumerate(view) if height >= my_height), len(view)) for view in views.values()])

def part1(input):
    forest = get_forest(input)
    return sum([is_visible(forest[x][y], get_views(forest, x, y)) for x,y in itertools.product(range(0,forest.shape[0]), range(0,forest.shape[1]))])

def part2(input):
    forest = get_forest(input)
    return max([get_scenic_score(forest[x][y], get_views(forest, x, y)) for x,y in itertools.product(range(0,forest.shape[0]), range(0,forest.shape[1]))])

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,21)
my_puzzle.test(part1,21)

## Part 2
#my_puzzle.test_and_submit(part2,8)
my_puzzle.test(part2,8)