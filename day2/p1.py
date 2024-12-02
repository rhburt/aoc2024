DEV = "example.lst"
PROD = "input.lst"

with open(PROD) as f:
    lines = [x.split() for x  in f.read().splitlines()]

    result = 0
    for row in lines:
        last = int(row[0])
        increasing = int(row[1]) > last
        for elem in row[1:]:
            elem = int(elem)
            if (elem > last) != increasing:
                break
            if abs(elem-last) == 0 or abs(elem-last) > 3:
                break
            last = elem
        else:
            result += 1

    print(result)

