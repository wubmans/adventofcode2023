
grid = []

start = None
steps = 64

for y, line in enumerate(open('21input.txt').readlines()):
    line = line.strip()

    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)


    grid.append([*line])

grid = list(list(i) for i in zip(*grid))

print(start)

points = [start]
seen = set()

for i in range(steps):

    new_points = []

    for p in points:
        for dir in [(0, 1), (0, -1), (1, 0), (-1 , 0)]:
            pp = (p[0] + dir[0], p[1] + dir[1])
            if pp in points:
                continue

            if pp[0] not in range(len(grid)) or pp[1] not in range(len(grid[1])):
                continue
                 
            if grid[pp[0]][pp[1]] == '#':
                continue

            seen.add(pp)

            if pp not in new_points:
                new_points.append(pp)
                                             
                                            
    points = new_points



for p in points:
    grid[p[0]][p[1]] = 'O'


for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end = '')
    print()

print(len(points))