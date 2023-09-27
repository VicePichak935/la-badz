
a, b, c = map(int, input('Type 3 numbers separated by space: ').split())
D = (b ** 2) - 4 * a * c

if D < 0:
    print('No Solutions')
    exit()

x1 = (-b + (D ** 0.5)) / (2 * a)
print(x1, end=' ')

if D > 0:
    x2 = (-b - (D ** 0.5)) / (2 * a)
    print(x2, end=' ')

print()
