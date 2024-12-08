from collections import defaultdict
from itertools import combinations
TEST1 = "test1.lst"
TEST2 = "test2.lst"
DEV = "example.lst"
PROD = "input.lst"

def get_antenna_map(inp):
    antenna_map = defaultdict(list)
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] != '.':
                antenna_map[inp[row][col]].append((row,col))

    return antenna_map

def get_antinodes(inp, antenna_map):
    antinodes = set()
    for ant_type, ant_locs in antenna_map.items():
        for first, second in combinations(ant_locs, 2):
            diff_row = first[0] - second[0]
            diff_col = first[1] - second[1]
            antinodes.add(first)
            antinodes.add(second)
            hops = 1
            test = (first[0] + (diff_row*hops), first[1] + (diff_col*hops))
            while not out_of_range(test[0], test[1], inp):
                if (test != first and test != second):
                    antinodes.add(test)
                hops += 1
                test = (first[0] + (diff_row*hops), first[1] + (diff_col*hops))
            hops = 1
            test = (first[0] - (diff_row*hops), first[1] - (diff_col*hops))
            while not out_of_range(test[0], test[1], inp):
                if (test != first and test != second):
                    antinodes.add(test)
                hops += 1
                test = (first[0] - (diff_row*hops), first[1] - (diff_col*hops))

    return antinodes

def out_of_range(row, col, inp):
    if row >= len(inp) or row < 0:
        return True
    if col >= len(inp[0]) or col < 0:
        return True
    return False

with open(PROD) as f:
    inp = list(map(list, f.read().split()))

    antenna_map = get_antenna_map(inp)

    result = get_antinodes(inp, antenna_map)

    print(len(result))