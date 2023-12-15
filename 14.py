import re

def rotate(grid):
    return list(''.join(a[::-1]) for a in zip(*grid))

def flip(grid):
    return list(''.join(a) for a in zip(*grid))

def unflip(grid):
    return list(''.join(a[::-1]) for a in zip(*grid))

def calculate_score(grid):
    score = 0
    for i, row in enumerate(grid):
        score += (len(grid) - i) * row.count('O')

    return score

file = open('14input.txt')

grid = []

results = {}

for line in file:

    line = line.rstrip()
    grid.append(line)

q = grid
ig = ''.join(q)
processed_grid = None
score = 0

for cycle in range(int(1e9)):

    if cycle % 1e6 == 0:
        print('%s => score: %s' % (cycle /1e6, score))
        
    if ig in results:
        c, ig, q, score = results[ig]
        print("cycle starts on %s, from %s, with length %s" % (cycle, c, cycle - c))
        irr = int((1e9 - c) % (cycle - c) + c - 1)
        print(irr)
        sc = results[list(results.keys())[irr]][3]
        print(sc)
        break
        
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
        
    results[ig] = (cycle, ''.join(q), q, calculate_score(q))

    ig = ''.join(q)
        
   