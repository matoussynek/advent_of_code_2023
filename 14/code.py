def count_plane(plane):
    return sum(line.count("O") * (len(plane) - i) for i, line in enumerate(plane))

def roll_line(line):
    blocks = line.split('#')
    res = []
    for block in blocks:
        ohs = block.count('O')
        rolled_block = 'O' * ohs + '.' * (len(block) - ohs)
        res.append(rolled_block)
    
    return '#'.join(res)

def rotate():
    global plane2
    for _ in range(4):
        plane2 = tuple(map(''.join, zip(*plane2)))
        plane2 = tuple(roll_line(line) for line in plane2)
        plane2 = tuple(line[::-1] for line in plane2)
    
    return plane


plane_input = open('./input.txt').read().splitlines()
plane = list(map(''.join, zip(*plane_input)))
plane2 = tuple(map(''.join, zip(*plane_input)))

plane = [roll_line(line) for line in plane]
plane = list(map(''.join, zip(*plane)))

tot = count_plane(plane)

print(f'star1: {tot}')

#star2 - doesnt work
visited = {plane2}
planes = [plane2]
i = 0
while True:
    i += 1
    rotate()
    if plane2 in visited:
        break
    visited.add(plane2)
    planes.append(plane2)

first_found_twice = planes.index(plane2)

plane2 = planes[(1000000000 - first_found_twice) % (i - first_found_twice) + first_found_twice]

tot2 = count_plane(plane2)

print(f'star2: {tot2}')
