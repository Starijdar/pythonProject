first = int(input('Первое число:'))
second = int(input('Второе число:'))
third = int(input('Третье число:'))

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)