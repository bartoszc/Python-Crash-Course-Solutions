class User:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'First name: {self.first_name}')
        print(f'Last name {self.last_name}')
        print(f'Age: {self.age}')
    
    def greet_user(self):
        print(f'Hello: {self.first_name} !!!')


u1 = User('Bartosz', 'Chojnacki', 33)
u1.describe_user()
u1.greet_user()
print('_________________________')
u2 = User('Piotr', 'Testowy', 28)
u2.describe_user()
u2.greet_user()