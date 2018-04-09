"""
The Matrix ADT, m行，n列
"""
from array_two_demensional import Array2D


class Matrix:
    """
    m,n矩阵
    """
    def __init__(self, num_rows, num_cols) -> None:
        self._the_grid = Array2D(num_rows, num_cols)
        self._the_grid.clear(0)

    @property
    def num_rows(self):
        """
        num_rows
        :return:
        """
        return self._the_grid.num_rows

    @property
    def num_cols(self):
        """
        num_cols
        :return:
        """
        return self._the_grid.num_cols

    def __getitem__(self, ndx_tuple):
        return self._the_grid[ndx_tuple[0], ndx_tuple[1]]

    def __setitem__(self, ndx_tuple, value):
        self._the_grid[ndx_tuple[0], ndx_tuple[1]] = value

    def scaleby(self, scalar):
        """
        每个元素乘scalar
        :return:
        """
        for _r in range(self.num_rows):
            for _c in range(self.num_cols):
                self._the_grid[_r, _c] *= scalar

    def __add__(self, rhs_matrix):
        assert (rhs_matrix.num_rows == self.num_rows and
                rhs_matrix.num_cols == self.num_cols)
        new_matrix = Matrix(self.num_rows, self.num_cols)
        for _r in range(self.num_rows):
            for _c in range(self.num_cols):
                new_matrix[_r, _c] = self[_r, _c] + rhs_matrix[_r, _c]

    def __str__(self):
        return self._the_grid.__str__()

    def clear(self, value):
        self._the_grid.clear(value)


if __name__ == '__main__':
    MATRIX = Matrix(3, 3)
    print(MATRIX.num_rows,MATRIX.num_cols)
    MATRIX.clear(1)
    print(MATRIX)
