num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

operation = input("Виберіть операцію (+ для суми, - для різниці, * для добутку, / для середнього арифметичного): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = (num1 + num2) / 2
else:
    result = "Неправильна операція"

print(f"Результат: {result}")