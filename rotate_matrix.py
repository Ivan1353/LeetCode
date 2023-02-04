def rotate(matrix):
    old_matrix = list(reversed(matrix))
    new_matrix = [[] for x in range(len(matrix))]
    for i in range(len(old_matrix)):
        for j in range(len(old_matrix)):
            new_matrix[i].append(old_matrix[j][i])
    return new_matrix