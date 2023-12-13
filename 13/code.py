def get_mirror(mirror):
    for split in range(1,len(mirror)):
        top = mirror[:split][::-1]
        bot = mirror[split:]

        top = top[:len(bot)]
        bot = bot[:len(top)]

        if top == bot:
            return split
        
    return 0

def get_mirror_star2(mirror):
    for split in range(1,len(mirror)):
        top = mirror[:split][::-1]
        bot = mirror[split:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(top, bot)) == 1:
            return split
    
    return 0

tot = 0
tot2 = 0
for mirror_str in open('./input.txt').read().split("\n\n"):
    mirror = mirror_str.splitlines()

    #rows
    tot += get_mirror(mirror) * 100
    tot2 += get_mirror_star2(mirror) * 100

    #cols
    tot += get_mirror(list(zip(*mirror)))
    tot2 += get_mirror_star2(list(zip(*mirror)))

print(f'Star1 total: {tot}')
print(f'Star2 total: {tot2}')