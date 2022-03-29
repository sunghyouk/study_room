# 키와 값을 바꾸기

# 28.1
def invert_dict(d):
    new_d = {}

    for k in d.keys():
        new_d[d[k]] = k
    return new_d


# 28.2
def invert_dict_inplace(d):
    tmp = d.copy()
    d.clear()

    for k in tmp.keys():
        d[tmp[k]] = k
