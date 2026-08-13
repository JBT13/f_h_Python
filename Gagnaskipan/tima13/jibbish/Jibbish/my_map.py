from collections.abc import MutableMapping
from itertools import chain
from collections import namedtuple


def polynomial_rolling_hash(s):
    """
    A polynomial rolling hash function using a prime number (31) as the multiplier.
    """
    hash_code = 0
    for c in s:
        hash_code = (hash_code * 31) + ord(c)  # ord() returns unicode-value of c
    return hash_code

def h1(s: str) -> int:
    """Hash code generation."""
    # return 0
    # return len(s)
    return polynomial_rolling_hash(s)

def h2(n: int, max_n: int) -> int:
    """Compresses hash-code into range [0, max_n-1]."""
    assert max_n > 0, "Invalid max_n"
    return n % max_n

def h(s: str, max_n: int) -> int:
    """Hash function returning a hash value for input string."""
    return h2(h1(s), max_n)

class MyMap(MutableMapping):

    # Define a named tuple class named 'Item' with fields 'key' and 'value'.
    # This represents a (key, value) pair in our map; create new as: self.Item(key, value)
    Item = namedtuple('Item', ['key', 'value'])

    def _in_array(self, bucket: list[Item], key: str) -> int | None:
        """ If item with given key is in the array, return its index, otherwise return None. """
        for i in range(len(bucket)):
            if bucket[i].key == key:
                return i
        return None

    def _load_factor(self):
        return self._len / len(self._array)

    def __repr__(self):
        bucket_sizes = []
        for bucket in self._array:
            bucket_sizes.append(len(bucket))
        return str(bucket_sizes)

    def __init__(self, size_arr: int = 1, max_load_factor = None):
        assert size_arr > 0, "Invalid array size"
        self._max_load_factor = max_load_factor # Do automatically resize when load-factor exceeds max_load_factor
        self._array = [[] for _ in range(size_arr)]
        self._len = 0

    def __iter__(self):
        """
        Returns an iterator; note, for dictionaries one iterates on the keys (not key-value pairs)
        """
        return chain.from_iterable(self._array)  # NOTE: key or not?"

    def __str__(self):
        """
        Returns a string representation of the dictionary (in the same format as Python dict, e.g. {1: 755, 2: 290}
        """
        items = []
        for item in self:
            items.append(f'{item[0]}: {item[1]}')
        return '{' + ', '.join(items) + '}'

    def __len__(self):
        """
        Returns the number of entries in the dictionary.
        """
        return self._len

    # ------------------------------------------------------------------

    def __setitem__(self, key, value):
        # 1. Check for resize
        if self._max_load_factor is not None and 0.0 < self._max_load_factor <= self._load_factor():
            self._resize()

        # 2. Find the correct bucket
        bucket_id = h(key, len(self._array))
        bucket = self._array[bucket_id]
        
        # 3. Check if key already exists
        index = self._in_array(bucket, key)
        new_item = self.Item(key, value)

        if index is None:
            # Add new item
            bucket.append(new_item)
            self._len += 1
        else:
            # Update existing item
            bucket[index] = new_item

    def __getitem__(self, key):
        bucket_id = h(key, len(self._array))
        bucket = self._array[bucket_id]
        
        index = self._in_array(bucket, key)
        if index is not None:
            return bucket[index].value
        
        raise KeyError(f"Key '{key}' not found.")

    def __delitem__(self, key):
        bucket_id = h(key, len(self._array))
        bucket = self._array[bucket_id]
        
        index = self._in_array(bucket, key)
        if index is not None:
            bucket.pop(index)
            self._len -= 1
            return
        
        raise KeyError(f"Key '{key}' not found.")

    def _resize(self):
        # 1. Save the old data
        old_array = self._array
        
        # 2. Double the capacity and reset the map
        new_capacity = len(old_array) * 2
        self._array = [[] for _ in range(new_capacity)]
        self._len = 0 # Reset length because __setitem__ will re-increment it
        
        # 3. Rehash: Iterate through every bucket and every item
        for bucket in old_array:
            for item in bucket:
                # Use the existing __setitem__ to put items in the new larger array
                self.__setitem__(item.key, item.value)