def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while a % b != 0:
        a, b = b, a % b
    return abs(b)


number_f = int(input('Введите первое число: '))
number_s = int(input('Введите второе число: '))
print(gcd(number_f, number_s))