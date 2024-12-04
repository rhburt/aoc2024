import re

DEV = "example.lst"
PROD = "input.lst"

SEARCH = "XMAS"

with open(PROD) as f:
    inp = f.read().splitlines()

    result = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            # RIGHT
            if inp[i][j:j+len(SEARCH)] == SEARCH:
                result += 1
            # LEFT
            if inp[i][j-len(SEARCH)+1:j+1][::-1] == SEARCH:
                result += 1
            # DOWN
            if "".join([x[j] for x in inp[i:i+len(SEARCH)]]) == SEARCH:
                result += 1
            # UP
            if "".join([x[j] for x in inp[i-len(SEARCH)+1:i+1]][::-1]) == SEARCH:
                result += 1
            # DIAG RIGHT DOWN
            try:
                if "".join([inp[i+k][j+k] for k in range(len(SEARCH)) if i+k < len(inp) and j+k < len(inp[i])]) == SEARCH:
                    result += 1
            except IndexError:
                pass
             # DIAG RIGHT UP
            try:
                if "".join([inp[i-k][j+k] for k in range(len(SEARCH)) if i-k >=0 and j+k < len(inp[i])]) == SEARCH:
                    result += 1
            except IndexError:
                pass
            # DIAG LEFT DOWN
            try:
                if "".join([inp[i+k][j-k] for k in range(len(SEARCH)) if i+k < len(inp) and j-k >= 0]) == SEARCH:
                    result += 1
            except IndexError:
                pass
            # DIAG LEFT UP
            try:
                if "".join([inp[i-k][j-k] for k in range(len(SEARCH)) if i-k >= 0 and j-k >= 0]) == SEARCH:
                    result += 1
            except IndexError:
                pass
            
    print(result)


