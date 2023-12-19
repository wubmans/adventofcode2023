import re

ruleset = {}
points = []

for line in open('19input.txt').readlines():
    line = line.rstrip()

    if line == '':
        continue

    m = re.match(r'(\w+){(.+)}', line)
    if m != None:
        name, rules = m.groups()
        rules = rules.split(',')

        rr = []

        for rule in rules:
            m = re.match(r'(x|m|a|s)([<>])(\d+):(\w+)', rule)
            if m:
                rr.append(m.groups())
            else:
                rr.append((rule))            

        ruleset[name] = rr


    else:
        pl = {}
        line = line.replace('{', '').replace('}', '')
        pps = line.split(',')
        for p in pps:
            k, v = p.split('=')
            pl[k] = int(v)

        points.append(pl)

def apply_rule(path, ruleset, rule):

    if rule in ('A', 'R'):
        path['result'] = rule
        return [path]

    paths = []

    for i, r in enumerate(ruleset[rule]):

        npath = path.copy()

        npath[rule] = []

        for j in range(i):
            v, cmp, rng, rr = ruleset[rule][j]
            cmp = '>=' if cmp == '<' else '<='
            npath[rule].append((v, cmp, rng))

        if type(r) is tuple:
            v, cmp, rng, rr = r
            npath[rule].append((v, cmp, rng))
        else:
            rr = r

        paths += apply_rule(npath, ruleset, rr)

    return paths


sum = 0

paths = apply_rule({}, ruleset, 'in')

for path in paths:

    q = {
        'x' : [1, 4000],
        'm' : [1, 4000],
        'a' : [1, 4000],
        's' : [1, 4000]
    }
    
    if (path['result'] == 'R'):
        continue

    for step in path:
        for pp in path[step]:

            if type(pp) is not tuple:
                continue

            k, cmp, rng = pp

            if cmp == '<':
                q[k][1] = int(rng) - 1  
            if cmp == '<=':
                q[k][1] = int(rng)  
            if cmp == '>':
                q[k][0] = int(rng) + 1  
            if cmp == '>=':
                q[k][0] = int(rng)  

    pr = 1

    for k in q:
        pr *= (q[k][1] - q[k][0] + 1)


    print("%s => %s" % (q, pr))
    sum += pr


print("total combo's: %s" % sum)
# while True:

#     output = 'in'
#     print('%s =====> ' % p, end = '')

#     while output not in ('R', 'A'):
#         output = apply_rule(p, ruleset[output]) 
#         print(output + ' -> ', end = '')


#     print(output)
#     if output == 'A':
#         for k in p:
#             sum += p[k]



# print('Total score: %s' % sum)