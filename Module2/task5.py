# Матрица воплоти
# [[10, 10], [10, 10]]
# [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
# [[13, 13], [13, 13], [13, 13], [13, 13]]

def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []

    matrix = []
    for a in range(n):
        res = []
        for j in range(m):
            res.append(value)
        matrix.append(res)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

for i in range(1, 4):
    print(eval(f'result{i}'))
