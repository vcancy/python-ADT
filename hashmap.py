__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-
from array import Array


class _MapEntry:
    """Storage class for holding the key/value pairs."""

    def __init__(self, key, value):
        self.key = key
        self.value = value


class _HashMapIterator:
    def __init__(self, array):
        self._array = array
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._array):
            if self._array[self._idx] is not None and self._array[self._idx].key is not None:
                key = self._array[self._idx].key
                self._idx += 1
                return key
            self._idx += 1
        else:
            raise StopIteration


class HashMap:
    # Defines constants to represent the status of each table entry.
    UNUSED = None
    EMPTY = _MapEntry(None, None)

    # Create an empty map instance
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        # 超过2/3空间被使用就重新分配
        self._maxCount = len(self._table) - len(self._table) // 3

    def __len__(self):
        """Returns the number of entries in the map."""
        return self._count

    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None

    def add(self, key, value):
        if key in self:
            slot = self._findSlot(key, False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key, True)
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, 'Invalid map key'
        return self._table[slot].value

    def remove(self, key):
        assert key in self, 'Key error %s' % key
        slot = self._findSlot(key, False)
        value = self._table[slot].value
        self._count -= 1
        self._table[slot] = HashMap.EMPTY
        return value

    def _slot_can_insert(self, slot):
        return (self._table[slot] is HashMap.UNUSED or self._table[slot] is HashMap.EMPTY)

    def _findSlot(self, key, forInsert):
        """
        # Finds the slot containing the key or where the key can be added.
        # forInsert indicates if the search is for an insertion, which locates
        # the slot into which the new key can be added.
        """
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)
        # Probe for the key.
        M = len(self._table)
        if not forInsert:
            while self._table[slot] is not HashMap.UNUSED:
                if self._table[slot] is HashMap.EMPTY:
                    slot = (slot + step) % M
                    continue
                elif self._table[slot].key == key:
                    return slot
                slot = (slot + step) % M
            return None
        else:
            while not self._slot_can_insert(slot):
                slot = (slot + step) % M
            return slot

    # The main hash function for mapping keys to table entries
    def _hash1(self, key):
        return abs(hash(key)) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)

    def _rehash(self):
        """Rebuilds the hash table."""

        # Create a new larger table.
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)
        # Modify the size attributes.
        self._count = 0
        self._maxCount = newSize - newSize // 3

        # Add the keys from the original array to the new table
        for entry in origTable:
            if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY:
                slot = self._findSlot(entry.key, True)
                self._table[slot] = entry
                self._count += 1

    def __iter__(self):
        return _HashMapIterator(self._table)


def print_h(h):
    for idx, i in enumerate(h):
        print(idx, i)
    print('\n')


def test_HashMap():
    """ 一些简单的单元测试，不过测试用例覆盖不是很全面 """
    h = HashMap()
    assert len(h) == 0
    h.add('a', 'a')
    assert h.valueOf('a') == 'a'
    assert len(h) == 1

    a_v = h.remove('a')
    assert a_v == 'a'
    assert len(h) == 0

    h.add('a', 'a')
    h.add('b', 'b')
    assert len(h) == 2
    assert h.valueOf('b') == 'b'
    b_v = h.remove('b')
    assert b_v == 'b'
    assert len(h) == 1
    h.remove('a')
    assert len(h) == 0

    n = 10
    for i in range(n):
        h.add(str(i), i)
    assert len(h) == n
    print_h(h)

    for i in range(n):
        assert str(i) in h
    for i in range(n):
        h.remove(str(i))
    assert len(h) == 0
