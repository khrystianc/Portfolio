# Author: Khrystian Clark
# Date: 11/12/2020
# Description: A program that navigated through a Linked List using a series of
#              methods with recursion.

class Node:
    """Represents a node in a linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A linked list implementation of the List ADT"""

    def __init__(self):
        self._head = None

    def add_rec(self, current, val):  # Helper to make the recursive
        """Helper: Adds a node containing val to the linked list"""
        if current is None:  # If the list is empty
            return Node(val)
        current.next = self.add_rec(current.next, val)
        return current

    def add(self, val):
        """Adds a node containing val to the linked list"""
        return self.add_rec(self._head, val)

    def remove_rec(self, current, previous, val):
        """Helper: Removes the node containing val from the linked list"""
        if current is None:  # If the list is empty
            return False
        if current.data == val:  # If the node to remove is the head
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
            return True
        return self.remove_rec(current.next, current, val)

    def remove(self, val):
        """Removes the node containing val from the linked list"""
        return self.remove_rec(self._head, None, val)

    def contains_rec(self, current, key):
        """Helper: Returns True if the list contains a Node with the value key,
        otherwise returns False"""
        if current is None:
            return False
        if current.data == key:
            return True
        else:
            return self.contains_rec(current.next, key)

    def contains(self, key):
        """Returns True if the list contains a Node with the value key,
        otherwise returns False"""
        return self.contains_rec(self._head, key)

    def insert_rec(self, current, val, pos):
        """Helper: Inserts a node containing val into the linked list at position pos"""
        if pos == 0:
            temp = Node(val)
            temp.next = current
            return temp
        if current is None:
            return Node(val)
        else:
            current.next = self.insert_rec(current, val, pos-1)
            return current

    def insert(self, val, pos):
        """Inserts a node containing val into the linked list at position pos"""
        self.insert_rec(self._head, val, pos)

    def reverse_rec(self, current):
        """Helper: Reverses the linked list"""
        if current is None:
            return current
        if current.next is None:
            self._head = current
            return current
        next_place = current.next
        next_place.next = current
        current.next = None
        return self.reverse_rec(current.next)

    def reverse(self):
        """Reverses the linked list"""
        return self.reverse_rec(self._head)

    def to_reg_list_rec(self, current, result):
        """Helper: Returns a regular Python list containing the same values,
        in the same order, as the linked list"""
        if current is None:
            return result
        result.append(current.data)
        return self.to_reg_list_rec(current.next, result)

    def to_regular_list(self):
        """Returns a regular Python list containing the same values,
        in the same order, as the linked list"""
        result = []
        self.to_reg_list_rec(self._head, result)
        return result

    def get_head(self):
        """Get method: Returns node object referenced by _head"""
        return self._head

    def display_rec(self, current):
        """Helper: Prints out the values in the linked list"""
        if current is None:
            return
        print(current.data, end=" ")
        self.display_rec(current.next)

    def display(self):
        """Prints out the values in the linked list"""
        self.display_rec(self._head)

    def is_empty(self):
        """Returns True if the linked list is empty,
        returns False otherwise"""
        return self._head is None
