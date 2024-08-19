# Course: CS261 - Data Structures
# Student Name: Khrystian Clark
# Assignment: Assignment 3, pt 2
# Description: Write code methods for the MaxStack class


from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def is_empty(self) -> bool:
        """
        Return True is Maxstack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the MaxStack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.length()

    # ------------------------------------------------------------------ #

    def push(self, value: object) -> None:
        """
        Pushes a new value to the top of the max stack
        """
        self.sll_val.add_front(value)

    def pop(self) -> object:
        """
        Pops the top values off of the max stack
        """
        if self.is_empty() is True:
            raise StackException
        else:
            prev = self.sll_val.get_front()
            self.sll_val.remove_front()
            return prev

    def top(self) -> object:
        """
        Returns the value of the item at the top of the stack
        """
        if self.is_empty() is True:
            raise StackException
        return self.sll_val.get_front()

    def get_max(self) -> object:
        """
        Retrieves the maximum valeu of the max stack
        """
        if self.is_empty() is True:
            raise StackException
        if self.size() == 1:
            return self.sll_val.get_front()
        else:
            cur = self.sll_val.head.next
            maxi = cur.value
            while cur is not self.sll_val.tail:
                if cur.value > maxi:
                    maxi = cur.value
                    cur = cur.next
                else:
                    cur = cur.next
            return maxi


# BASIC TESTING
if __name__ == "__main__":
    pass

    print('\n# push example 1')
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print('\n# pop example 1')
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print('\n# top example 1')
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)

    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))

