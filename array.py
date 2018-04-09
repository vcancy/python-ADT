'''
array: 定长，操作有限，但是节省内存
'''
import ctypes


class Array:
    """
    实现一个array的ADT
    """

    def __init__(self, size) -> None:
        assert size > 0, 'array size must be > 0'
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < len(self), 'out of index'
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), 'out of index'
        self._elements[index] = value

    def clear(self, value):
        """设置每个元素为value"""
        for _ in range(len(self)):
            self._elements[_] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        return ','.join([str(e) for e in self._elements])


class _ArrayIterator:
    def __init__(self, items) -> None:
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration


if __name__ == '__main__':
    A = Array(5)
    for i in range(len(A)):
        A[i] = i
    print(A)
    for _ in A:
        print(_)
