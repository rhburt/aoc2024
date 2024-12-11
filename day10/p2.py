from itertools import batched

DEV = "example.lst"
PROD = "input.lst"

def get_score(row, col, inp):
    if int(inp[row][col]) == 9:
        return 1
    
    right, left, down, up = 0,0,0,0
    if col < len(inp[0])-1 and int(inp[row][col+1]) == int(inp[row][col]) + 1:
        right = get_score(row, col+1, inp)
    if col > 0 and int(inp[row][col-1]) == int(inp[row][col]) + 1:
        left = get_score(row, col-1, inp)
    if row < len(inp)-1 and int(inp[row+1][col]) == int(inp[row][col]) + 1:
        down = get_score(row+1, col, inp)
    if row > 0 and int(inp[row-1][col]) == int(inp[row][col]) + 1:
        up = get_score(row-1, col, inp)

    return right+left+down+up

with open(PROD) as f:
    inp = f.read().splitlines()

    result = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if int(inp[i][j]) == 0:
                result += get_score(i, j, inp)

    print(result)
