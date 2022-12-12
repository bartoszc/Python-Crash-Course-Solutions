class Restaurant:
    def __init__(self, name, cuisine_type) -> None:
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The name of a restaurant is: {self.name}')
        print(f'The restaurant specializes in: {self.cuisine_type} cuisine')
    
    def open_restaurant(self):
        print('The restaurant in open')


r1 = Restaurant('Da Grasso', 'French')
print(r1.name)
print(r1.cuisine_type)
r1.describe_restaurant()
r1.open_restaurant()
print('_________________________')
r2 = Restaurant('Italian City', 'Italian')
print(r2.name)
print(r2.cuisine_type)
r2.describe_restaurant()
r2.open_restaurant()
print('_________________________')
r3 = Restaurant('Bar', 'Polish')
print(r3.name)
print(r3.cuisine_type)
r3.describe_restaurant()
r3.open_restaurant()