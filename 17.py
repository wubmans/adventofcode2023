import heapq

def parse_input(filename):
    grid =  [[i for i in line.rstrip()] for line in open(filename).readlines()]
    grid = list(zip(*grid))
    return grid

def print_grid(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y], end = '')
        print()

def find_route(grid):

    open_nodes = [(3, 0, 0), (1, 1, 1)]
    closed_nodes = []

    heapq.heapify(open_nodes)
    
    while len(open_nodes) > 0:

        dist, x, y = heapq.heappop(open_nodes)
        closed_nodes.append((x, y))
        print((x, y))

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            point = (x + direction[0], y + direction[1])
            if point[0] not in range(len(grid)) or point[1] not in range(len(grid[0])):
                continue

            if (point[0], point[1]) in closed_nodes:
                continue

            heapq.heappush(open_nodes, (int(grid[x][y]) + dist, point[0], point[1]))

 
        # /heapq.heappush(neighbors, open_nodes)

grid = parse_input('17input.txt')
print_grid(grid)
find_route(grid)