def make_matrix(matrix: str, vertex: int):
    rows = []
    currect_matrix = []

    matrix = list(map(int, matrix.split()))
    
    for i in range(len(matrix)):
        if i == len(matrix) - 1:
            rows.append(matrix[i])
            currect_matrix.append(rows[:])
        elif i % vertex != 0 or i == 0:
            rows.append(matrix[i])
        else:
            currect_matrix.append(rows[:])
            rows.clear()
            rows.append(matrix[i])

    return currect_matrix
