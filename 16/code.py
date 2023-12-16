from collections import deque

grid = open('./input.txt').read().splitlines()

def calculate_beams(r, c, dr, dc):
    a = [(r, c, dr, dc)]
    visited = set()
    queue = deque(a)

    while queue:
        r, c, dr, dc = queue.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        ch = grid[r][c]
        
        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                queue.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                queue.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                queue.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    queue.append((r, c, dr, dc))
                    
    unique = {(r, c) for (r, c, _, _) in visited}
    
    return len(unique)

print(f'Star1 energized nodes: {calculate_beams(0, -1, 0, 1)}')

max_val = 0

for r in range(len(grid)):
    max_val = max(max_val, calculate_beams(r, -1, 0, 1))
    max_val = max(max_val, calculate_beams(r, len(grid[0]), 0, -1))
    
for c in range(len(grid)):
    max_val = max(max_val, calculate_beams(-1, c, 1, 0))
    max_val = max(max_val, calculate_beams(len(grid), c, -1, 0))

print(f'Star2 max: {max_val}')