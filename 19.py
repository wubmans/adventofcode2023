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

def apply_rule(p, rule):
    for r in rule:
        if type(r) is tuple:
            v, cmp, rng, rr = r
            if cmp == '>':
                if p[v] > int(rng):
                    return rr
            if cmp == '<':
                if p[v] < int(rng):
                    return rr
        else:
            return r

sum = 0

for p in points:

    output = 'in'
    print('%s =====> ' % p, end = '')

    while output not in ('R', 'A'):
        output = apply_rule(p, ruleset[output]) 
        print(output + ' -> ', end = '')


    print(output)
    if output == 'A':
        for k in p:
            sum += p[k]



print('Total score: %s' % sum)