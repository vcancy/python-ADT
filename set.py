__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

class Set:
    """ 使用list实现set ADT
    Set()
    length()
    contains(element)
    add(element)
    remove(element)
    equals(element)
    isSubsetOf(setB)
    union(setB)
    intersect(setB)
    difference(setB)
    iterator()
    """

    def __init__(self) -> None:
        self._elements = list()

    def __len__(self):
        return len(self._elements)

    def __contains__(self, element):
        return element in self._elements

    def add(self, element):
        if element not in self._elements:
            self._elements.append(element)

    def remove(self, element):
        assert element in self._elements, 'the element must be set'
        self._elements.remove(element)

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    def isSubsetOf(self, setB):
        for element in self._elements:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._elements.extend(self._elements)
        for element in setB:
            if element not in self._elements:
                newSet._elements.append(element)
        return newSet

    def __str__(self):
        return ','.join([str(_) for _ in self._elements])


if __name__ == '__main__':
    set = Set()
    set.add(1)
    set.add(2)
    set.add(1)
    set2 = Set()
    set2.add(1)
    print(set.isSubsetOf(set2))
