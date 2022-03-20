spam = ['apples', 'bananas', 'tofu', 'cats']


def to_sentence(spam):
    for i in range(len(spam) - 1):
        print(spam[i-1])
    print(' and ')
    print(spam[-1])
