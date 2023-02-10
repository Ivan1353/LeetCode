def total_length(matrix):
    length = 0
    for list in matrix:
        length += len(list)
    return length