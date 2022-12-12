
with open('Chapter 9\\input.txt', 'r') as f:
    input = f.read().splitlines()

bl = []
for line in input:
    bl.append([int(x) for x in list(line)])

total = (len(bl[0]) -1) * 4
for i, line in enumerate(bl):
    if i == 0 or i == len(bl) - 1:
        continue
    for j, tree in enumerate(line):
        if j == 0 or j == len(line) - 1:
            continue

        left = [x for x in line[:j]]
        right = [x for x in line[j+1:]]
        top = [bl[x][j] for x in range(i)]
        bottom = [bl[x][j] for x in range(i+1, len(bl))]
        print(left)

        if any(z >= tree for z in left) and any(z >= tree for z in right) and any(z >= tree for z in top) and any(z >= tree for z in bottom):
            pass
        else:
            total += 1
         
print(total)