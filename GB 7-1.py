class Matrix():

    def __init__(self, list):
        self.list = list

    def __str__(self):
        matrix = ''
        for lst in self.list:
            matrix += ' '.join(str(x) for x in lst) + '\n'
        return matrix

    def __add__(self, other):
        matrix = []
        count_row = 0
        for row in self.list:
            row_lst = []
            count_num = 0
            for num in row:
                row_lst.append(num + other.list[count_row][count_num])
                count_num += 1
            matrix.append(row_lst)
            count_row += 1
        return matrix


matrix = Matrix([[3, 5, 32], [2, 4, 6], [1, 64, 8]])
print(matrix)
matrix2 = Matrix([[5, 6, 3], [35, -4, -86], [12, -4, 8]])
sum_matrix = Matrix(matrix + matrix2)
print(sum_matrix)