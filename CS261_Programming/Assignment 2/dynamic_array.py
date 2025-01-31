# Course: CS261 - Data Structures
# Student Name: Khrystian Clark
# Assignment: Assignment 2, pt1
# Description: Show ability and understanding if the functions of a dynamic array
# Last revised: 02/01/2021


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # ------------------------------------------------------------------ #

    def resize(self, new_capacity: int) -> None:
        """
        Adds to the size of the dynamic array if space needs to be added.
        Does nothing if the new cap is less than the original or negative.
        """
        if new_capacity < self.size:
            # if the new capacity is less than the original size of the DA
            return
        if new_capacity <= 0:
            # if the new cap is 0 or negative
            return
        # or else make a new array of None, and add the old array's values
        else:
            new_arr = StaticArray(new_capacity)
            for i in range(self.size):
                new_arr[i] = self.data[i]
            self.data = new_arr
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Add the given value to the end of the DA. A resizes the array if needed.
        """
        if self.size == self.capacity:
            # if the array is already full, double the capacity
            new_cap = self.capacity * 2
            self.resize(new_cap)
        self.data[self.size] = value
        self.size += 1 # increase size now that there is a new value in the DA.
        
    def insert_at_index(self, index: int, value: object) -> None:
        """
        Add new value to a specific index position in the DA.
        """
        if index < 0: # invalid index error
            raise DynamicArrayException
        if index > self.size: # invalid index error
            raise DynamicArrayException
        if self.size == self.capacity:
            # if the array is already full, double the capacity
            new_cap = self.capacity * 2
            self.resize(new_cap)
            self.insert_at_index(index, value)
        else:
            for i in range(self.size-1, index-1, -1):
                # shifts the array over and then add the value to the index
                self.data[i+1] = self.data[i]
            self.data[index] = value
            self.size += 1 # increment the size

    def remove_at_index(self, index: int) -> None:
        """
        Removes an item from a specific index position.
        """
        if index < 0 or index >= self.size: # invalid index error
            raise DynamicArrayException
        if self.size < (self.capacity / 4):
            #if the number of elements is less than 1/4 the capacity
            # the new capacity is changed to 2*number of elements.
            if self.capacity <= 10:
                if self.size == 0:
                    return
                for i in range(index, (self.size-1)):
                    self.data[i] = self.data[i+1]
                self.data[self.size-1] = 0
                self.size -= 1
                return
            else:
                new_cap = self.size * 2
                self.resize(new_cap)
                if self.capacity <= 10:
                    self.capacity = 10
                self.remove_at_index(index)
        else:
            if self.size == 0:
                return
            for i in range(index, (self.size-1)):
                self.data[i] = self.data[i+1]
            self.data[self.size-1] = 0
            self.size -= 1

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new new DA that has elements from range within the
        given DA.
        """
        if start_index < 0 or start_index > self.size: # invalid index error if start_index is out of bounds
            raise DynamicArrayException
        if size < 0 or size > (self.size - start_index): # invalid if size is out of bounds or ends the new DA out of bounds.
            raise DynamicArrayException
        if size == 0: # if size is 0 return None
            return DynamicArray()
        else:
            new_data = DynamicArray() # establisht the new DA to be manipulated
            for i in range(size): # Add its to the new DA based on the size given, incrementing the start_index
                new_data.append(self.data[start_index])
                start_index += 1
            return new_data

    def merge(self, second_da: object) -> None:
        """
        Merge the original DA with a second DA, added onto the end of the original.
        """
        for i in range(second_da.size): # Anything in a range the length of the DA2
            self.append(second_da[i])

    def map(self, map_func) -> object:
        """
        Manually performs map() function on the DA and returns the output into a new DA.
        """
        new_data = DynamicArray()
        for i in range(self.size):
            new_data.append(map_func(self.data[i]))
        return new_data

    def filter(self, filter_func) -> object:
        """
        Perform the filter() func on a DA, returns a new DA with the information.
        """
        new_data = DynamicArray() # establish new empty DA
        for i in range(self.size): # for every item in the original DA
            if filter_func(self.data[i]) == True: # filter func returns a bool
                new_data.append(self.data[i])
        return new_data

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Perform the reduce() func with a given DA, and the optional initializer
        Ensure you have the correct checks
        """
        if initializer == None and self.size == 0: # check if the func even needs to run
            return None
        if initializer is None: # if only the initializer in None, it is now the first item in the DA
            initializer = self.data[0]
            for i in range(1, self.size): # Run the func down every value in the DA
                initializer = reduce_func(initializer, self.data[i])
            return initializer
        if self.size == 0: # if the DA is empty check
            if initializer != None:
                return initializer
            else:
                return None
        else: # or else it creates a new val with the initial and first item in the DA going through the reduce func.
            val = reduce_func(initializer, self.data[0])
            for i in range(1, self.size): # reduce func iterates through the DA
                val = reduce_func(val, self.data[i])
            return val


# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))