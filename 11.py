import functools
from math import floor
from functools import cmp_to_key
import re

grid = None
x = None
y = None

galaxies = []

def parse_input(filename):

    global galaxies

    # grid = []
    # global x
    # global y

    # size_y = len(open(filename).readlines())
    y = 0

    file = open(filename).readlines()
    for line in file:
        line = line.rstrip()
        for x in range(len(line)):
            # if x > len(grid) - 1:
            #     grid.append([0 for p in range(size_y)])
            
            if line[x] == '#':
                galaxies.append([x, y])
            # grid[x][y] = line[x]

        y += 1

    return grid

def print_galaxies(galaxies):
    max_x = functools.reduce(lambda a, b: b[0] if b[0] > a else a, galaxies, -1)
    max_y = functools.reduce(lambda a, b: b[1] if b[1] > a else a, galaxies, -1)

    print("dimensions: (%s, %s)" % (max_x, max_y))

    for j in range(max_y + 1):
        for i in range(max_x + 1):

            found = False
            for g in galaxies:
                if g[0] == i and g[1] == j:
                    # print("#", end = '')
                    found = True
            if found == False:
                print(".", end = '')
        
        print()
                    

def horizontal_lines(galaxies, factor):
    
    max_y = functools.reduce(lambda a, b: b[1] if b[1] > a else a, galaxies, -1)

    print(max_y)

    empty_rows = []

    for y in range(max_y):
        empty = functools.reduce(lambda a, b: a and b[1] != y , galaxies, True)
        if empty:
            empty_rows.append(y)
            print("row %s is empty" % (y))
    
    for i, row in enumerate(empty_rows): 
        for g in galaxies:
            if g[1] > row + i * factor :
                g[1] += 1 * factor
    

def vertical_lines(galaxies, factor):

    max_x = functools.reduce(lambda a, b: b[0] if b[0] > a else a, galaxies, -1)
    print(max_x)

    empty_columns = []

    for x in range(max_x):
        empty = functools.reduce(lambda a, b: a and b[0] != x , galaxies, True)
        if empty:
            empty_columns.append(x)
            print("column %s is empty" % (x))
    
    
    for i, column in enumerate(empty_columns):
        for g in galaxies:
            if g[0] > column + i * factor:
                g[0] += 1 * factor  
def main():
    parse_input('11input.txt')
    
    # for y in range(len(grid[0])):
    #     for x in range(len(grid)):
    #         print(grid[x][y], end = '')
    #     print()
        

    horizontal_lines(galaxies, 1000000 - 1)
    vertical_lines(galaxies, 1000000 - 1)

    # print_galaxies(galaxies)
    
    total_distance = 0
    p = 0

    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            g = galaxies[i]
            h = galaxies[j]

            if j == i:
                continue

            if j <= i :
                # print("i == %s and j == %s, continue" % (i, j))
                continue
            
            p += 1

            distance = abs(g[0] - h[0]) + abs(g[1] - h[1])
            total_distance += distance
            # print("distance form (%s, %s) to (%s, %s) == %s" % (g[0], g[1], h[0], h[1], distance))


    print("total pairs: %s" % p)
    print("total distance: %s", total_distance)

if __name__ == "__main__":
    main()