import re

def rotate(grid):
    return list(''.join(a[::-1]) for a in zip(*grid))

def flip(grid):
    return list(''.join(a) for a in zip(*grid))

def unflip(grid):
    return list(''.join(a[::-1]) for a in zip(*grid))

file = open('14input.txt')

grid = []

results = {}

for line in file:

    line = line.rstrip()
    grid.append(line)

q = grid
processed_grid = None
score = 0

for cycle in range(int(1e9)):

    if cycle % 1e6 == 0:
        print('.', end = '')
        print(score)

    ig = ''.join(q)

    if ig in results:
        q = results[ig]
        continue

    for dir in range(4):

        score = 0

        q = flip(q)
        processed_grid = []

        for r in q:
            s = []

            # gezeik met delimiter split die de delimiter weghaalt
            s = list(filter(bool, re.split(r'(#)', ''.join(r))))
        
            ct = ''
            offset = 0

            for i, d in enumerate(s):

                if d == '#':
                    ct += d
                    offset += 1
                    continue

                count_os = d.count('O')
                score += sum(10 - offset - x for x in range(0, count_os))
                offset += len(d)

                ct += ''.join(['O' for i in range(0, count_os)])
                ct += ''.join(['.' for i in range(0, len(d) - count_os)])
                

            # print(''.join(r))
            # print(ct)
            # print()
                
            processed_grid.append(ct)

        processed_grid = flip(processed_grid)

        q = rotate(processed_grid)

    # print('cycle %s, score = %s' % (cycle, score))
        
    results[ig] = q
        
   