# Course: CS261 - Data Structures
# Assignment: 5
# Student: Khrystian Clark
# Description: Implementing the minheap class and it's functions.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

# -----------------helpers
    def parent(self,index):
        return (index - 1) // 2
    def left(self,index):
        return 1 + index*2
    def right(self,index):
        return 2 + index*2

    def upheap(self, i):  # iterates up the heap
        while i > 0:
            if self.heap.get_at_index(i) < self.heap.get_at_index(self.parent(i)):
                self.heap.swap(i, self.parent(i))
            i = self.parent(i)
    
    def downheap(self, i):  # iterates down the heap
        while i < self.heap.length():
            left = self.left(i)
            right = self.right(i)
            small_child = None
            val = self.heap.get_at_index(i)
            if left < self.heap.length() and val > self.heap.get_at_index(left):
                small_child = left
                val = self.heap.get_at_index(left)
            if right < self.heap.length() and val > self.heap.get_at_index(right):
                small_child = right
                val = self.heap.get_at_index(right)
            if small_child is not None:
                self.heap.swap(i, small_child)
                i = small_child
            else:
                break
# -----------------------

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap maintaining heap property.
        """
        self.heap.append(node)
        self.upheap(self.heap.length() - 1)

    def get_min(self) -> object:
        """
        Returns the minimim key of the minheap without removal
        """
        if self.is_empty():
            raise MinHeapException()
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes the minimim key and returms that key
        """
        if self.is_empty():
            raise MinHeapException()
        val = self.heap.get_at_index(0)
        lastVal = self.heap.pop()
        if self.heap.length() == 0:
            return val
        self.heap.set_at_index(0, lastVal)
        self.downheap(0)
        return val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DA andbuilds a proper MinHeap
        """
        new_heap = DynamicArray()
        for i in range(da.length()):
            val = da.get_at_index(i)
            new_heap.append(val)
        self.heap = new_heap
        node_index = (da.length()-1)//2 - 1 # parent of last node
        while node_index != -1: #percolates through nodes
            self.downheap(node_index)
            node_index -= 1

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
