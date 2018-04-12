__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-
from array import Array


class MultiArray:
    def __init__(self, *dimensions):
        assert len(dimensions) > 0, 'Dimension must be >0.'
        self._dims = dimensions
        size = 1  # 数组中元素的总数
        for d in dimensions:
            assert d > 0, 'Dimension must be >0.'
            size *= d
        # 实际存放多维数组数据的一维数组
        self._elements = Array(size)
        # 用于计算元素偏移量的一维数组
        self._factors = Array(len(self._dims))
        # 用于计算_factors
        self._computeFactors()

    def numDims(self):
        """返回维度"""
        return len(self._dims)

    def length(self, dim):
        assert dim > 1 and dim < len(self._dims), 'Dimension component out of range'
        return self._dims[dim - 1]

    def clear(self, value):
        self._elements.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), 'Invalid of array subscripts.'
        index = self._computeIndex(ndxTuple)
        assert index is not None, 'Array subscript out of range.'
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), 'Invalid of array subscript.'
        index = self._computeIndex(ndxTuple)
        assert index is not None, 'Array subscript out of range.'
        self._elements[index] = value

    def _computeIndex(self, idx):
        offset = 0
        for j in range(len(idx)):
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._factors[j]
        return offset

    def _computeFactors(self):
        max_idx = len(self._factors) - 1
        self._factors[max_idx] = 1
        for i in range(max_idx, 0, -1):
            self._factors[i - 1] = self._dims[i] * self._factors[i]


if __name__ == '__main__':
    test = MultiArray(3,3,3)
    test.clear(10)
    test[1,2,1] = 55
    print(test[1,1,1])
    print(test[1,2,1])