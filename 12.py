from dave_utils import puzzle
import numpy as np
import itertools

def get_valid_neighbours(node, height_map):
    valid_neighbours = []
    for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= node[0]+dir[0] < height_map.shape[0] and 0 <= node[1]+dir[1] < height_map.shape[1]:
            if ord(height_map[node[0], node[1]]) - ord(height_map[node[0]+dir[0], node[1]+dir[1]]) <= 1:
                valid_neighbours.append((node[0]+dir[0], node[1]+dir[1]))
    return valid_neighbours

def get_shortest_path_to_node(height_map, target_node, initial_node):
    processed_nodes = set()
    paths = [set([initial_node])]
    # Start building path from the end node
    while True:
        paths.append(set())
        for node in paths[-2]:
            # Get all new nodes that are valid neighbours of the current node
            new_nodes = set(get_valid_neighbours(node, height_map))
            if len(new_nodes) == 0:
                # If there are none then this is a dead end
                continue
            for new_node in new_nodes:
                if new_node not in processed_nodes:
                    # If we haven't already processed this node then add it to the current path
                    paths[-1].add(new_node)
                    processed_nodes.add(new_node)
            if target_node in paths[-1]:
                # Check if we have found a complete path to the start node
                return len(paths)-1

def get_shortest_path_to_value(height_map, value, initial_node):
    processed_nodes = set()
    paths = [set([initial_node])]
    # Start building path from the end node
    while True:
        paths.append(set())
        for node in paths[-2]:
            # Get all new nodes that are valid neighbours of the current node
            new_nodes = set(get_valid_neighbours(node, height_map))
            if len(new_nodes) == 0:
                # If there are none then this is a dead end
                continue
            for new_node in new_nodes:
                if height_map[new_node] == value:
                    # Check if we have found a complete path to the start node
                    return len(paths)-1
                if new_node not in processed_nodes:
                    # If we haven't already processed this node then add it to the current path
                    paths[-1].add(new_node)
                    processed_nodes.add(new_node)

def process_input(input):
    array = np.array([[char for char in row] for row in input])
    start = next ((x,y) for x,y in itertools.product(range(array.shape[0]), range(array.shape[1])) if array[x,y] == 'S')
    end = next ((x,y) for x,y in itertools.product(range(array.shape[0]), range(array.shape[1])) if array[x,y] == 'E')
    array[start] = 'a'
    array[end] = 'z'
    return array, start, end

def part1(input):
    height_map, start, end = process_input(input)
    return get_shortest_path_to_node(height_map, start, end)

def part2(input):
    height_map, start, end = process_input(input)
    return get_shortest_path_to_value(height_map, 'a', end)

my_puzzle = puzzle()

## Part 1
#my_puzzle.test_and_submit(part1,31)
my_puzzle.run(part1)

## Part 2
#my_puzzle.test_and_submit(part2,29)
my_puzzle.run(part2)