
file = open('14input.txt')

grid = []

for line in file:

    line = line.rstrip()
    
    grid.append(line)

q = list(list(a) for a in zip(*grid))

score = 0

for r in q:
    s = ''.join(r).split('#')
    offset = 0

    ct = ''
    for i, d in enumerate(s):

        if d == '':
            if i > 0:
                ct += '#'
                offset += 1
            continue

        if i > 0:
            offset += 1
        
        count_os = d.count('O')
        score += sum(100 - offset - x for x in range(0, count_os))
        offset += len(d)

        ct += ''.join(['O' for i in range(0, count_os)])
        ct += ''.join(['.' for i in range(0, len(d) - count_os)])
        ct += '#' if i < len(s) - 1 else ''

    print(''.join(r))
    print(ct)
    print()

print('total score is %s' % score)