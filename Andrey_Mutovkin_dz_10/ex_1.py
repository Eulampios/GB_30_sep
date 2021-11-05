class MatrixSizeError(ValueError):
    pass


class Matrix:
    def __init__(self, matrix_list: list):
        self._data = matrix_list

    def __str__(self):
        return '\n'.join([' '.join(
            [str(ceil) for ceil in raw]
        ) for raw in self._data])

    @staticmethod
    def _check_length(list1, list2):
        if len(list1) != len(list2):
            raise MatrixSizeError(ERROR_MESSAGE_MATRIX_SIZE_ERROR)

    def __add__(self, matrix):
        result = []
        Matrix._check_length(self._data, matrix._data)
        for row_index in range(len(self._data)):
            Matrix._check_length(self._data[row_index], matrix._data[row_index])
            result.append([
                self._data[row_index][ceil_index] + matrix._data[row_index][ceil_index]
                for ceil_index in range(len(self._data[row_index]))
            ])
        return Matrix(result)


matrix1 = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

matrix2 = Matrix(
    [
        [1, 1, 1],
        [2, 2, 2]
    ]
)

print(f"Matrix 1: \n{matrix1}")
print(f"Matrix 2: \n{matrix2}")

matrix3 = matrix1 + matrix2
print(f"Matrix 3: \n{matrix3}")
