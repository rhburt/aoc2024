DEV = "example.lst"
PROD = "input.lst"

def check_row(row):
    last = int(row[0])
    increasing = int(row[1]) > last
    for i, elem in enumerate(row):
        if i == 0:
            continue
        elem = int(elem)
        if (elem > last) != increasing:
            return False
        if abs(elem-last) == 0 or abs(elem-last) > 3:
            return False
        last = elem
    else:
        return True

with open(PROD) as f:
    lines = [x.split() for x  in f.read().splitlines()]

    result = 0
    for row in lines:
        if check_row(row):
            result += 1
            continue
        for i in range(len(row)):
            if check_row(row[:i] + row[i+1:]):
                result += 1
                break
        else:

    print(result)

