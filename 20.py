import graphviz

conns = {}

for line in open('20input.txt').readlines():
    line = line.strip()
    input, outputs = line.split('->')
    outputs = [l.strip() for l in outputs.split(',')]
    input = input.strip()

    type = input[0] if input[0] in ('&', '%') else None
    name = input[1:] if input[0] in ('&', '%') else input

    conns[name] = { 'type': type, 'inputs': {}, 'outputs': outputs, 'state': 0}


for conn, stats in conns.items():
    if stats['type'] == '&':
        for c, s in conns.items():
            if conn in s['outputs']:
                stats['inputs'][c] = 0

# print(conns)
# print()
# print()


lows = 0
highs = 0

dot = graphviz.Digraph(comment= 'Le epic diagram of pulses')

for conn, stats in conns.items():
    dot.node(conn, conn)

    for output in stats['outputs']:
        dot.edge(conn, output)

dot.render('pretty_pulses.gv', view=True)
exit()


for i in range(20000, int(1e9)):

    if i % 1000 == 0:
        print('.', end = '')
    pulses = [('button', 'broadcaster', 0)]

    while pulses:

        new_pulses = []

        for pulse in pulses:
            # print(pulse)
            if pulse[1] == 'rx' and pulse[2] == 0:
                print("%s, %s and %s" % (i, lows, highs))
                exit()


            if pulse[2] == 0:
                lows += 1
            elif pulse[2] == 1:
                highs += 1

            if pulse[1] not in conns:
                continue

        


            conn = conns[pulse[1]]

            if conn['type'] == '&':
                for output in conn['outputs']:
                    conn['inputs'][pulse[0]] = pulse[2]
                    p = 1
                    for u in conn['inputs']:
                        p = p and conn['inputs'][u]
                    
                    new_pulses.append((pulse[1], output, 0 if p == 1 else 1))
            elif conn['type'] == '%':
                    if pulse[2] == 0:
                        conn['state'] = 1 if conn['state'] == 0 else 0
                        for output in conn['outputs']:
                            
                            new_pulses.append((pulse[1], output, conn['state']))
            else:
                for output in conn['outputs']:
                    
                    new_pulses.append((pulse[1], output, pulse[2]))
                    
                

        pulses = new_pulses

# print("%s lows, %s highs, %s total" % (lows, highs, lows * highs))