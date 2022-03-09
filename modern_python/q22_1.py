def area(shape, n):
    return shape(n)


def circle(radius):
    return 3.14 * radius ** 2


def square(length):
    return length * length


print(area(circle, 5))

area(circle, 10)
area(square, 5)
area(circle, 4/2)
