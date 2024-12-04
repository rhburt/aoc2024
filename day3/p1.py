import re

DEV = "example.lst"
PROD = "input.lst"

with open(DEV) as f:
    inp = f.read()

    print(sum([int(x)*int(y) for x,y in re.findall(r'mul\((\d+),(\d+)\)', inp)]))

