from itertools import batched

DEV = "example.lst"
PROD = "input.lst"

def get_blocks(diskmap):
    blocks = []
    occupied_idxs = []
    free_idxs = []

    last_id = 0
    for i, (filelen, free_space) in enumerate(batched(diskmap[:-1], n=2)):
        start = len(blocks)
        blocks += [i for _ in range(filelen)]
        end = len(blocks)
        occupied_idxs.append((start,end))

        if free_space > 0:
            start = len(blocks)
            blocks += ['.' for _ in range(free_space)]
            end = len(blocks)
            free_idxs.append((start,end))

        last_id = i

    start = len(blocks)
    blocks += [i+1 for _ in range(diskmap[-1])]
    end = len(blocks)
    occupied_idxs.append((start,end))

    return blocks, occupied_idxs, free_idxs

def rearragne_blocks(blocks, occupied_idxs, free_idxs):
    for i, occupied in enumerate(occupied_idxs[::-1]):
        for j, free in enumerate(free_idxs):
            if free[0] > occupied[0]:
                break
            if (free[1] - free[0]) >= (occupied[1] - occupied[0]):
                blocks[free[0]:free[0]+(occupied[1]-occupied[0])] = blocks[occupied[0]:occupied[1]]
                blocks[occupied[0]:occupied[1]] = ['.' for i in range(occupied[1] - occupied[0])]
                occupied_idxs.insert(i, (free[0],free[0]+(occupied[1]-occupied[0])))
                deleted = False
                for k in range(len(free_idxs)):
                    if k > len(free_idxs)-1:
                        break
                    if free_idxs[k][1] == occupied[0]:
                        free_idxs[k] = (free_idxs[k][0], occupied[1])
                    if k > 0 and free_idxs[k][0] == free_idxs[k-1][1]:
                        free_idxs[k-1] = (free_idxs[k-1][0], free_idxs[k][1])
                        del free_idxs[k]
                        deleted = True
                if ((free[1] - free[0]) > (occupied[1] - occupied[0])):
                    free_idxs.insert(j, (free[0]+(occupied[1]-occupied[0]),free[1]))
                if j > 0 and free_idxs[j-1][1] == free[0]:
                    free_idxs[j-1] = (free_idxs[j-1][0], free[1])
                if free in free_idxs:
                    free_idxs.remove(free)
                occupied_idxs.remove(occupied)
                break
    return blocks

def get_checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == '.':
            continue
        checksum += i * blocks[i]

    return checksum
    

with open(PROD) as f:
    inp = list(map(int, list(f.read().strip())))

    blocks, occupied_idxs, free_idxs = get_blocks(inp)

    rearranged = rearragne_blocks(blocks, occupied_idxs, free_idxs)

    checksum = get_checksum(rearranged)

    print(checksum)
