grid = []

grid = [[-1 for y in range(10)] for x in range(10)]

for i, l in enumerate(grid):
    for j, p in enumerate(grid[i]):
        print(grid[i][j], end = '')
    print()