import re

def parse_line(line):

    min_red = 0
    min_green = 0
    min_blue = 0

    m = re.match(r'^Game (\d+):.*', line)    
    id = int(m.group(1))

    s = line.split(':')
    s = s[1].split(';')

    for e in s:
        marbles = e.split(',')
        for color in marbles:
            # print(color)
            l = re.match(r'^\s(\d+)\s(green|red|blue)', color)
            a = int(l.group(1))
            c = l.group(2)

            # print(a)
            
            if c == 'red' and a > min_red:
                min_red = a
            if c == 'green' and a > min_green:
                min_green = a
            if c == 'blue' and a > min_blue:
                min_blue = a
    
    return min_red * min_green * min_blue


def main():

    total = 0

    file = open('2input.txt')

    for line in file.readlines():
        id = parse_line(line)
        if id != None:
            print(id)
            total += id

    print("the total is: %i" % (total))

main()