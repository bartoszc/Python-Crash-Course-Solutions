class User:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'First name: {self.first_name}')
        print(f'Last name {self.last_name}')
        print(f'Age: {self.age}')
    
    def greet_user(self):
        print(f'Hello: {self.first_name} !!!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User('Bartosz', 'Chojnacki', 33)
for _ in range(6):
    u1.increment_login_attempts()
print('_________________________')
print(u1.login_attempts)
print('_________________________')
u1.reset_login_attempts()
print(u1.login_attempts)