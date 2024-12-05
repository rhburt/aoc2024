from collections import defaultdict
DEV = "example.lst"
PROD = "input.lst"

with open(PROD) as f:
    inp = f.read().split('\n\n')

    rules = inp[0].splitlines()
    updates = inp[1].splitlines()

    rule_map = defaultdict(list)
    for rule in rules:
        num, before = rule.split('|')
        rule_map[num].append(before)

    result = 0
    for update in updates:
        update_list = update.split(',')
        valid = True
        for i, update_element in enumerate(update_list):
            if any(x in update_list[:i] for x in rule_map[update_element]):
                valid = False
        if valid:
            result += int(update_list[len(update_list)//2])

    print(result)
