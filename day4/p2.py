import re

DEV = "example.lst"
PROD = "input.lst"

SEARCH = ["SAM", "MAS"]
SEARCH_RANGE = [-1, 0, 1]

with open(PROD) as f:
    inp = f.read().splitlines()

    result = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            # DIAG RIGHT UP
            valid = True
            try:
                if "".join([inp[i-k][j+k] for k in SEARCH_RANGE if i-k >=0 and j+k < len(inp[i])]) not in SEARCH:
                    continue
            except IndexError:
                continue
            # DIAG LEFT UP
            try:
                if "".join([inp[i-k][j-k] for k in SEARCH_RANGE if i-k >= 0 and j-k >= 0]) not in SEARCH:
                    continue
            except IndexError:
                continue
            
            result += 1
            
    print(result)


