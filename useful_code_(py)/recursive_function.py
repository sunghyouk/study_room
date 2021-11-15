# excercise 1
example = [[1, 2, 3],
           [4, [5, 6]],
           7,
           [8, 9]]


def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output


print("변환", flatten(example))

# excercise 2
memo = {}


def table(remain, already_sit):
    key = str([remain, already_sit])

    if key in memo:
        return memo[key]

    if remain < 0:
        return 0

    if remain == 0:
        return 1

    count = 0
    for i in range(already_sit, 10 + 1):
        count += table(remain - i, i)

    memo[key] = count
    return count


print(table(100, 2))
