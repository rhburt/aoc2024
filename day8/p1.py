from collections import defaultdict
TEST1 = "test1.lst"
DEV = "example.lst"
PROD = "input.lst"

def get_antenna_map(inp):
    antenna_map = defaultdict(list)
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] != '.':
                antenna_map[inp[row][col]].append((row,col))

    return antenna_map

def out_of_range(row, col, inp):
    if row >= len(inp):
        return True
    if col >= len(inp[0]):
        return True
    return False

def check_if_antinode(row, col, inp, antenna_map):
    for _,antenna_locations in antenna_map.items():
        for ant_row, ant_col in antenna_locations:
            if row != ant_row or col != ant_col:
                if (ant_row + (ant_row - row), ant_col + (ant_col - col)) in antenna_locations:
                    return True
    return False


with open(PROD) as f:
    inp = list(map(list, f.read().split()))

    antenna_map = get_antenna_map(inp)

    result = set()
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if check_if_antinode(row, col, inp, antenna_map):
                result.add((row,col))

    print(len(result))
