s = {1: ['S', 'C', 'V', 'N'], 2: ['Z', 'M', 'J', 'H', 'N', 'S'],
    3: ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
    4: ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
    5: ['P', 'F', 'H'],
    6: ['C', 'T', 'Z', 'H', 'J'],
    7: ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
    8: ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
    9: ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z'],}


with open('Chapter 9\\input.txt', 'r') as f:
    # ✅ get list of all lines
    lines = f.read().splitlines()

for line in lines:
    l_range = int(line.split(' ')[1])
    l_from = int(line.split(' ')[3])
    l_to = int(line.split(' ')[5])

    # for i in range(l_range):
    #     s.get(l_to).append(s.get(l_from).pop())
    s[l_to] = s.get(l_to) + s.get(l_from)[-l_range:]
    s[l_from] = s.get(l_from)[:-l_range]

print(s[1][-1], s[2][-1], s[3][-1])
print(''.join([v[-1] for v in s.values()]))

