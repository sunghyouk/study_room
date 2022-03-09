def f(a, b):
    x = a + b
    y = a - b
    print(x * y)
    return x/y


a = 1
b = 2
x = 5
y = 6

print(f(x, y))
print(f(a, b))
print(f(x, a))
print(f(y, b))
