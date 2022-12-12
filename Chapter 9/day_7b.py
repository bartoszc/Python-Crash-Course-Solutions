with open('Chapter 9\\input.txt', 'r') as f:
    # ✅ get list of all lines
    lines = f.read().splitlines()

d = {}
sl = []
total = 0
for line in lines:
    if line.startswith('$ cd'):
        d[line.split(' ')[2]] = sl
        sl = []
        continue
    else:
        sl.append(line)

print(d)