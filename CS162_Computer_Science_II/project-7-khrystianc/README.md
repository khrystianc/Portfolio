# project-7

Write a LinkedList class that has **recursive** implementations of the **add** and **remove** methods described in the lesson.  It should also have **recursive** implementations of the **contains**, **insert**, and **reverse** methods described in the exercises.  The reverse method should **not** change the _data_ value each node holds - it must rearrange the order of the nodes (by changing the _next_ value each node holds).

It should have a **recursive** method named **to_regular_list** that takes no parameters and returns a regular Python list that has the same values (from the data attribute of the Nodes), in the same order, as the linked list.

It should have a method named **get_head** that takes no parameters and returns the Node object referenced by _head.

The _head_ data member of the LinkedList class must be private.

You may use default arguments and/or helper functions.

Your recursive functions must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments

Here's an example of how a recursive version of the display() method from the lesson could be written:
```
    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)
```

The file must be named: **LinkedList.py**
