from itertools import batched

DEV = "example.lst"
PROD = "input.lst"

def get_score(row, col, inp, prev_trail):
    if (row,col) in prev_trail:
        return 0
    if int(inp[row][col]) == 9:
        prev_trail.add((row, col))
        return 1
    
    right, left, down, up = 0,0,0,0
    if col < len(inp[0])-1 and int(inp[row][col+1]) == int(inp[row][col]) + 1:
        right = get_score(row, col+1, inp, prev_trail)
    if col > 0 and int(inp[row][col-1]) == int(inp[row][col]) + 1:
        left = get_score(row, col-1, inp, prev_trail)
    if row < len(inp)-1 and int(inp[row+1][col]) == int(inp[row][col]) + 1:
        down = get_score(row+1, col, inp, prev_trail)
    if row > 0 and int(inp[row-1][col]) == int(inp[row][col]) + 1:
        up = get_score(row-1, col, inp, prev_trail)

    if right or left or down or up:
        prev_trail.add((row, col))
    return right+left+down+up

with open(PROD) as f:
    inp = f.read().splitlines()

    result = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if int(inp[i][j]) == 0:
                print(f"{i},{j}, {get_score(i, j, inp, set())}")
                result += get_score(i, j, inp, set())

    print(result)
