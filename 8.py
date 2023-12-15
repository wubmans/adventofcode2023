import re
import functools 

def parse_input(filename):

    directions = None

    nodes = {}
    
    file = iter(open(filename).readlines())
    for line in file:
        line = re.sub(r'\n', '', line)
        if line == '':
            continue
        if re.search(r'=', line):
            line = re.sub(r'\s+', '', line)
            source, destinations = line.split('=')
            nodes[source] = re.sub(r'\(|\)|\n', '', destinations).split(',')
        else:
            directions = line
    
    return directions, nodes

def is_prime(number):
    for i in range(2, number):
        if number % i == 0 and number != i:
            return False
        
    return True
    

def get_next_prime(number):
    next = number + 1
    while is_prime(next) == False:
        next += 1

    return next


def prime_factorize(number):
    factors = []
    n = 2

    while number > 1:
        if n == number:
            factors.append(n)
            break
        
        while n < number:
            if number % n == 0:
                number /= n
                factors.append(n)
                n = 2
                continue
            n = get_next_prime(n)

    factors_dict = {}

    for n in factors:
        if n in factors_dict:
            factors_dict[n] += 1
        else:
            factors_dict[n] = 1


    return factors_dict


def lcm(a, b):
    factors_a = prime_factorize(a)
    factors_b = prime_factorize(b)

    factors = set().union(*[factors_a, factors_b])

    d = 1

    for f in factors:
        e = factors_a[f] if f in factors_a and (f not in factors_b or factors_a[f] > factors_b[f]) else factors_b[f]
        d *= f ** e

    return d


def lcm_numbers(numbers):
    factors = {}

    for i in range(len(numbers)):
        n_factors = prime_factorize(numbers[i])
        keys = set().union(*[factors, n_factors])

        for k in keys:
            factors[k] = factors[k] if k in factors and (k not in n_factors or n_factors[k] < factors[k]) else n_factors[k]

    d = 1

    for f in factors:
        e = factors[f]
        d *= f ** e

    return d


def main():

    directions, nodes = parse_input("8input.txt")

    # print(directions)
    # print(nodes)

    current_nodes = []

    for node in nodes:
        if node[2] == 'A':
            current_nodes.append(node)
    i = 0

    done = False

    loops = [-1 for i in range(len(current_nodes))]

    while done == False:

        next_nodes = []
        direction = ['L', 'R'].index(directions[i % len(directions)])
        for node in current_nodes:
            next_nodes.append(nodes[node][direction])

        for j in range(len(next_nodes)):
            if next_nodes[j][2] == 'Z' and loops[j] == -1:
                loops[j] = i + 1

        done = functools.reduce(lambda x, y: x and y != -1 , loops, True)
       
        current_nodes = next_nodes
        if i % 1e6 == 0: 
            print('.')

        i += 1
       
    print(loops)
    print(lcm_numbers(loops))

if __name__ == "__main__":
    main()