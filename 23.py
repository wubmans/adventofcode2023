grid = []

def print_grid(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid)):  
            print(grid[i][j], end = '')
        print()
        

def search_grid(grid):


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

    # 
        
    def bfs(p, graph):

        results = []

        for v in graph[p['path'][-1]]:
            if v in p['seen']:
                continue

            pp = { 'path': p['path'].copy(), 'seen': p['seen'].copy(), 'score': p['score'] }

            pp['path'].append(v)
            pp['seen'].add(v)


            pp['score'] += edges[(p['path'][-1], v)] if (p['path'][-1], v) in edges else edges[(v, p['path'][-1])]

            if v != (139, 140):
                results += bfs(pp, graph)
            else:
                results += [pp]

        return results


    graph = { v: [] for v in vertices }

    for v0, v1 in edges:
        graph.setdefault(v0, []).append(v1)
        graph.setdefault(v1, []).append(v0)

    nedges = {}

    results = bfs({ 'path': [(1, 0)], 'seen': set((1, 0)), 'score': 0 }, graph)
   

    # changing = True

    # while changing:

    #     changing = False

    #     for v0, v1 in edges:

    #         if v0 != (1,0):
    #             continue

    #         v0c = 0
    #         v1c = 0

    #         pps = []

    #         for vn0, vn1 in edges:
                
    #             if v0 == vn0 or v0 == vn1:
    #                 v0c += 1

    #             if v1 == vn0 or v1 == vn1:
    #                 v1c += 1

    #             if vn0 == v1:
    #                 pps.append(vn1)

    #         if v0c <= 3 and v1c <= 3:
    #             changing = True
    #             for p in pps:
    #                 edges[(v0, p)] = edges[(v0, v1)] + edges[(v1, p)]
    #                 del edges[(v1, p)]
    #             del edges[(v0, v1)]

    #             break

    # print(edges)

    
    # counts = {}

    # for v0, v1 in edges:
    #     if v0 not in counts:
    #         counts[v0] = 0
    #     if v1 not in counts:
    #         counts[v1] = 0

    #     counts[v0] += 1
    #     counts[v1] += 1


    # paths = [[(1, 0)]]

    # closed_paths = []

    # ds = {}

    # def distance_between_vs(v0, v1):

       

    #     if (v0, v1) in ds:
    #         return ds[(v0, v1)]
        
    #     vss = [v0]
    
    #     while v1 not in vss:

    #         nvss = []

    #         for vs in vss:

    #             for v in graph[vs]:
    #                 ds[(vs, v)] = edges[(vs, v)] if (vs, v) in edges else edges[(v, vs)]
    #                 if v0 != v:
    #                     ds[(v0, v)] = ds[(v0, vs)] + ds[(vs, v)]
    #                 if v == v1:
    #                     return ds[(vs, v)]
                    
    #                 nvss.append(v)

    #         vss = nvss
            

    # distance_between_vs((1, 0), (13, 13))

    # while paths:

    #     new_paths = []

    #     for path in paths:
    #         for v in graph[path[-1]]:
    #             if v == (139, 140):
    #                 closed_paths.append(path.copy().append(v))
    #             if v not in path:
    #                 np = path.copy()
    #                 np.append(v)
    #                 new_paths.append(np)

    #     paths = new_paths

    # print()
    # print()

    max_length = -1

    for result in results:
        if result['score'] > max_length or max_length == -1:
            max_length = result['score']
  
    print("max length: %s" % (max_length))

    # print_grid(grid)

for y, line in enumerate(open('23input.txt').readlines()):
    line = line.strip()
    grid.append(line)

grid = list(list(i) for i in zip(*grid))

print_grid(grid)
search_grid(grid)