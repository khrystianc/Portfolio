# Course: CS261 - Data Structures
# Student Name: Khrystian Clark
# Assignment: 1
# Description: 14 problems to display knowledge and understanding of the concepts used in this course.

import random
import string
from a1_include import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def descend(arr, count, size):
    """This is a helper method to return values dependent on if the array is
    descending, not sorted or acending"""
    if count < size-1:
        if arr[count] > arr[count+1]:
            count += 1
            return descend(arr, count, size)
        else:
            return 0
    return 2

def ascend(arr, count, size):
    """This is a helper method to return values dependent on if the array is
    ascending, not sorted or acending"""
    if count < size-1:
        if arr[count] < arr[count+1]:
            count += 1
            return ascend(arr, count, size)
        else:
            return 0
    return 1

def mergesort(arr):
    """Merge sort helper method to sort an array in ascending order. fastest I
    could find to sort 1000 values"""
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def two_intersect(arr1, arr2, new):
    """Finds the intersects of two arrays"""
    m = {}
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    for i in arr1:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    for i in arr2:
        if i in m and m[i]:
            m[i] -= 1
            new.append(i)

def doMath(arr1, arr2):
    """adds the consecutive values in two arrays, and modifies one of the
    arrays to show the answer"""
    for i in range(0, len(arr1)):
        arr2[i] = arr2[i] + arr1[i]
    for i in range(0, len(arr2)-1):
        if arr2[i] >= 10:
            arr2[i] = arr2[i] - 10
            arr2[i+1] = arr2[i+1] + 1
    if arr2[-1] >= 10:
        arr2[-1] = arr2[-1] - 10
        arr2.append(1)


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    Receives a static array and returns a tuple of the min and max values.
    """
    low = arr.get(0)          # low and high number are the first number of the array
    high = arr.get(0)
    count = arr.size() - 1    # set the limit to be the amount of items in the array
    while count >= 0:         # comparisons and adjustments for min and max numbers
        if low > arr[count]:
            low = arr[count]
        if high < arr[count]:
            high = arr[count]
        count -= 1
    if count < 0: # once count finishes last item in the array, it returns nim and max
        return low, high
    return None, None


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Receives a static array and returns a new static array. a number in the original array
    is a multiple of 3, it becomes fizz. if the num is a multiple of 5, the return is buzz.
    If the num is a multiple of 3 and 5, it returns fizzbuzz.
    """
    count = 0
    new_arr = StaticArray(arr.size())          # create a new array to save to
    while count < arr.size():                  # do the math to find if the item is divisible
        item = arr[count]
        if item % 3 == 0 and item % 5 == 0:
            new_arr.set(count, "fizzbuzz")
        elif item % 3 == 0:
            new_arr.set(count, "fizz")
        elif item % 5 == 0:
            new_arr.set(count, "buzz")
        else:
            new_arr.set(count, arr.get(count))
        count += 1                             # increment the counter
    if count == arr.size():                    # return the new array created
        return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Takes a static array and reverses the items in it in place
    """
    size = arr.size()
    count1 = arr.size() - 1
    cut = int(size/2)          # create a number range to manipulate
    for i in range(0, cut):    # performa a placement swap betwen the beginning and the end
        val = arr[count1]
        arr[count1] = arr[i]
        arr[i] = val
        count1 -= 1            # decrement the counter


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    takes a static array, and an integer anf rotates the items in the array the as many times as the input integer requests.
    returns a new static array with the rotated values.
    """
    # Setup counters and new array to store values
    new_arr = StaticArray(arr.size())
    count = arr.size()
    count2 = 0
    # scenario if the input is a positive value
    if steps >= 0:
        if steps > count:   # in the case that the value input is larger than the array size
            steps = steps % count
        if count2 < arr.size():
            for item in range(count - steps, count):
                new_arr.set(count2, arr[item])
                count2 += 1
            for item in range(0, count - steps):
                new_arr.set(count2, arr[item])
                count2 += 1
        return new_arr
    # scenario if the input is a negative value
    if steps < 0:
        step = -steps                                 # make it a positive value
        # First scenario if the new positive value is larger than the array size
        if step > count:
            step = step % count
            for i in range(step, count):
                new_arr.set(count2, arr[i])
                count2 += 1
            for i in range(0, step):
                new_arr.set(count2, arr[i])
                count2 += 1
            return new_arr
        for i in range(step, count):
            new_arr.set(count2, arr[i])
            count2 += 1
        for i in range(0, step):
            new_arr.set(count2, arr[i])
            count2 += 1
        return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    receives two integers and returns a new static array with the value between the two integers entered.
    """
    count = 0
    if start > end: # if the start is bigger than the end value
        size = (start - end) + 1
        arr = StaticArray(size)
        while count < size:
            for i in range(end, start+1):
                arr.set(count, i)
                count += 1
            reverse(arr)
            return arr
    else: # if the end num is bigger
        size = (end - start) + 1
        arr = StaticArray(size)
        while count < size:
            for i in range(start, end+1):
                arr.set(count, i)
                count += 1
            return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Receives an array and lets you know if it is sorted descending, ascending or not at all, with a number value.
    0 = not sorted, 1 = ascending, 2 = descending
    """
    size = arr.size()
    count = 0
    if size < 2:
        return 1
    else:
        while count <= size:
            if arr[count] > arr[count+1]:
                count += 1
                return descend(arr, count, size)
            if arr[count] < arr[count+1]:
                count += 1
                return ascend(arr, count, size)
            else:
                return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    Receives and sorts an array in ascending order. Array is changed in place.
    """
    size = arr.size()
    new_arr = []
    count = 0
    for i in range(0, size):
        new_arr.append(arr[i])
    mergesort(new_arr)
    for j in range(0, size):
        arr.set(count, new_arr[j])
        count += 1


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Receives a static array and returns a new static array without duplicate values.
    """
    new_arr = []
    size = arr.size()
    count = 0
    for i in range(0, size):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])
    new_stat_arr = StaticArray(len(new_arr))
    for i in range(0, len(new_arr)):
        new_stat_arr.set(count, new_arr[count])
        count += 1
    return new_stat_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    With help of mergesort, receives a static array and returns a new array with elements in descending order.
    """
    new_arr = []
    size = arr.size()
    for i in range(0, size):
        new_arr.append(arr[i])
    new_stat_arr = StaticArray(len(new_arr))
    for i in range(0, size):
        new_stat_arr.set(i, arr[i])
    sa_sort(new_stat_arr)
    reverse(new_stat_arr)
    return new_stat_arr
    

# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    Receives 3 static arrays and reutrns on array containing the intersections
    between the 3 arrays.
    """
    n_arr1 = []
    n_arr2 = []
    n_arr3 = []
    almost = []
    final = []
    for i in range(0, arr1.size()):
        n_arr1.append(arr1[i])
    for i in range(0, arr2.size()):
        n_arr2.append(arr2[i])
    for i in range(0, arr3.size()):
        n_arr3.append(arr3[i])
    two_intersect(n_arr1, n_arr2, almost)
    if len(almost) == 0:
        return StaticArray(1)
    two_intersect(almost, n_arr3, final)
    if len(final) == 0:
        return StaticArray(1)
    else:
        new_stat = StaticArray(len(final))
        for i in range(0, new_stat.size()):
            new_stat.set(i, final[i])
        return new_stat


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Receives a static array, and returns a new array of the sorted quares of
    the elements in the array.
    """
    new_arr = []
    size = arr.size()
    for i in range(0, size):
        new_arr.append(arr[i])
    for i in range(0, size):
        new_arr[i] = new_arr[i] * new_arr[i]
    new_stat_arr = StaticArray(len(new_arr))
    for i in range(0, size):
        new_stat_arr.set(i, new_arr[i])
    sa_sort(new_stat_arr)
    return new_stat_arr


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    Receives two arrays and adds numbers between them as if the elements in
    them make one integer.
    """
    n_arr1 = []
    n_arr2 = []
    reverse(arr1)
    reverse(arr2)
    for i in range(0, arr1.size()):
        n_arr1.append(arr1[i])
    for i in range(0, arr2.size()):
        n_arr2.append(arr2[i])
    if len(n_arr1) <= len(n_arr2):
        doMath(n_arr1, n_arr2)
        new_stat = StaticArray(len(n_arr2))
        for i in range(0, len(n_arr2)):
            new_stat.set(i, n_arr2[i])
        reverse(new_stat)
        reverse(arr1)
        reverse(arr2)
        return new_stat
    else:
        doMath(n_arr2, n_arr1)
        new_stat = StaticArray(len(n_arr1))
        for i in range(0, len(n_arr1)):
            new_stat.set(i, n_arr1[i])
        reverse(new_stat)
        reverse(arr1)
        reverse(arr2)
        return new_stat


# ------------------- PROBLEM 13 - BALANCED_STRINGS -------------------------


def balanced_strings(s: str) -> StaticArray:
    """
    TODO: Write this implementation
    """        
    pass

# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    transform the elements of a string to other values based
    on the given input and criteria.
    """
    new_s = ""
    for x in source:
        if x in s1:
            for y in range(0, len(str(s1))):
                if x == s1[y]:
                    new_s += s2[y]
        elif x.isupper() == True:
            new_s += " "
        elif x.islower() == True:
            new_s += "#"
        elif x.isdigit() == True:
            new_s += "!"
        else:
            new_s += "="
    return new_s

# BASIC TESTING
if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randrange(-30000, 30000) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')



    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [random.randrange(-499, 499) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
        [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = sorted_squares(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# balanced_strings example 1')
    test_cases = (
        'aaabbbccc', 'abcabcabc', 'babcCACBCaaB', 'aBcCbA', 'aBc',
        'aBcaCbbAcbCacAbcBa', 'aCBBCAbAAcCAcbCBBa', 'bACcACbbACBa',
        'CBACcbcabcAaABb'
    )
    for case in test_cases:
        print(balanced_strings(case))


    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
