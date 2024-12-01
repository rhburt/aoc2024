from collections import defaultdict

DEV = "example.lst"
PROD = "input.lst"

with open(PROD) as f:
    lines = [x.split() for x  in f.read().splitlines()]

    left = [int(x[0]) for x in lines]
    right = [int(x[1]) for x in lines]

    nummap = defaultdict(int)
    for num in right:
        nummap[num] += 1

    result = 0
    for num in left:
        result += num * nummap[num]

    print(result)
