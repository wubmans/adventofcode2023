
import re


file = open('1input.txt', 'r')
file2 = open('1output.txt', 'w')

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0

def replace_incorrects(line = ''):

    for i in digits:
        for j in digits:
            if i == j:
                continue
            if i[-1] == j[0]:
                line = line.replace(i[0:-1] + j, i + j)

    return line

def parse_line(line):

    firstDigit = None
    lastDigit = None

    line = line.rstrip()
    line = replace_incorrects(line)

    m = re.split(r'(' + '|'.join(digits) +  '|\d{1})', line)

    for digit in m:
        if digit == '':
            continue
        if digit.isdigit():
            parseDigit = int(digit)
        elif digit in digits:
                parseDigit = digits.index(digit) + 1
        else:
            continue

        
        if firstDigit == None: 
            firstDigit = parseDigit
            lastDigit = parseDigit
        else:
            lastDigit = parseDigit
        

    return firstDigit, lastDigit

def main():

    total = 0
        

    for line in file.readlines():
        firstDigit, lastDigit = parse_line(line)
        result = (firstDigit * 10 + lastDigit)
        total += result


        # total += result
            
        file2.write('%s => %i  - %i\n' % (line.rstrip(), result, total))

    print('The total is : %i' % total)



if __name__ == "__main__":
    main()