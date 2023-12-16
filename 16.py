
import json


def next_point(point, direction):
    if direction == 'n':
        return (point[0], point[1] - 1)
    if direction == 's':
         return (point[0], point[1] + 1)    
    if direction == 'w':
        return (point[0] - 1, point[1])
    if direction == 'e':
         return (point[0] + 1, point[1])

def out_of_bounds(point, grid):
    return point[0] < 0 or point[0] > len(grid[0]) - 1 or point[1] < 0 or point[1] > len(grid) - 1

def process_beam(beam, grid):

    for p in beam['prevs']:
        if p['point'] == beam['point'] and p['direction'] == beam['direction']:
            return

    beam['prevs'].append({ 'point': beam['point'], 'direction': beam['direction']})
    p = grid[beam['point'][0]][beam['point'][1]]

    if p == '\\':
        fd = { 'n' : 'w', 'w' : 'n', 'e': 's', 's' : 'e' }
        beam['direction'] = fd[beam['direction']]
        return [beam]

    if p == '/':
        fd = { 'n' : 'e', 'e' : 'n', 's': 'w', 'w' : 's' }
        beam['direction'] = fd[beam['direction']]
        return [beam]

    if p == '|' and beam['direction'] in ['e', 'w']:
        beams = [{ 'point': beam['point'], 'direction' : 'n', 'prevs': beam['prevs'] }, { 'point': beam['point'], 'direction' : 's', 'prevs': beam['prevs'] }]
        return beams

    if p == '-' and beam['direction'] in ['n', 's']:
        beams = [{ 'point': beam['point'], 'direction' : 'w', 'prevs': beam['prevs'] }, { 'point': beam['point'], 'direction' : 'e', 'prevs': beam['prevs'] }]
        return beams
    
    # print('x')
    return [beam]

def lit(beam, lit_grid):
    if lit_grid[beam['point'][0]][beam['point'][1]] == 0:
        lit_grid[beam['point'][0]][beam['point'][1]] = 1
        return True

    return False

def show(grid_lit):
    print()
    print()
    for y in range(len(grid_lit)):
        for x in range(len(grid_lit[0])):
            print('#' if grid_lit[x][y] != 0 else '.', end = '')
        print()

def run(beams):

    grid_lit = [[ 0 for i in range(len(grid))] for i in range(len(grid[0]))]

    while len(beams) > 0:

        processed_beams = []

        changed = False
    
        for beam in beams:
            lit(beam, grid_lit)
            result = process_beam(beam, grid)
            # processed_beams += result if result != None else []

            if result == None:
                continue

            for beam in result:
                    beam['point'] = next_point(beam['point'], beam['direction'])
                    if out_of_bounds(beam['point'], grid):
                        continue      
                    processed_beams.append(beam)

            # result = process_beam(beam, grid)

        # for beam in processed_beams:
        #     # print(beam['point'])
        
    
            
        beams = processed_beams

    score = sum([ sum(row) for row in grid_lit ])
    # print(score)

    return score

    # if changed == False:
    #     break

    # changed = False
    # for beam in beams:
    #     changed = changed or lit(beam, grid_lit) or 'cycles' not in beam

    # if changed == False:
    #     for beam in beams:
    #         if 'cycles' not in beam:
    #             continue

    #     break

# print("\n\nResult:\n\n")
# show(grid_lit)

# show(grid_lit)

# score = sum([ sum(row) for row in grid_lit ])
# print(score)

grid = []
file = open('16input.txt')

for line in file:
    line = line.rstrip()
    grid.append(line)


grid = list(''.join(a) for a in zip(*grid))

max_score = -1

max_y = len(grid)
max_x = len(grid[0])

for i in range(len(grid)):

    for point in [ (0, i, 'e'), (max_x - 1, i, 'w'), (i, 0, 's'), (i, max_y - 1, 'n') ]:
    
        beams = [{ 'point': (point[0], point[1]), 'direction' : point[2], 'prevs': [] }]
        score = run(beams)
        print("start: (%s, %s) -> %s  ==> score: %s" % (point[0]
        , point[1], point[2] , score))
        if score > max_score:
            max_score = score


print(max_score)
