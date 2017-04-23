def make_car(manufacturer, model, **functions):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in functions.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True, power_steering=True)

print(car)

