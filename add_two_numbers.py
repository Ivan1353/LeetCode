
def addTwoNumbers(l1, l2):
    int_1 = int("".join(map(str, list(reversed(l1)))))
    int_2 = int("".join(map(str, list(reversed(l2)))))
    int3 = int_1 + int_2
    endlist = list(map(int, reversed(list(str(int3)))))
    return endlist