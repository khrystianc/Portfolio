# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

import random

from bst import BST
from bst import TreeNode
from bst import Stack
from bst import Queue


class AVLTreeNode(TreeNode):
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None
        self.height = 0


class AVL(BST):
    def add(self, value):
        """
        insert key, value into tree like normal BST insertion
        """
        node = TreeNode(value)
        par = node.parent
        while par is not None:
            rebalance(par)
            par = par.parent

    def remove(self, value) -> bool:
        """
        TODO: Write your implementation
        """
        #Perform normal BST
        if not self.root:
            return TreeNode(value)
        elif value < self.root.value:
            self.root.left = self.insert(self.root.left, value)
        else:
            self.root.right = self.insert(self.root.right, value)

        #Update the height of the ancestor node
        self.root.height = 1 + max(self.get_height(self.root.left), self.get_height(root,right))
        #get the balance factor
        balance = self.get_balance(root)
        
        #If the inserted node is unbalanced
        #1. Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        #2. Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        #3. Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        #4. Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    

    """def rotate_left(self, x):
        y = x.right  # C ← N.right
        x.right = y.left  # N.right ← C.left
        if y.left is not None:
            y.left.parent = x  # N.right.parent ← N
        if x.parent is None:  # x is the root
            self.root = y
        elif x == x.parent.left:  # if x is left child
            x.parent.left = y
        else:  # x is the right child
            x.parent.right = y
        y.left = x
        x.parent = y
        self.update_height(x)
        self.update_height(y)
        self.rebalance(y)

    def rotate_right(self, x):
        y = x.left  # C ← N.right
        x.left = y.right  # N.right ← C.left
        if y.right is not None:
            y.right.parent = x  # N.right.parent ← N
        if x.parent is None:  # x is the root
            self.root = y
        elif x == x.parent.right:  # if x is left child
            x.parent.right = y
        else:  # x is the right child
            x.parent.left = y
        y.right = x
        x.parent = y
        self.update_height(x)
        self.update_height(y)

    def update_height(self, x):
        x.height = max(self.height(x.left), self.height(x.right)) + 1

    def balance_factor(self, x):
        if x is not None:
            return 0
        else:
            return self.height(x.left) - self.height(x.right)

    def rebalance(self, x):
        if self.balance_factor(x) < -1:
            if self.balance_factor(x.left) > 0:
                x.left = self.rotate_left(x.left)
                x.left.parent = x
            new_sub_root = self.rotate_right(x)
            new_sub_root.parent = x.parent
            x.parent.left or x.parent.right = new_sub_root
        elif self.balance_factor(x) > 1:
            if self.balanceFactor(x.right) < 0:
                x.right = self.rotate_right(x.right)
                x.right.parent = x
            new_sub_root = self.rotate_left(x)
            new_sub_root.parent = x.parent
            x.parent.left or x.parent.right = new_sub_root
        else:
            self.update_height(x)"""





if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),          #RR
        (3, 2, 1),          #LL
        (1, 3, 2),          #RL
        (3, 1, 2),          #LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)


    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 30, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),                             # no AVL rotation
        ((1, 2, 3), 2),                             # no AVL rotation
        ((1, 2, 3), 3),                             # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),     # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),     # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),     # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),     # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),     # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),     # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),     # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl.size(), avl, avl.root)
        avl.remove(avl.root.value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL(case)
        if avl.size() != len(case):
            raise Exception("PROBLEM WITH ADD OPERATION")
        for value in case[::2]:
            avl.remove(value)
        if avl.size() != len(case) - len(case[::2]):
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('Stress test finished')


    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = AVL()
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
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())


    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = AVL()
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
