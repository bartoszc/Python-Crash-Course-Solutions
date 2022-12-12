def make_car(manufacturer, model_name, **car_info):
    car_info['Manufacturer'] = manufacturer
    car_info['Model name'] = model_name
    return car_info

car = make_car('Ford', 'Fiesta')
print(car)
print('---------------------------')
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)