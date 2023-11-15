base = []
dots_in_plot = []
final_array_of_dots = []
settings = []
print('Введите количество точек:')
n = int(input())
for i in range(1, n+1):
    base.append(i)
print('Вводите координаты точек (x; y)')
for i in range(0, 2*n):
    dot = int(input())
    dots_in_plot.append(dot)
print('Введите количество количество связей')
k = int(input())
print('Введите связи номеров точек через -')
for i in range(0, k):
    point = input()
    c = point.find('-')
    a = point[:c]
    b = point[c+1:]
    settings.append(a)
    i += 1
    settings.append(b)
a = 0
u = 0
for i in range(0, k):
    count = settings.count(settings[a])
    if count == 2:
        base.pop(a)
        a -= 1
    a += 1
print(base)
