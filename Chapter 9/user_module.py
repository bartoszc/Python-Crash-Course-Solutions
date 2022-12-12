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