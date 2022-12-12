from random import choice

l1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E')
for _ in range(4):
    print(str(choice(l1)) + ' wins the prize!')