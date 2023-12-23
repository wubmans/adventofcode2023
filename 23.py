grid = []

def print_grid(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid)):  
            print(grid[i][j], end = '')
        print()
        

def search_grid(grid):
    
    paths = [[(1, 0)]]

    done_paths = []

    new_point = True

    while new_point:

        new_point = False

        new_paths = []

        for path in paths:

            p = path[-1]

            pps = []

            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                point = (p[0] + dir[0], p[1] + dir[1])

                if point[0] not in range(len(grid)) or point[1] not in range(len(grid[0])):
                    continue

                c = grid[point[0]][point[1]]

                if c == '#':
                    continue

                # if c == '>' and dir == (-1, 0):
                #     continue

                # if c == 'v' and dir == (0, -1):
                #     continue

                if point in path:
                    continue

                pps.append(point)

                # new_point = True
            
                # new_path = path.copy()
                # new_path.append(point)

                # new_paths.append(new_path)

            if len(pps) > 1:
                done_paths.append(path)
                new_paths = [ [point, p] for p in pps]
                new_point = True
                
            elif len(pps) == 1:
                np = path.copy()
                np.append(pps[0])
                new_paths.append(np)
                new_point = True

        paths = new_paths


    max_length = -1
    lp = None

    for path in paths:
        pp = path[-1]
        if pp[1] != len(grid[0]) -1:
            continue

        if len(path) > max_length:
            lp = path
        max_length = max(max_length, len(path) - 1)

    print()
    print()

    if lp == None:
        exit()

    for p in lp:
        grid[p[0]][p[1]] = 'o'

    print("max length: %s" % (max_length))

    print_grid(grid)

for y, line in enumerate(open('23input.txt').readlines()):
    line = line.strip()
    grid.append(line)

grid = list(list(i) for i in zip(*grid))

print_grid(grid)
search_grid(grid)