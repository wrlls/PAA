from functions import *

print("Введите значения a и b")
a=int(input())
b=int(input())
print("Выберите операцию")
print("1:Сложение")
print("2:Вычитание")
print("3:Умножение")
print("4:Деление")
choice = int(input())
if choice == 1:
    print(sum(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))
else:
    print("Введите корректный номер предложенных операций")
