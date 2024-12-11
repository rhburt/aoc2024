from collections import defaultdict
from itertools import batched
from tqdm import tqdm

DEV = "example.lst"
PROD = "input.lst"

NUM_BLINKS = 75
ALREADY_DONE = defaultdict(dict)

def get_num_stones(stone, blinks_remaining):
    if blinks_remaining == 0:
        return 1

    if stone in list(ALREADY_DONE[blinks_remaining].keys()):
        return ALREADY_DONE[blinks_remaining][stone]

    if stone == 0:
        total = get_num_stones(1, blinks_remaining-1)
        ALREADY_DONE[blinks_remaining][stone] = total

    elif len(str(stone)) % 2 == 0:
        first = int(str(stone)[:len(str(stone))//2])
        second = int(str(stone)[len(str(stone))//2:])
        total = get_num_stones(first, blinks_remaining-1)
        total += get_num_stones(second, blinks_remaining-1)
    else:
        total = get_num_stones(stone*2024, blinks_remaining-1)

    ALREADY_DONE[blinks_remaining][stone] = total
    return total

with open(PROD) as f:
    inp = list(map(int, f.read().split(' ')))

    total = 0
    for stone in inp:
        total += get_num_stones(stone, NUM_BLINKS)
    print(total)
