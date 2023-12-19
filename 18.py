

point = (0, 0)

lines = {}

points = []

directions = { 'L': (-1, 0), 'R': (1,0), 'D' : (0, 1), 'U' : (0, -1) }

for line in open('18input.txt').readlines():
    direction, length, color = line.split(' ')

    for _ in range(int(length)):
        point = (point[0] + directions[direction][0], point[1] + directions[direction][1])

    if point[1] not in lines:
        lines[point[1]] = []
    
    lines[point[1]].append(point[0])
    
    # print(point)
    points.append(point)
    
    # print(direction, length, color)

sum = 0

min_y = 0
min_x = 0

max_x = -1
max_y = -1

for i in points:
    if i[1] < min_y:
        min_y = i[1]
    if i[1] > max_y or max_y == -1:
        max_y = i[1]

    if i[0] < min_x:
        min_x = i[0]
    if i[0] > max_x or max_x == -1:
        max_x = i[0]

print("min_x: %s" % (min_x))
print("min_y: %s" % (min_y))
print("max_x: %s" % (max_x))
print("max_y: %s" % (max_y))

points = [ (p[0] - min_x, p[1] - min_y) for p in points]

grid = [ ['.' for i in range (min_y, max_y + 1)] for line in range(min_x, max_x + 1)]

for p, q in zip(points, points[1:] + [points[0]]):
    if p[0] != q[0]:
        grid[p[0]][p[1]] = '#'
        grid[q[0]][p[1]] = '#'
        for x in range(min(p[0], q[0]), max(p[0], q[0])):
            grid[x][p[1]] = '#'
    else:
        for y in range(min(p[1], q[1]), max(p[1], q[1])):
            grid[p[0]][y] = '#'

pgrid = list(list(i) for i in zip(*grid))

# for i in range(len(pgrid)):
#     for j in range(len(pgrid[0])):
#         print(pgrid[i][j], end = '')
#     print()

sum = 0
count = False


q = [(100, 100)]
seen = []

while q:

    pm = q.pop(0)

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        pn = (pm[0] + d[0], pm[1] + d[1])

        if pn[0] not in range(0, len(pgrid)) or pn[1] not in range(0, len(pgrid[0])):
            continue

        if pn in seen:
            continue

        if pgrid[pn[0]][pn[1]] == '.':
            seen.append(pn)
            q.append(pn)

    pgrid[pm[0]][pm[1]] = '#'

sum = 0

for i in range(len(pgrid)):
    for j in range(len(pgrid[0])):
        print(pgrid[i][j], end = '')
        if pgrid[i][j] == '#':
            sum += 1
    print()


print("total count %s" % sum)
# # for line in lines:
# #     lines[line][0] += min_x
# #     lines[line][1] += min_x

# lines = list(sorted(lines.items()))

# i = 0

# while i < len(lines) - 1:

#     y, numbers = lines[i]
#     y_next, _ = lines[i + 1]

#     numbers.sort()

#     for w in range(y, y_next):
    
#     # print(lines[line])

#         j = 0
#         while j < len(numbers):
#             for k in range(numbers[j], numbers[j + 1]):
#                 grid[k - min_x][w - min_y] = 'o'

#             sum += numbers[j + 1] - numbers[j]
#             j += 2

#     i += 1
#     # print()
#     # print("%s | %s => %s == %s" % (line, lines[line][0], lines[line][1], lines[line][0] - lines[line][1] + 1))
#     # sum += lines[line][0]  - lines[line][1] + 1

# print("total: %s", sum)

# for p in points:
#     grid[p[0] - min_x][p[1] - min_y] = '*'



