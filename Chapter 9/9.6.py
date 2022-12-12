class Restaurant:
    def __init__(self, name, cuisine_type) -> None:
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The name of a restaurant is: {self.name}')
        print(f'The restaurant specializes in: {self.cuisine_type} cuisine')
    
    def open_restaurant(self):
        print('The restaurant in open')
    
    def set_number_served(self, num):
        self.number_served = num
    
    def increment_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type) -> None:
        super().__init__(name, cuisine_type)
        self.flavors = ['Chocolate', 'Strawberry', 'Mint']
    
    def present_flavors(self):
        for flavor in self.flavors:
            print(flavor)


f1 = IceCreamStand('My Ice Empire', 'Sweets')
f1.present_flavors()