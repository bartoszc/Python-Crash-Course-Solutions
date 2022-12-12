def make_sandwich(*args):
    print('Summary of your order:')
    for topping in args:
        print(topping)


make_sandwich(['cheese'])
make_sandwich(['cheese', 'tomato'])
make_sandwich(['cheese', 'tomato', 'ham'])