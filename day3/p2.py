import re

DEV = "example.lst"
PROD = "input.lst"

with open(PROD) as f:
    inp = f.read()

    matches = re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', inp)

    enabled = True
    result = 0
    for match in matches:
        if match[2]:
            enabled = True
        elif match[3]:
            enabled = False
        else:
            if enabled:
                result += int(match[0]) * int(match[1])

    print(result)
