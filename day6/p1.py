from collections import defaultdict
DEV = "example.lst"
PROD = "input.lst"

UP = (-1,0)
DOWN = (1,0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

with open(DEV) as f:
    inp = f.read().splitlines()

    position = [0,0, UP]
    obstacles = set()
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == '^':
                position = [row, col, 0]
            if inp[row][col] == 'v':
                position = [row, col, 2]
            if inp[row][col] == '<':
                position = [row, col, 3]
            if inp[row][col] == '>':
                position = [row, col, 1]
            if inp[row][col] == '#':
                obstacles.add((row, col))

    result = 0
    visited = {(position[0], position[1])}
    count = 0
    while position[0] >= 0 and position[0] < len(inp) and position[1] >= 0 and position[1] < len(inp[0]):
        print(position)
        print(visited)
        print(obstacles)
        visited.add((position[0], position[1]))

        while (position[0] + DIRECTIONS[position[2] % len(DIRECTIONS)][0], position[1] + DIRECTIONS[position[2] % len(DIRECTIONS)][1]) in obstacles:
            position[2] += 1
        position[0] += DIRECTIONS[position[2] % len(DIRECTIONS)][0]
        position[1] += DIRECTIONS[position[2] % len(DIRECTIONS)][1]

    print(len(visited))

