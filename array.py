__author__ = "vcancy"
# /usr/bin/python
# -*-coding:utf-8-*-

# Data Structures and Algorithms Using Python
# CHAPTER 2: Arrays
# Listing 2.1: array.py

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
        """
        When the subscript notation is used in a program,
        y = x[i], Python will call the __getitem__ method,
        passing the value of i to the index parameter.
        """
        assert 0 <= index < len(self), 'out of index'
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        The __setitem__ operator method is used to set or
        change the contents of a specific element of the
        array. It takes two arguments: the array index of
        the element being modified and the new value that
        will be stored in that element.
        The order of the two arguments is extremely import
        -ant. The parameter 'index' must be passed as the
        first argument(after self), then followed the para
        -meter 'value'.
        """
        assert 0 <= index < len(self), 'out of index'
        self._elements[index] = value

    def clear(self, value):
        """设置每个元素为value"""
        for _ in range(len(self)):
            self._elements[_] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the
        elements. --> an instance of the _ArrayIterator.
        """
        return _ArrayIterator(self._elements)

    def __str__(self):
        return ','.join([str(e) for e in self._elements])


class _ArrayIterator:
    """
    To use Python's traversal mechanism with our own
    abstract data types, we must define an iterator
    class, which is a class in Python containing two
    special methods, __iter__() and next(). Iterator
    classes are commonly defined in the same module
    as the corresponding container class.
    """

    def __init__(self, items) -> None:
        self._items = items
        self._idx = 0

    def __iter__(self):
        """
        The __iter__ method simply returns a reference
        to the object itself and is always implemented
        to do so.
        """
        return self

    def __next__(self):
        """
        The next() method is called to return the next
        item in the container. The method first saves a
        reference to the current item indicated by the
        loop variable. The loop variable is the incremen
        -ted by one to prepare it for the next invocation
        of the next() method. If there are no additional
        items, the method must raise a StopIteration excep
        -tion that flags the for loop to terminate.
        """
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
