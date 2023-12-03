def construct_grid(file, grid, mask):


    y = 0

    for line in file.readlines():
        x = 0
        for c in line:
            if c == '\n':
                continue

            if c.isdigit():
                grid[x][y] = c
                mask[x][y] = False
            else:
                grid[x][y] = None
                mask[x][y] = c == '*'

            x += 1
            
        y += 1


def print_grid(grid, filename):

    file = open(filename, 'w')

    for y in range(140):
        for x in range(140):
            if grid[x][y] in (None, False):
                file.write('.')
            elif grid[x][y] == True:
                file.write('x')
            else:
                file.write(grid[x][y])

        file.write('\n')

def search_grid(grid, mask):

    total = 0

    for y in range(140):
        for x in range(140):

            if mask[x][y] == False:
                continue

            adjacents = 0
            contacts = []
            

            for b in range(y - 1, y +2):
                a = x - 1

                while a < x + 2:

                    if a < 0 or b < 0 or a >= 140 or b >= 140:
                        a += 1 
                        continue

                    if grid[a][b] != None:
                        adjacents += 1
                        contacts.append((a,b))
                        while a >= 0 and b >= 0 and a < 140 and b < 140 and grid[a][b] != None:
                            a += 1
                        

                    a += 1

            if adjacents == 2:

                numbers = []

                for contact in contacts:

                    number = 0
                    interrupted = False

                    for i in range(contact[0] - 3, contact[0] + 3):
                        if i < 0 or i >= 140:
                            continue
                        if contact == contacts[0] and contact[1] == contacts[1][1] and i >= contacts[1][0]:
                            continue

                        if grid[i][contact[1]] != None:
                            if interrupted:
                                number = 0
                                interrupted = False
                            number *= 10
                            number += int(grid[i][contact[1]])
                        else:
                            if number != 0: 
                                interrupted = True

                    
                    numbers.append(number)

                print("%i * %i = %i" % (numbers[0], numbers[1], numbers[0] * numbers[1]))
                total += numbers[0] * numbers[1]

            else:
                mask[x][y] = False

    return total

def main():

    file = open('3input.txt')

    grid = [[0 for y in range(140)] for x in range(140)]
    mask = [[0 for y in range(140)] for x in range(140)]

    construct_grid(file, grid, mask)
  
    total = search_grid(grid, mask)
    print_grid (mask, 'mask.txt')
   

    print("Total for this grid: %i" % (total))


if __name__ == "__main__":
    main()
