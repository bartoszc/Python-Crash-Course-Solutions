import user_module

class Privileges:
    def __init__(self) -> None:
        self.privileges = ["can add post", 
                           "can delete post", 
                           "can ban user",]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
    

class Admin(user_module.User):
    def __init__(self, first_name, last_name, age) -> None:
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()