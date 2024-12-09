from collections import defaultdict
from copy import deepcopy

DEV = "example.lst"
PROD = "input.lst"

UP = (-1,0)
DOWN = (1,0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

def run(start, inp, obstacles):
    result = 0
    visited = set() 
    count = 0
    while position[0] >= 0 and position[0] < len(inp) and position[1] >= 0 and position[1] < len(inp[0]):
        if (position[0], position[1], position[2] % len(DIRECTIONS)) in visited:
            return visited, True
        visited.add((position[0], position[1], position[2] % len(DIRECTIONS)))

        while (position[0] + DIRECTIONS[position[2] % len(DIRECTIONS)][0], position[1] + DIRECTIONS[position[2] % len(DIRECTIONS)][1]) in obstacles:
            position[2] += 1
        position[0] += DIRECTIONS[position[2] % len(DIRECTIONS)][0]
        position[1] += DIRECTIONS[position[2] % len(DIRECTIONS)][1]

    return visited, False

with open(PROD) as f:
    inp = f.read().splitlines()

    original_position = [0,0, UP]
    obstacles = set()
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == '^':
                original_position = [row, col, 0]
            if inp[row][col] == 'v':
                original_position = [row, col, 2]
            if inp[row][col] == '<':
                original_position = [row, col, 3]
            if inp[row][col] == '>':
                original_position = [row, col, 1]
            if inp[row][col] == '#':
                obstacles.add((row, col))

    position = deepcopy(original_position)
    visited, _ = run(position, inp, obstacles)

    ## PART 2
    result = 0
    loops = set()
    for new_obstruction in visited:
        position = deepcopy(original_position)
        obstacles.add((new_obstruction[0], new_obstruction[1]))
        _, loop = run(position, inp, obstacles)
        obstacles.remove((new_obstruction[0], new_obstruction[1]))
        if loop:
            loops.add((new_obstruction[0], new_obstruction[1]))

    print(len(loops))
