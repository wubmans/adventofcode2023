def construct_grid(file, grid, mask):

    for line in file.readlines():
        x = 0
        for c in line:
            if len(grid) < x + 1:
                grid.append([])
                mask.append([])

            if c != '\n':
                if c.isdigit():
                    grid[x].append(c)
                    mask[x].append(False)
                else:
                    grid[x].append(None)
                    mask[x].append(c != '.')

            x += 1

def print_grid(grid, filename):

    file = open(filename, 'w')

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[x][y] in (None, False):
                file.write('.')
            elif grid[x][y] == True:
                file.write('x')
            else:
                file.write(grid[x][y])

        file.write('\n')

def expand_mask(grid, mask):
    for y in range(len(mask)):
        for x in range(len(mask[y])):
            m = mask[x][y]
            if m == False:
                continue

            for a in range (x - 1 , x + 2):
                for b in range (y - 1, y + 2):

                    if (a < 0) or (b < 0) or (a > len(grid) - 1) or (b > len(grid[a]) -1):
                        continue

                    if grid[a][b] != None:
                        mask[a][b] = True

def search_grid(grid, mask):

    total = 0

    number = None
    m = False
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            c = grid[x][y]

            if c == None:
                if m == True:
                    total += number
                number = None
                m = False

            else:
                m = m or mask[x][y]
                if number == None:
                    number = 0
                number *= 10
                number += int(c)

    return total

def main():

    file = open('3input.txt')
    grid = []
    mask = []

    construct_grid(file, grid, mask)
    expand_mask(grid, mask)

    total = search_grid(grid, mask)

    print("Total for this grid: %i" % (total))


if __name__ == "__main__":
    main()
