import sys


def fix_ctetra(line):
    elems = line[0:-1].split(',')
    return ','.join(elems[0:-2] + [elems[-1], elems[-2]]) + '\n'

with open(sys.argv[1], 'r') as input:
    data = [fix_ctetra(line) if 'CTETRA' in line else line for line in input]

with open(sys.argv[1], 'w') as output:
    output.write(''.join(data))
