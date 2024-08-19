# Course: CS261 - Data Structures
# Student Name: Khrystian Clark
# Assignment: Assignment 3, pt3
# Description: Circular Doubly Linked List class and methods.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #
    # place helper functions here
    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds value to the front of the CDLL
        """
        new_head = DLNode(value)
        if self.sentinel.prev == self.sentinel:  # If you are initiating an empty list
            new_head.prev = self.sentinel
            new_head.next = self.sentinel.next
            self.sentinel.prev = new_head
            self.sentinel.next = new_head
        else:
            new_head.prev = self.sentinel
            new_head.next = self.sentinel.next
            self.sentinel.next.prev = new_head
            self.sentinel.next = new_head

    def add_back(self, value: object) -> None:
        """
        Adds a value to the back of the CDLL
        """
        new_back = DLNode(value)
        if self.is_empty() is True:  # initiate first element in the LL
            self.add_front(value)
        else:
            new_back.prev = self.sentinel.prev
            new_back.next = self.sentinel
            self.sentinel.prev.next = new_back
            self.sentinel.prev = new_back

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a specific value at a specific index of the LL
        """
        new_node = DLNode(value)
        if index < 0 or index > self.length():  # Raise the exception if the index requested in out of bounds
            raise CDLLException
        if index == 0:  # if the requested index is the front, then we use the add_front method
            self.add_front(value)
        else:  # else we iterate and place the value at the index
            cur = self.sentinel.next
            for i in range(index):
                cur = cur.next
            new_node.prev = cur.prev
            cur.prev.next = new_node
            new_node.next = cur
            cur.prev = new_node

    def remove_front(self) -> None:
        """
        Removes the front value of the LL
        """
        if self.is_empty() is True:  # raise exception if the LL is empty
            raise CDLLException
        else:
            self.sentinel.next.next.prev = self.sentinel
            self.sentinel.next = self.sentinel.next.next

    def remove_back(self) -> None:
        """
        Removes the last item of a LL
        """
        if self.is_empty() is True:  # raises the exception if the LL is empty
            raise CDLLException
        else:
            self.sentinel.prev.prev.next = self.sentinel
            self.sentinel.prev = self.sentinel.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
        Removes the item at a specific index of the LL
        """
        if index < 0 or index >= self.length():  # check raises exception
            raise CDLLException
        if self.is_empty() is True:  # check raises exception
            raise CDLLException
        if index == 0:
            self.remove_front()
        else:  # iterate through to find the index and remove the value
            cur = self.sentinel.next
            for i in range(index):
                cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    def get_front(self) -> object:
        """
        Returns the item at the from of the LL
        """
        if self.is_empty() is True:
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Returns the item at the back of a CDLL
        """
        if self.is_empty() is True:
            raise CDLLException
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Finds and removes a specific value from a CDLL and returns the bool if
        an item was removed.
        """
        if self.is_empty() is True:
            return False
        cur = self.sentinel.next
        while cur != self.sentinel:
            if cur.value == value:
                if cur.prev != self.sentinel and cur.next != self.sentinel:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                if cur.prev == self.sentinel and cur.next != self.sentinel:
                    self.remove_front()
                if cur.prev != self.sentinel and cur.next == self.sentinel:
                    self.remove_back()
                return True
            else:
                cur = cur.next
        return False

    def count(self, value: object) -> int:
        """
        Counts the amount of times a specific value is present in the CDLL
        """
        count = 0
        cur = self.sentinel.next
        if self.is_empty() is True:
            return count
        while cur is not self.sentinel:
            if cur.value == value:
                cur = cur.next
                count += 1
            else:
                cur = cur.next
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        if self.is_empty() is True:
            raise CDLLException
        if index1 < 0 or index1 > self.length():
            raise CDLLException
        if index2 < 0 or index2 > self.length():
            raise CDLLException
        else:
            node1 = self.sentinel.next
            node2 = self.sentinel.next
            for i in range(index1):
                node1 = node1.next
            for i in range(index2):
                node2 = node2.next
        """
        pass

    def reverse(self) -> None:
        """
        Reverses the CDLL in place
        """
        cur = self.sentinel.next
        next_point = cur.next
        while cur is not self.sentinel:
            cur.next = cur.prev
            cur.prev = next_point
            cur = next_point
            next_point = cur.next
        temp = cur.prev
        cur.prev = cur.next
        cur.next = temp

    def sort(self) -> None:
        """
        Sorts the CDLL in place
        """
        if self.is_empty() is True:
            return
        cur = self.sentinel.next
        new_num = None
        while cur is not self.sentinel:
            new_num = cur.next
            while new_num is not self.sentinel:
                if cur.value > new_num.value:
                    temp = cur.value
                    cur.value = new_num.value
                    new_num.value = temp
                new_num = new_num.next
            cur = cur.next

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty() is True:
            return
        if steps == 0 or steps == self.length():
            return
        cur = self.sentinel.next
        end = self.sentinel.prev
        if steps > 0:
            if steps > self.length():
                new_steps = steps % self.length()
                self.rotate(new_steps)
            for i in range(steps):
                end.prev = self.sentinel
                end.next = self.sentinel.next
                self.sentinel.next.prev = end
                self.sentinel.next = end
                self.sentinel.prev.prev.next = self.sentinel
        if steps < 0:
            for i in range(-steps):
                temp = self.sentinel.next
                head = temp.next
                head.prev = self.sentinel
                self.sentinel.prev.next = temp
                temp.prev = self.sentinel.prev
                self.sentinel.prev = self.sentinel.prev.next
                self.sentinel.prev.next = self.sentinel
            return
        pass

    def remove_duplicates(self) -> None:
        """
        TODO: Write this implementation
        """
        """if self.is_empty() is True:
            return
        cur = self.sentinel.next
        self.remdup_help(cur)

    def remdup_help(self, cur):
        if cur is not self.sentinel:
            if self.count(cur.value) > 1:
                the_dup = cur

                for i in range(self.count(the_dup.value)):
                    self.remove(the_dup.value)
                self.remdup_help(cur)
            else:
                cur = cur.next
                self.remdup_help(cur)
        else:
            return"""
        pass

    def odd_even(self) -> None:
        """
        Segregates the odd and even values in a CDLL, with odds first
        """
        if self.is_empty() is True:
            return
        if self.length() == 1:
            return
        head1 = self.sentinel.next
        head2, head2_beg = self.sentinel.next.next, self.sentinel.next.next
        while head2.next != self.sentinel and head2.next.next != self.sentinel:
            head1.next = head2.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next
        if head2.next != self.sentinel:
            head1.next = head2.next
            head1 = head1.next
        head1.next = head2_beg
        head2.next = self.sentinel

    def add_integer(self, num: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)

    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)

    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())

    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)

    print('\n# reverse example 3')


    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age

        def __eq__(self, other):
            return self.age == other.age

        def __str__(self):
            return str(self.name) + ' ' + str(self.age)


    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)

    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)

    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)

    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)

    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)

    print('\n# add_integer example 1')
    test_cases = (
       ([1, 2, 3], 10456),
       ([], 25),
       ([2, 0, 9, 0, 7], 108),
        ([9, 9, 9], 9_999_999),
    )
    for list_content, integer in test_cases:
       lst = CircularList(list_content)
    print('INPUT :', lst, 'INTEGER', integer)
    lst.add_integer(integer)
    print('OUTPUT:', lst)
