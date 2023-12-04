
import re


def parse_input(filename):

    points = 0

    file = open(filename)
    for line in file.readlines():
        parts = re.split(r':|\|', line.rstrip())
        lucky_numbers = filter(lambda n: n != '', parts[1].split(' '))
        actual_numbers = filter(lambda n: n != '', parts[2].split(' '))
        correct = len(set(lucky_numbers) & set(actual_numbers))
        
        points +=  2 ** (correct - 1) if correct > 0 else 0

    return points

def main():
    points = parse_input('4input.txt')
    print("Total points is: %s" % (points))


if __name__ == "__main__":
    main()