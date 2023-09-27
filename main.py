meters = float(input("Введіть кількість метрів: "))

unit = input("Виберіть одиниці виміру (милі, дюйми, ярди): ")

METERS_TO_MILES = 0.000621371
METERS_TO_INCHES = 39.3701
METERS_TO_YARDS = 1.09361

if unit == 'милі':
    converted_value = meters * METERS_TO_MILES
    unit_name = 'милі'
elif unit == 'дюйми':
    converted_value = meters * METERS_TO_INCHES
    unit_name = 'дюйми'
elif unit == 'ярди':
    converted_value = meters * METERS_TO_YARDS
    unit_name = 'ярди'
else:
    converted_value = None
    unit_name = None

if converted_value is not None and unit_name is not None:
    print(f"{meters} метрів дорівнює {converted_value} {unit_name}")
else:
    print("Неправильно вибрані одиниці виміру.")