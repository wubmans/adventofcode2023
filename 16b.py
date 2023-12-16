def print_visited(visited):

    p = 0

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            # print("#" if len(visited[i][j]) > 0 else '.', end = '')
            p += 1 if len(visited[i][j]) > 0 else 0 
        # print()

    return p

def move(beam):

    if beam[2] == 'n':
        beam[1] -= 1
    if beam[2] == 's':
        beam[1] += 1 
    if beam[2] == 'w':
        beam[0] -= 1
    if beam[2] == 'e':
        beam[0] += 1

    if beam[0] < 0 or beam[0] > len(grid[0]) - 1 or beam[1] < 0 or beam[1] > len(grid) - 1:
        return None

    return beam

def process_beam(beam, grid, visited):

    if beam[2] in visited[beam[0]][beam[1]]:
        return None
    
    visited[beam[0]][beam[1]][beam[2]] = True

    p = grid[beam[0]][beam[1]]

    if p == '\\':
        fd = { 'n' : 'w', 'w' : 'n', 'e': 's', 's' : 'e' }
        beam[2] = fd[beam[2]]
        return [beam]

    if p == '/':
        fd = { 'n' : 'e', 'e' : 'n', 's': 'w', 'w' : 's' }
        beam[2] = fd[beam[2]]
        return [beam]

    if p == '|' and beam[2] in ['e', 'w']:
        beams = [ [beam[0], beam[1], 'n'], [beam[0], beam[1], 's'] ]
        return beams

    if p == '-' and beam[2] in ['n', 's']:
        beams = [ [beam[0], beam[1], 'w'], [beam[0], beam[1], 'e'] ]
        return beams
    
    return [beam]

grid = []
file = open('16input.txt')

for line in file:
    line = line.rstrip()
    grid.append(line)

grid = list(''.join(a) for a in zip(*grid))


def run(beams):

    visited = [ [ {} for _ in  row ] for row in grid ]

    while len(beams) > 0:

        processed_beams = []

        for beam in beams:  
            ps = process_beam(beam, grid, visited)

            if ps == None:
                continue

            for p in ps:
                p = move(p)
                if p != None:
                    processed_beams.append(p)

        beams = processed_beams

    return visited

max_score = -1

max_y = len(grid)
max_x = len(grid[0])

for i in range(len(grid)):

    for point in [ [0, i, 'e'], [max_x - 1, i, 'w'], [i, 0, 's'], [i, max_y - 1, 'n'] ]:
        visited = run([point])
        score = print_visited(visited)
        print("start: (%s, %s) -> %s  ==> score: %s" % (point[0], point[1], point[2] , score))
        if score > max_score:
            max_score = score


print(max_score)

# p = print_visited(visited)
# print('score: ', p)