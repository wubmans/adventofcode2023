def horizontal(puzzle):

    for i in range (0, len(puzzle) -1):
        mirror = True
        smudge = 0
        for j in range(0, min(i, len(puzzle) - i - 2) + 1):
            if puzzle[i - j ] != puzzle[i + j + 1]:
                smudge += sum(map(lambda t: t[0] != t[1], zip(puzzle[i - j], puzzle[i + j + 1])))
                mirror = False
                if smudge > 1: 
                    break

        if smudge == 1:
            print(" possible smudge at %s" % (i + 1))
            return i + 1

        # if mirror == True:
        #     return i + 1

    return 0

def vertical(puzzle):
    for i in range (0, len(puzzle[0]) -1):
        mirror = True
        smudge = 0
        for j in range(0, min(i, len(puzzle[0]) - i - 2) + 1):
            for k in range(len(puzzle)):
                if puzzle[k][i - j] != puzzle[k][i + j + 1]:
                    smudge += 1
                    mirror = False
                    # break

                    if smudge > 1:
                        break

        if smudge == 1:
            print(" possible smudge at %s" % (i + 1))
            return i + 1

        # if mirror == True:
        #     return i + 1

    return 0

puzzles = []
puzzle = []

for line in open('13input.txt'):
    if line == '\n':
        if len(puzzle) > 0:
            puzzles.append(puzzle)
        puzzle = []
    else:
        puzzle.append(line.rstrip())

puzzles.append(puzzle)

score = 0

for puzzle in puzzles:
    score += horizontal(puzzle) * 100
    score += vertical(puzzle) 

print("score is %s" % score)