# Course: CS261 - Data Structures
# Assignment: 5
# Student: Khrystian Clark
# Description: Hash-map implementation and methods to iterate through


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

# -----------------------------Helper Section

    def is_empty(self, llist):
        empty = True
        if llist.length() > 0:
            empty = False
        return empty
# -----------------------------

    def clear(self) -> None:
        """
        Clear the content of the hash map, but does not change the
        table capacity.
        """
        is_clear = LinkedList()
        size = self.capacity
        for i in range(0, size):
            self.buckets.set_at_index(i, is_clear)
            self.size = 0
        pass

    def get(self, key: str) -> object:
        """
        Return the value associated with a specific key.
        Returns None if key is not in the map
        """
        if self.contains_key(key) is False:
            return None
        the_map = self.hash_function(key)
        size = self.capacity
        index = the_map % size
        return self.buckets.get_at_index(index).contains(key).value

    def put(self, key: str, value: object) -> None:
        """
        Update the key/value pair. If the given key exists,
        the value associated is replaced with the new one. Otherwise,
        the key/value pair is added.
        """
        the_map = self.hash_function(key)
        size = self.capacity
        index = the_map % size
        llist = self.buckets.get_at_index(index)
        if self.is_empty(llist) is True:
            llist.insert(key, value)
        elif llist.contains(key) is not None:
            llist.remove(key)
            self.size -= 1
            llist.insert(key, value)
        else:
            llist.insert(key, value)
        self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes a given key and its value from a hash map.
        If the key is not in the hash map, it does nothing.
        """
        the_map = self.hash_function(key)
        size = self.capacity
        index = the_map % size
        value = None
        if self.buckets.get_at_index(index).contains(key) is not None:
            value = self.buckets.get_at_index(index).contains(key).value
            self.buckets.get_at_index(index).remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Returns the bool if the a given key is in the hash map.
        """
        the_map = self.hash_function(key)
        size = self.capacity
        val = the_map % size
        if self.buckets.get_at_index(val).contains(key):
            return True
        return False

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table. Iterates through
        finds empty linkedlists
        """
        empty = 0
        size = self.capacity
        for i in range(0, size):
            if self.buckets.get_at_index(i).length() == 0:
                empty += 1
        return empty

    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the hash table. All existing key/value pairs
        are transferred to the new hash map.
        """
        if new_capacity < 1:
            return
        newhtable = DynamicArray()
        keylist = LinkedList()
        for i in range(new_capacity):  # new empty DA with new cap
            newhtable.append(LinkedList())
        for i in range(0, self.capacity):
            llist = self.buckets.get_at_index(i)
            if self.is_empty(llist) is True:
                continue
            else:
                for item in llist:
                    keylist.insert(item.key, item.value)
        self.size = 0
        self.capacity = new_capacity
        self.buckets = newhtable
        for item in keylist:
            self.put(item.key, item.value)

    def get_keys(self) -> DynamicArray:
        """
        Returns a DA containing all keys stored in the hash map
        """
        new_da = DynamicArray()
        for i in range(0, self.buckets.length()):
            index = self.buckets.get_at_index(i)
            for item in index:
                new_da.append(item.key)
        return new_da


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
