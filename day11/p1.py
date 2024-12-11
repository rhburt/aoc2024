from itertools import batched

DEV = "example.lst"
PROD = "input.lst"

NUM_BLINKS = 25

with open(PROD) as f:
    inp = list(map(int, f.read().split(' ')))

    for blink in range(NUM_BLINKS):
        to_insert = []
        for i in range(len(inp)):
            if inp[i] == 0:
                inp[i] = 1
            elif len(str(inp[i])) % 2 == 0:
                len_stone = len(str(inp[i])) // 2
                first_half = int(str(inp[i])[:len_stone])
                second_half = int(str(inp[i])[len_stone:])
                inp[i] = first_half
                to_insert.append((i+1, second_half))
            else:
                inp[i] *= 2024
        for i, (pos, stone) in enumerate(to_insert):
            inp.insert(pos+i, stone)

    print(len(inp))
