with open('Chapter 9\\input.txt', 'r') as f:
    # ✅ get list of all lines
    lines = f.read().splitlines()

sum = 0
for line in lines:
    left, right = line.split(',')
    l1 = list(range(int(left.split('-')[0]), int(left.split('-')[1])+1))
    l2 = list(range(int(right.split('-')[0]), int(right.split('-')[1])+1))
    if(any(x in l1 for x in l2)) or (any(x in l2 for x in l1)):
        sum += 1

print(sum)