import heapq

def read_grid(filename):
    grid = [[ i for i in line.rstrip() ] for line in open(filename).readlines()]
    grid = list(list(i) for i in zip(*grid))
    return grid


def print_grid(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y], end = '')

        print()


# def find_neighbors(grid, node):
#     x, y, previous_directions = node
#     for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):

#         if len(previous_directions) > 2:
#             if previous_directions[0] == previous_directions[1] == previous_directions[2]:
#                 if previous_directions[2] == direction:
#                     continue

#         nx = x + direction[0]
#         ny = y + direction[1]
#         if nx not in range(len(grid)) or ny not in range(len(grid[0])):
#                 continue
        
       
#         pd = previous_directions

#         pd = pd[-2:] + [direction]

#         yield nx, ny, pd

def print_path(goal, previous, grid):
    
    p = goal
    
    while True:
        print(p)
        grid[p[0]][p[1]] = '.'
        p = previous[p]

        if p == (0, 0):
            grid[p[0]][p[1]] = '.'
            break

    print_grid(grid)


def search_grid(grid):


    queue = [(0, 0, 0, 0, 0, 0, [])]

    costs = {}
   
    seen = set()

    heapq.heapify(queue)

    while queue:

        c, x, y, dx, dy, dcount, prevs = heapq.heappop(queue)
    
        if x == len(grid) - 1  and y == len(grid[0]) - 1 and dcount >= 4:
            
            grid[x][y] = '.'
            s = 0
            t = 0
            for i in prevs:
                grid[i[0]][i[1]] = '.'
                if s != i[0]:
                      for q in range(min(s, i[0]), max(s, i[0])):
                        grid[q][i[1]] = '.'

                else:
                    for r in range(min(t, i[1]), max(t, i[1])):
                        grid[i[0]][r] = '.'
                s = i[0]
                t = i[1]

            print_grid(grid)

            print
            print("min score: %s" % c)

            break

        if (x, y, dx, dy, dcount) in seen:
            continue

        seen.add((x, y, dx, dy, dcount))

        for ndx, ndy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            if (dx, dy) == (0, 0):
                (dx, dy) = (ndx, ndy)

            nc = c

            ndcount = dcount

            if (dx, dy) == (-ndx, - ndy):
                continue

            if (ndcount < 4):
                ndcount += 1
                (ndx, ndy) = (dx, dy)
            else:
                if (dx, dy) == (ndx, ndy):
                    ndcount += 1
                else:
                    ndcount = 1

            # if (ndcount < 4) and (dx, dy) != (0, 0):
            #     

            if ndcount > 10:
                continue

            nx = x + ndx
            ny = y + ndy

            if nx not in range(len(grid)) or ny not in range(len(grid[0])):
                continue

            n = (nx, ny, ndx, ndy, ndcount, prevs + [(x, y, dx, dy, dcount)])

            nc += int(grid[nx][ny])
            
            heapq.heappush(queue, (nc, *n))

    return costs, []

grid = read_grid('17input.txt')
# print_grid(grid)
costs, previous = search_grid(grid)



# # print_grid(grid)

# p = (12, 12)

# # for i in costs:
    
# #     if i[0] == p[0] and i[1] == p[1]:
# #         p = i
# #         break



for i in previous:
    if i[0] == 12 and i[1] == 12:
        print(i, costs[i])
        # d = i
        # s = set()
        # while d in previous and d not in s:
        #     s.add(d)    
        #     print(d, costs[d])
        #     d = previous[d]


        # print('xxx')
        


print(10)

# print_path( goal, previous, grid)

# print(costs[goal])