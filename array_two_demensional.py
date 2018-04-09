"""
Two-Demensional Arrays
实现二维矩阵
"""

from array import Array


class Array2D:
    """
    Two-Demensional Arrays ADT
    """
    def __init__(self, num_rows, num_cols) -> None:
        self._the_rows = Array(num_rows)
        for i in range(num_rows):
            self._the_rows[i] = Array(num_cols)

    @property
    def num_rows(self):
        """
        rows
        :return:
        """
        return len(self._the_rows)

    @property
    def num_cols(self):
        """
        cols
        :return:
        """
        return len(self._the_rows[0])

    def __getitem__(self, ndx_tuple):  # ndx_tuple:(x,y)
        assert len(ndx_tuple) == 2
        _row, _col = ndx_tuple[0], ndx_tuple[1]
        assert (0 <= _row < self.num_rows and
                0 <= _col < self.num_cols)
        the_1d_array = self._the_rows[_row]
        return the_1d_array[_col]

    def __setitem__(self, ndx_tuple, value):
        assert len(ndx_tuple) == 2
        _row, _col = ndx_tuple[0], ndx_tuple[1]
        assert (0 <= _row < self.num_rows and
                0 <= _col < self.num_cols)
        the_1d_array = self._the_rows[_row]
        the_1d_array[_col] = value

    def __str__(self):
        ret = []
        for _r in range(self.num_rows):
            for _c in range(self.num_cols):
                the_1d_array = self._the_rows[_r]
                ret.append(str(the_1d_array[_c]))
        return ','.join(ret)


if __name__ == '__main__':
    ROW, COL = (2, 3)
    ARRAY_2D = Array2D(ROW, COL)
    for r in range(ROW):
        for c in range(COL):
            ARRAY_2D[r, c] = r + c

    print(ARRAY_2D)
