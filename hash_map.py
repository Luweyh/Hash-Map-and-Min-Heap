# Course: CS261 - Data Structures
# Assignment: 5
# Student: Luwey Hon
# Description: This program represent a hash map which includes
# a dyanmic array that hold buckets. Each bucket has its own
# linkedlist where it can be traversed to get the keys and
# values. The program implements several ADTs to make use
# of the hash map


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

    def clear(self) -> None:
        """
        Clears the content in the Hash map
        """

        self.size = 0

        pass

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key
        """

        hash_val = self.hash_function(key)
        index = hash_val % self.capacity
        list = self.buckets.get_at_index(index)

        # empty hash map is None
        if list.length() == 0:
            return None

        node = list.contains(key)

        if node is None:
            return None

        return node.value

    def put(self, key: str, value: object) -> None:
        """
        Puts a new key/value in to the hash map
        """

        hash_val = self.hash_function(key)
        index = hash_val % self.capacity
        list = self.buckets.get_at_index(index)

        # when the same key already exist
        if list.contains(key):
            list.remove(key)
            list.insert(key, value)

        # adding a new key/value
        else:
            list.insert(key, value)
            self.size += 1

        pass

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value
        """

        hash_val = self.hash_function(key)
        index = hash_val % self.capacity
        list = self.buckets.get_at_index(index)

        list.remove(key)
        pass

    def contains_key(self, key: str) -> bool:
        """
        Sees if the hash map contains the given key
        """

        hash_val = self.hash_function(key)
        index = hash_val % self.capacity
        list = self.buckets.get_at_index(index)

        # checks to see if the key is contained
        is_contains = 0
        if list.contains(key):
            is_contains += 1

        if is_contains >= 1:
            return True

        return False

    def empty_buckets(self) -> int:
        """
        Returns a number of empty buckets in the hash table
        """

        count = 0

        for num in range(self.capacity):
            if self.buckets.get_at_index(num).length() == 0:
                count += 1

        return count

    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """

        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table
        """
        if new_capacity < 1:
            return

        # making a new bucket
        new_bucket = DynamicArray()
        for _ in range(new_capacity):
            new_bucket.append(LinkedList())


        keys = [None] * self.size
        values = [None] * self.size
        count = 0

        # finding the keys and values
        for num in range(self.buckets.length()):
            # looks at all the linked list
            list = self.buckets.get_at_index(num)
            # iterate through all nodes and store the value
            for pos in list.__iter__():
                keys[count] = pos.key
                values[count] = pos.value
                count += 1     # count the key / size + 1

        # updating the size
        if self.size > 11:
            self.size = count - 1
        else:
            self.size = count


        # iterating through all keys to find the hash value
        for num in range(count):
            key = keys[num]
            if self.hash_function == hash_function_1:
                hash = 0
                for letter in key:
                    hash += ord(letter)

            elif self.hash_function == hash_function_2:
                hash, index = 0, 0
                index = 0
                for letter in key:
                    hash += (index + 1) * ord(letter)
                    index += 1

            # finding the index and rehashing it into new DA
            index = hash % new_capacity
            new_list = new_bucket.get_at_index(index)
            new_list.insert(key, values[num])

        # remove the old buckets
        for num in range(self.buckets.length()):
            self.buckets.pop()

        # add the new buckets
        for num in range(new_capacity):
            self.buckets.append(new_bucket.get_at_index(num))

        # updating capacity
        self.capacity = new_capacity

        pass

    def get_keys(self) -> DynamicArray:
        """
        Get all the keys stored in the hash map
        """

        keys = [None] * (self.size)  # will hold the keys
        count = 0


        for num in range(self.buckets.length()):
            # looks at all the linked list
            list = self.buckets.get_at_index(num)
            # iterate through all nodes and store the value
            for pos in list.__iter__():
                keys[count] = pos.key
                count += 1

        return keys



# BASIC TESTING
if __name__ == "__main__":

    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)


    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)

    #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())

    #
    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)

    #
    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    #
    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)


    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    # # #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')


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

    # #
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
