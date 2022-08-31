# задача1
name = input('Как Вас зовут?')
age = int(input('Сколько Вам лет?'))
country = input('Назовите страну проживания')
print(name, age, country)

# задача2
s = int(input())
m = s // 60
hours = m // 60
seconds = s % 60
minutes = m % 60
print(hours, ':', minutes, ':', seconds)

#задача3
n = int(input())
print(n + (n*10 + n) + (n*100 + n*10 + n))

#задача4
i = int(input())
maximum = 0
while i>0:
    last = i % 10
    if last > maximum:
        maximum = last
    i = i // 10
print(maximum)

# задача5-6
revenue = int(input())
costs = int(input())
if revenue > costs:
    print('Фирма работает на прибыль!')
    print('рентабельность = ', (revenue - costs) / revenue)
    count = int(input('Введите число сотрудников : '))
    print('прибыль фирмы в расчёте на одного сотрудника = ', (revenue - costs) / count)
else:
    print('Фирма работает в убыток!')

#задача7
a = float(input())
b = float(input())
count = 1
while a <= b:
    a = a + a/10
    count = count + 1
print(count)




