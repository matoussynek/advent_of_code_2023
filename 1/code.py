import re
nums_txt = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tot = 0
def dict_to_number(d):
    return d[min(d)] * 10 + d[max(d)]
def get_number_from_line(line):
    res = {}
    for m in re.finditer(r'(\d)', line):
        res[m.start()] = int(m.group())
    for i, n in enumerate(nums_txt):
        if not n in line:
            continue
        for m in re.finditer(rf'({n})', line):
            res[m.start()] = i
    return dict_to_number(res)
with open("./input.txt", "r") as file:
    i = 1
    for line in file.readlines():
        ln = get_number_from_line(line)
        tot += ln
        i += 1
print(tot)