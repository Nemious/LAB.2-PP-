#Задание1\2вариант
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
sum_result = num1 + num2
print("Сумма:", sum_result)
difference_result = num1 - num2
print("Разность:", difference_result)
product_result = num1 * num2
print("Произведение:", product_result)
average_result = (num1 + num2) / 2
print("Среднее арифметическое:", average_result)
quotient = round(num1 / num2, 2)
print("Частное чисел:", quotient)

if abs(num1) > abs(num2):
    print("Разность максимального и минимального:", (abs(num1) - abs(num2)))
elif abs(num2) > abs(num1):
    print("Разность максимального и минимального:", (abs(num2) - abs(num1)))
else:
    print("Ничего")