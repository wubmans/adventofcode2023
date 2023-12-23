grid = []

def print_grid(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid)):  
            print(grid[i][j], end = '')
        print()
        

def search_grid(grid):

    touched_grid = grid.copy()

    vertices = [(1,0), (21, 22)]
    edges = {}
    
    paths = [[(1, 0)]]

    forks = []
    done_paths = []

    new_point = True

    while new_point:

        new_point = False

        new_paths = []

        for path in paths:

            while True:

                p = path[-1]


                pps = []

                for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    point = (p[0] + dir[0], p[1] + dir[1])

                    if point[0] not in range(len(grid)) or point[1] not in range(len(grid[0])):
                        continue

                    c = grid[point[0]][point[1]]

                    if c == '#':
                        continue

                    if point in path:
                        continue

                    # if touched_grid[point[0]][point[1]] == 'x':
                    #     continue

                    # touched_grid[point[0]][point[1]] = 'x'

                    pps.append(point)

                if len(pps) == 1:
                    path.append(pps[0])
                    continue

                if (path[0], p) in edges or (p, path[0]) in edges:
                    break

                edges[(path[0], p)] = len(path) - 1

                if len(pps) == 0:                
                    break
                # we hit a fork

                if p not in vertices:
                    vertices.append(p)

    
                new_paths += [[p, ps] for ps in pps]
                new_point = True
                break

        paths = new_paths

    # for edge in list(edges):
    #     if edge[0] not in vertices or edge[-1] not in vertices:
    #         del edges[edge]



    max_length = -1
   
    paths = [[[(1,0)], 0]]

    changed = True
    
    while changed:
        changed = False

        new_paths = []

        for path in paths:

            pathChanged = False

            for edge in edges:
                if path[0][-1] in edge:
                    p = edge[0] if path[0][-1] == edge[1] else edge[1]
                    if p not in path[0]:
                        new_path = [path[0].copy(), path[1]]
                        new_path[0].append(p)
                        new_path[1] += edges[edge]
                        new_paths.append(new_path)
                        changed = True
                        pathChanged = True

            if pathChanged == False:
                new_paths.append(path)           
                        
        if changed:
            paths = new_paths

    print()
    print()

    for path in paths:
        if path[1] > max_length or max_length == -1:
            max_length = path[1]
  
    print("max length: %s" % (max_length))

    # print_grid(grid)

for y, line in enumerate(open('23input.txt').readlines()):
    line = line.strip()
    grid.append(line)

grid = list(list(i) for i in zip(*grid))

print_grid(grid)
search_grid(grid)