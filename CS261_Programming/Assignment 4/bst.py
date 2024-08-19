# Course: CS261 - Data Structures
# Student Name: Khrystian Clark
# Assignment: 4
# Description: Binary Search Tree and methods to help iterate and traverse


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #
    def pre_o_t_help(self, cur, ans):
        ans.enqueue(cur)
        if cur.left is not None:
            self.pre_o_t_help(cur.left, ans)
        if cur.right is not None:
            self.pre_o_t_help(cur.right, ans)

    def i_o_t_help(self, cur, ans):
        if cur.left is not None:
            self.i_o_t_help(cur.left, ans)
        ans.enqueue(cur)
        if cur.right is not None:
            self.i_o_t_help(cur.right, ans)

    def post_o_t_help(self, cur, ans):
        if cur.left is not None:
            self.post_o_t_help(cur.left, ans)
        if cur.right is not None:
            self.post_o_t_help(cur.right, ans)
        ans.enqueue(cur)

    def size_help(self, cur):
        count = 1
        if cur.left is not None:
            count += self.size_help(cur.left)
        if cur.right is not None:
            count += self.size_help(cur.right)
        return count

    def height_help(self, cur):
        if self.check_leaf(cur) is True:
            return 0
        if cur.left is not None and cur.right is None:
            return 1 + self.height_help(cur.left)
        if cur.left is None and cur.right is not None:
            return 1 + self.height_help(cur.right)
        if self.height_help(cur.left) > self.height_help(cur.right):
            return 1 + self.height_help(cur.left)
        else:
            return 1 + self.height_help(cur.right)

    def check_leaf(self, cur):
        if cur.left is None and cur.right is None:
            return True
        return False

    def count_leaves_help(self, cur):
        if self.check_leaf(cur) is True:
            return 1
        if cur.left is not None and cur.right is None:
            return self.count_leaves_help(cur.left)
        if cur.left is None and cur.right is not None:
            return self.count_leaves_help(cur.right)
        ans = self.count_leaves_help(cur.left) + self.count_leaves_help(cur.right)
        return ans

    def full_help(self, cur): #edit return or change order
        if self.check_leaf(cur) is True:
            return True
        if cur.left is None and cur.right is not None:
            return False
        if cur.left is not None and cur.right is None:
            return False
        return True and self.full_help(cur.left) and self.full_help(cur.right)

    def perfect_help(self, cur, num, steps):
        # handle base case where iteration limit reached without returning false
        if num == steps:
            return True

        # handle base case where node with < 2 children found
        if cur.left is None or cur.right is None:
            return False

        # handle recursive case where node has 2 children
        return self.perfect_help(cur.left, num + 1, steps) and self.perfect_help(cur.right, num + 1, steps)

    def get_min(self, cur):
        if self.root is None:
            return
        else:
            parent = None
            while cur.left is not None:
                parent = cur
                cur = cur.left
            return cur, parent

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Add a new node to a BST
        """
        if self.root is None:
            self.root = TreeNode(value)
            return
        new_node = TreeNode(value)  # Create the new node to be added
        ele = self.root  # Set the pointer to where the new element is to be added
        pos = None  # Set the pointer to where the last position of the last pointer was
        while ele is not None:
            pos = ele
            if value < ele.value:
                ele = ele.left
            else:
                ele = ele.right
        if value < pos.value:  # new node is less than other parent, it goes on the left
            pos.left = new_node
        else:  # or else add it at the right child
            pos.right = new_node

    def contains(self, value: object) -> bool:
        """
        Check if the BST contains a given value, and returns the bool.
        """
        cur = self.root
        while cur is not None:
            if value > cur.value:  # Checks down the right side of the branch
                cur = cur.right
            elif value < cur.value:  # Check down the left side of the branches
                cur = cur.left
            elif value == cur.value:
                return True
        return False

    def get_first(self) -> object:
        """
        Returns the value stored as the first node in the BST
        """
        if self.root is None:  # if the tree is empty, returns None
            return None
        return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the first value in a BST and returns the bool if it did/did not
        """
        if self.root is None:  # If the tree is empty
            return False
        if self.check_leaf(self.root) is True:  # if there is only one value, delete and return true
            self.root = None
            return True
        if self.root.right is None:  # if the root only have a left leaf/node
            self.root = self.root.left
            return True
        if self.root.left is None:
            self.root = self.root.right
            return True
        new_node = self.root.right
        new_parent = self.root
        left_bool = False
        while new_node.left is not None:
            new_parent = new_node
            new_node = new_node.left
            left_bool = True
        if left_bool is True:
            new_parent.left = new_node.right
        else:
            new_parent.right = new_node.right
        new_node.left = self.root.left
        new_node.right = self.root.right
        self.root = new_node
        return True

    def remove(self, value) -> bool:
        """
        Removes a specific value from the BST
        """
        left_bool = False
        node_found = False
        parent = None
        to_remove = self.root
        while to_remove is not None and not node_found:  # search to find the value
            if value == to_remove.value:
                node_found = True
            elif value < to_remove.value:
                parent = to_remove
                to_remove = to_remove.left
                left_bool = True
            else:
                parent = to_remove
                to_remove = to_remove.right
                left_bool = False
        if not node_found:  # if the value is not present, return False
            return False
        if to_remove == self.root:  # if the value to remove is the first node
            self.remove_first()
            return True
        if self.check_leaf(to_remove) and left_bool:  # if the value is a leaf
            parent.left = None
            return True
        if self.check_leaf(to_remove) and not left_bool:
            parent.right = None
            return True
        if to_remove.right is None and left_bool:  # only left subtree
            parent.left = to_remove.left
            return True
        if to_remove.right is None and not left_bool:
            parent.right = to_remove.left
            return True
        left_bool_2 = False  # has a right subtree find left-most child from right subtree
        replace_node = to_remove.right
        replace_parent = to_remove
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool_2 = True
            if left_bool_2:
                replace_parent.left = replace_node.right
            if not left_bool_2:
                replace_parent.right = replace_node.right
        if left_bool:
            parent.left = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True
        if not left_bool:
            parent.right = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True

    def pre_order_traversal(self) -> Queue:
        """
        Returns the pre-order traversal
        """
        the_ans = Queue()
        if self.root is None:
            return the_ans
        cur = self.root
        self.pre_o_t_help(cur, the_ans)
        return the_ans

    def in_order_traversal(self) -> Queue:
        """
        Returns the in order traversal
        """
        the_ans = Queue()
        if self.root is None:
            return the_ans
        cur = self.root
        self.i_o_t_help(cur, the_ans)
        return the_ans

    def post_order_traversal(self) -> Queue:
        """
        Returns the post order traversal
        """
        the_ans = Queue()
        if self.root is None:
            return the_ans
        cur = self.root
        self.post_o_t_help(cur, the_ans)
        return the_ans

    def by_level_traversal(self) -> Queue:
        """
        Returns the by level traversal
        """
        almost_ans = Queue()
        the_ans = Queue()
        if self.root is None:
            return the_ans
        cur = self.root
        almost_ans.enqueue(cur)
        while almost_ans.is_empty() is False:
            add_node = almost_ans.dequeue()
            if add_node is not None:
                the_ans.enqueue(add_node)
                almost_ans.enqueue(add_node.left)
                almost_ans.enqueue(add_node.right)
        return the_ans

    def is_full(self) -> bool:
        """
        Returns the bool if the BST is full
        """
        if self.root is None:
            return True
        if self.root.left is None and self.root.right is None:
            return True
        cur = self.root
        return self.full_help(cur)

    def is_complete(self) -> bool: # spacing issue
        """
        Returns the bool if the BST is complete
        """
        if self.root is None:
            return True
        if self.is_perfect():
            return True
        ans = Queue()
        ans.enqueue(self.root)
        complete = False
        while ans.is_empty() is False:
            cur = ans.dequeue()
            if complete and cur.left or cur.right:
                return False
            if cur.left is None and cur.right:
                return False
            if cur.left:
                ans.enqueue(cur.left)
            else:
                complete = True
            if cur.right:
                ans.enqueue(cur.right)
            else:
                complete = True
        return True

    def is_perfect(self) -> bool:
        """
        Returns bool if the BST is perfect
        """
        # handle case where BST is empty
        if self.root is None:
            return True
        # iterate through BST while testing for perfect property
        height = self.height()
        return self.perfect_help(self.root, 0, height)

    def size(self) -> int:
        """
        Returns the number of nodes in a BSN
        """
        if self.root is None:
            return 0
        cur = self.root
        return self.size_help(cur)

    def height(self) -> int:
        """
        Returns how many levels are the in the BST
        """
        if self.root is None:
            return -1
        cur = self.root
        return self.height_help(cur)

    def count_leaves(self) -> int:
        """
        Returns the number of leaves in the BST
        """
        if self.root is None:
            return 0
        cur = self.root
        return self.count_leaves_help(cur)

    def count_unique(self) -> int:
        """
        Returns the number of unique elements in a BST
        count = 0
        parent = None
        cur = self.root
        # handle case where BST is empty
        if cur is None:
            return count
        # call recursive helper function to count unique values
        return self.unique_help(cur, parent, count)
        """



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8} ',
              f'{str(tree.is_complete()):10} ',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())} ')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

