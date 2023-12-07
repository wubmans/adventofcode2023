from math import floor
import re


def parse_input(filename):


    data = []
    
    file = iter(open(filename).readlines())
    for line in file:
        line = line.rstrip()
        line = re.sub(r'^\w+:', '', line)

        line = re.sub(r'\D*', '', line)

        data.append(line)

    return data

def main():

    data = parse_input("6input.txt")


    options = 0

    time = int(data[0])
    distance = int(data[1])

    for j in range(1, floor(time / 2) + 1):

        p = j * (time - j)
        # print("%i * %i = %i" % (j, time - j, p))

        if p > distance:
            if j != (time -j):
                options += 2
            else:
                options += 1

    print(options)
    # total_options *= options

    # print(total_options)

if __name__ == "__main__":
    main()