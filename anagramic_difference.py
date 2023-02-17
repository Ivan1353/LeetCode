def string_to_dict(dict1, a):
    for x in list(a):
        if x not in dict1:
            dict1[x] = 1
        else:
            dict1[x] += 1


def difference(a, b):
    dict_a, dict_b, dict_c = {},{},{}
    string_to_dict(dict_a,a)
    string_to_dict(dict_b, b)
    for x in dict_a:
        if x not in dict_b:
            dict_c[x] = 1
        else:
            if dict_a[x] != dict_b[x]:
                dict_c[x] = dict_a[x] - dict_b[x]
    return dict_c
