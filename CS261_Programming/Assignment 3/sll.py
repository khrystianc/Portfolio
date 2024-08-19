# Course: CS261 - Data Structures
# Student Name: Khrystian Clark
# Assignment: Assignment 3, pt 1
# Description: Write the code methods for a Singly Linked List.



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # -------------------Helper methods----------------------------------------------- #
    def addback_help(self, cur, new_tail, prev):
        """Helper for the add_back method"""
        if cur.next is not self.tail:
            prev = cur
            cur = cur.next
            self.addback_help(cur, new_tail, prev)
        else:
            new_tail.next = cur.next
            cur.next = new_tail

    def ins_ind_help(self, count, index, cur, new_point):
        """Helper for the insert at index method"""
        if count < index:
            cur = cur.next
            count += 1
            self.ins_ind_help(count, index, cur, new_point)
        else:
            new_point.next = cur.next
            cur.next = new_point

    def remback_help(self, cur, prev):
        """Helper function for the remove back method"""
        if cur.next is not self.tail:
            prev = cur
            cur = cur.next
            self.remback_help(cur, prev)
        else:
            prev.next = self.tail

    def rem_ind_help(self, count, index, cur, prev):
        """Helper for the remove at index method"""
        if count < index + 1:
            prev = cur
            cur = cur.next
            count += 1
            self.rem_ind_help(count, index, cur, prev)
        else:
            prev.next = cur.next

    def getback_help(self, cur):
        """Helper for the get back method"""
        if cur.next is not self.tail:
            cur = cur.next
            return self.getback_help(cur)
        return cur.value

    def remove_help(self, cur, prev, value):
        """Helper for the remove value method"""
        if cur is not self.tail:
            if cur.value == value:
                prev.next = cur.next
                return True
            else:
                prev = cur
                cur = cur.next
                return self.remove_help(cur, prev, value)
        else:
            return False

    def count_help(self, cur, count, value):
        """Helper for the count the values method"""
        if cur is not self.tail:
            if cur.value == value:
                cur = cur.next
                count += 1
                return self.count_help(cur, count, value)
            else:
                cur = cur.next
                return self.count_help(cur, count, value)
        else:
            return count

    def slice_help(self, start_index, cur, size, new_ll, num):
        """Helper for the slice method"""
        if num < (start_index+1):
            cur = cur.next
            num += 1
            self.slice_help(start_index, cur, size, new_ll, num)
        elif num < (size+start_index+1):
            new_ll.add_back(cur.value)
            cur = cur.next
            num += 1
            self.slice_help(start_index, cur, size, new_ll, num)
        return new_ll


    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node right after the first sentinel/beginning of the list
        """
        new_head = SLNode(value)
        new_head.next = self.head.next
        self.head.next = new_head

    def add_back(self, value: object) -> None:
        """
        Add an element to the back of the SLL
        """
        new_tail = SLNode(value)
        if self.is_empty() is True:
            self.add_front(value)
        else:
            cur = self.head
            prev = cur
            self.addback_help(cur, new_tail, prev) # helper for the recursion

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a specific value at a specific index
        """
        cur = self.head
        count = 0
        new_point = SLNode(value)
        if index == 0:
            self.add_front(value)
        elif index < 0 or index > self.length():
            raise SLLException
        elif index == self.length():
            self.add_back(value)
        else:
            self.ins_ind_help(count, index, cur,new_point)

    def remove_front(self) -> None:
        """
        Removes the front value from an SLL
        """
        if self.is_empty() is True:
            raise SLLException
        self.head = self.head.next

    def remove_back(self) -> None:
        """
        Removes the last element in an SLL
        """
        if self.is_empty() is True:
            raise SLLException
        else:
            cur = self.head
            prev = cur
            self.remback_help(cur, prev)

    def remove_at_index(self, index: int) -> None:
        """
        Removes an item at a specific index in the SLL
        """
        cur = self.head
        count = 0
        prev = cur
        if index == 0:
            self.remove_front()
        elif index == self.length()-1:
            self.remove_back()
        elif index < 0 or index >= self.length():
            raise SLLException
        else:
            self.rem_ind_help(count, index, cur, prev)

    def get_front(self) -> object:
        """
        Returns the front value of the SLL
        """
        if self.is_empty() is True:
            raise SLLException
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        Returns the back value of the SLL
        """
        if self.is_empty() is True:
            raise SLLException
        cur = self.head
        if cur.next is not self.tail:
            cur = cur.next
            return self.getback_help(cur)
        else:
            return cur.value

    def remove(self, value: object) -> bool:
        """
        Removes a specific value from the SLL and returns a bool of if a value was removed
        """
        if self.is_empty() is True:
            return False
        if value == self.head.value:
            self.remove_front()
            return True
        cur = self.head
        prev = None
        if cur is not self.tail:
            return self.remove_help(cur, prev, value)
        return False

    def count(self, value: object) -> int:
        """
        Counts the instances of a specific value in the SLL
        """
        count = 0
        if self.is_empty() is True:
            return count
        cur = self.head
        if cur is not None:
            return self.count_help(cur, count, value)
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Slices a portion of the original SLL into a new one
        """
        if start_index < 0 or start_index >= self.length() or size < 0:
            raise SLLException
        if size > start_index and (size-start_index) > self.length():
            raise SLLException
        if size < start_index and (start_index-size) > self.length():
            raise SLLException
        if size+start_index > self.length():
            raise SLLException
        new_ll = LinkedList()
        cur = self.head
        if size == 0:
            return new_ll
        else:
            num = 0
            self.slice_help(start_index, cur, size, new_ll, num)
        return new_ll





if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)
    
    
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

