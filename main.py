num1 = float(input('Введіть перше число'))
num2 = float(input('Введіть друге число'))
num3 = float(input('Введіть третє число'))

operation = input("Виберіть операцію (max для максимуму, min для мінімуму, avg для середнього арифметичного): ")
if operation == 'max':
    result = max(num1,num2,num3)
elif operation == 'min':
    result = min(num1,num2,num3)
elif operation == 'avg':
    result = (num1,num2,num3)
else:
    result=('Невірна операція')
print(f'Результат:{result}:')