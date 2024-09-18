def main(matrix: list[list[float]]):
    if len(matrix) == 1:
        return matrix[0][0]
    max_value = abs(matrix[0][0])
    max_index = 0
    for i in range(1,len(matrix)):
        if abs(matrix[i][0]) > max_value:
            max_value = abs(matrix[i][0])
            max_index = i
    multiplicator = 1
    if matrix[0] is not matrix[max_index]:
        multiplicator = -1
        matrix[0],matrix[max_index] = matrix[max_index],matrix[0]
    for i in range(1,len(matrix)):
        cof = matrix[i][0] / matrix[0][0]
        matrix[i] = [matrix[i][j] - matrix[0][j]*cof for j in range(len(matrix[0]))]
    
    n_matrix = [matrix[i][1:] for i in range(1,len(matrix))]
    return multiplicator * matrix[0][0] * main(n_matrix)


matrix = [[2, -1, 3], [4, 0, -2], [1, 5, 7]]

print(main(matrix))
    