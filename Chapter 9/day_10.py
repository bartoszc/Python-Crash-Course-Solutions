with open('Chapter 9\\input.txt', 'r') as f:
    input = f.read().splitlines()

def check_cycle(cycle):
    return cycle in (20, 60, 100, 140, 180, 220)

total = 1
cycle = 0
six = 0

for line in input:
    line = line.split(' ')
    if line[0] == 'noop':
        cycle += 1
        if check_cycle(cycle):
            six += cycle * total
    else:
        for i in range(2):
            cycle += 1
            if check_cycle(cycle):
                six += cycle * total
        total += int(line[1])

print(six)
