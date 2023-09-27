num1 = float(input('Введіть перше число'))
num2 = float(input('Введіть друге число'))
num3 = float(input('Введіть третє число'))

operation = input('Виберіть операцію(+ для суми,* для добутку):')

if operation == '+':
    result = num1+num2+num3
elif operation == '*':
    result = num1*num2*num3
else:
    result = 'Неправильна операція'

print(f'Результат: {result}')
