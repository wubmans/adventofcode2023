
q = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
]

for i in range(1, len(q)):

    

    top = q[max(0, 2 * i - len(q)):i]
    bottom = q[i:min(2 * i, len(q))]

    bottom = bottom[::-1]

    print(i)
    print(top)
    print(bottom)