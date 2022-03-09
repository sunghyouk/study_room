def add_one(a, b):
    x = a+1
    y = b+1

    def mult(a, b):
        return a * b
    return mult(x, y)


a = 1
b = 2
x = 5
y = 6

print(add_one(x, y))
