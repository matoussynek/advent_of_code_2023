def calculate_distance(start, end, expand_factor):
    tot = 0
    x_end = max(start[0], end[0])
    x_start = min(start[0], end[0])
    for x in range(x_start, x_end):
        tot += expand_factor if x in empty_cols else 1
    y_end = max(start[1], end[1])
    y_start = min(start[1], end[1])
    for y in range(y_start, y_end):
        tot += expand_factor if y in empty_rows else 1
    
    return tot
    

def calculate_distances(expand_factor):
    distances = {}
    tot = 0
    for i, start in enumerate(galaxies):
        for j, end in enumerate(galaxies):
            if i == j:
                continue
            if (i,j) in distances or (j,i) in distances:
                continue
            distance = calculate_distance(start, end, expand_factor)
            distances[(i,j)] = distance
            tot += distance
    
    return tot


grid = open('./input.txt').read().splitlines()

width = len(grid[0])
height = len(grid)

empty_rows = []
for y, row in enumerate(grid):
    if all(c == '.' for c in row):
        empty_rows.append(y)

empty_cols = []
for x in range(width):
    is_empty = True
    for y in range(height):
        is_empty = is_empty and grid[y][x] == '.'
    if is_empty:
        empty_cols.append(x)

galaxies = []
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '#':
            galaxies.append((x,y))

print('Star 1 total distance:', calculate_distances(2))
print('Star 2 total distance:', calculate_distances(1000000))