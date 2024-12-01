DEV = "example.lst"
PROD = "input.lst"

with open(PROD) as f:
    lines = [x.split() for x  in f.read().splitlines()]

    left = [int(x[0]) for x in lines]
    right = [int(x[1]) for x in lines]

    left = sorted(left)
    right = sorted(right)

    print(sum([abs(left[i] - right[i]) for i in range(len(left))]))

