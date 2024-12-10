from itertools import batched

DEV = "example.lst"
PROD = "input.lst"

def get_blocks(diskmap):
    blocks = []

    last_id = 0
    for i, (filelen, free_space) in enumerate(batched(diskmap[:-1], n=2)):
        blocks += [i for _ in range(filelen)]
        blocks += ['.' for _ in range(free_space)]
        last_id = i

    blocks += [i+1 for _ in range(diskmap[-1])]

    return blocks

def rearragne_blocks(blocks):
    p1 = 0
    p2 = len(blocks) - 1
    
    while p1 < p2:
        if blocks[p1] == '.':
            if blocks[p2] != '.':
                blocks[p1], blocks[p2] = blocks[p2], blocks[p1]
            else:
                p2 -= 1
        else:
            p1 += 1

    return blocks

def get_checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == '.':
            break
        checksum += i * blocks[i]

    return checksum
    

with open(PROD) as f:
    inp = list(map(int, list(f.read().strip())))

    blocks = get_blocks(inp)

    rearranged = rearragne_blocks(blocks)

    checksum = get_checksum(rearranged)

    print(checksum)
