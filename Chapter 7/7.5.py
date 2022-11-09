while True:
    age = input('What is your age? ')
    if age == "break":
        print('You decided to leave the program')
        break
    if int(age) < 3:
        print('You do not have to pay anything')
    elif int(age) in range(3, 13):
        print('Your ticket costs 10$')
    else:
        print('Your ticket costs 15$')