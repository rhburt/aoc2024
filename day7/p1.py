import itertools

DEV = "example.lst"
PROD = "input.lst"

OPERATORS = ['+', '*']

with open(PROD) as f:
    inp = f.read().splitlines()

    result = 0
    for line in inp:
        total, nums = line.split(': ')
        nums = nums.split(' ')

        total = int(total)

        for combination in itertools.product(OPERATORS, repeat=len(nums)-1):
            left = None
            last_op = None
            this_total = None
            for elem in [val for pair in zip(nums, combination) for val in pair]+[nums[-1]]:
                if elem in OPERATORS:
                    last_op = elem
                    continue
                if left:
                    this_total = eval(f"{left}{last_op}{elem}")
                else:
                    this_total = elem
                    left = elem
                left = this_total
            if this_total == total:
                result += total
                break


    print(result)

