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


r1 = Restaurant('Da Grasso', 'French')
print(r1.number_served)
r1.number_served = 20
print(r1.number_served)
print('--------------------------')
r1.set_number_served(25)
print(r1.number_served)
print('--------------------------')
r1.increment_number_served(30)
print(r1.number_served)