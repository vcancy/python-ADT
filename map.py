__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-

"""
Implementation of Map ADT using a single list.
"""


class Map():
    """
    A map is a container for storing a collection of data records
    in which each record is associated with a unique key. The key
    components must be comparable.
    """

    def __init__(self):
        self._entryList = list()

    def __len__(self):
        """ :return the number of entries in the map. """
        return len(self._entryList)

    def __contains__(self, item, key):
        """ Determines if the map contains the given key. """
        ndx = self._findPostion(key)
        return ndx is not None

    def __setitem__(self, key, value):
        """
        Adds a new key/value pair to the map if the key is not alre
        -ady in the map or replaces the data associated with the key
        if the key is in the map. Returns True if this is a new key
        and False if the data associated with the existing key is r
        -eplaced.
        Utilize the add() method defined in ADT by overloading the
        __setitem__ method, so that subscript operators can be used
        conveniently.
        """
        ndx = self._findPosition(key)
        if ndx:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def __getitem__(self, key):
        """
        Returns the data record associated with the given key. The
        key must exist in the map or an exception is raised.
        Utilize the valueOf() method defined in ADT by overloading
        the __getitem__() method, so that subscript operators can
        be used conveniently.
        """
        ndx = self._findPosition(key)
        assert ndx is not None, 'Invalid map key'
        return self._entryList[ndx].value

    def remove(self, key):
        """
        Removes the key/value pair for the given key if it is in the
        map and raises an exception otherwise.
        """
        ndx = self._findPosition(key)
        assert ndx, 'Invalid map key'
        self._entryList.pop(key)

    def _findPosition(self, key):
        """
        Many of the methods require a search to determine if the map
        contains a given key. Likewise, we routinely have to locate
        within the list the position containing a specific key/value
        entry.
        The _findPosition() helper method searches the list for the
        given key. If the key is found, the index of its location is
        returned; otherwise, the function returns None to indicate t
        -he key is not contained in the map.
        """
        for i in range(len(self._entryList)):
            if self._entryList[i].key == key:
                return i
        return None

    def __iter__(self):
        return _MapIterator(self._entryList)


class _MapIterator:
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._cur]
            self._idx += 1
            return val
        else:
            raise StopIteration


class _MapEntry:
    """
    Storage class for holding the key/value pairs. It's always
    a good idea that using a storage class to store structured
    data with named fields.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value


if __name__ == '__main__':
    m = Map()
    m['ID'] = 1001
    m['NAME'] = "vcancy"
    m['AGE'] = 22
    print(m['ID'])
    print(m['NAME'])
    print(m['AGE'])
