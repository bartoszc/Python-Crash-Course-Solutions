from pprint import pprint

with open('Chapter 9\\input.txt', 'r') as f:
    input = f.read().splitlines()


bl = []
sl = {}

for line in input:
    if line == '':
        bl.append(sl)
        sl = {}
    else:
        
pprint(bl)