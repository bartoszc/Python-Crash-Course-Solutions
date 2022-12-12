import string

print(string.ascii_letters)
file = open('Chapter 9\\input.txt', 'r')

with open('Chapter 9\\input.txt', 'r') as f:
    # ✅ get list of all lines
    lines = f.read().splitlines()

sum = 0
for index, line in enumerate(lines):
    if index % 3 == 0:
        three = [lines[index], lines[index+1], lines[index+2]]
        common = list(set(lines[index]) & set(lines[index+1]) & set(lines[index+2]))[0]
        sum += string.ascii_letters.index(common)+1

print(sum)