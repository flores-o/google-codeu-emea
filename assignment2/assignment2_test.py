# python -m unittest anagrams_test.py
import unittest
from assignment2 import Node, BinaryTree, Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        # replace this with function construct_binary_tree_from_list 
        self.binary_tree1 = Node(1)
        self.binary_tree1.left = Node(2)
        self.binary_tree1.right = Node(3)

        self.binary_tree2 = Node(1)
        self.binary_tree2.left = Node(2)
        self.binary_tree2.right = Node(3)
        self.binary_tree2.left.left = Node(4)
        self.binary_tree2.left.right = Node(5)
        self.binary_tree2.right.left = Node(6)

        # binary tree in assignment2 example
        self.binary_tree3 = Node(7)
        self.binary_tree3.left = Node(3)
        self.binary_tree3.right = Node(4)
        self.binary_tree3.left.left = Node(2)
        self.binary_tree3.left.right = Node(5)
        self.binary_tree3.right.right = Node(8)
        self.binary_tree3.left.left.left = Node(1)
        self.binary_tree3.left.left.right = Node(6)

        ##########

    def test_find_node(self):

        self.assertEqual(Solution().find_node(self.binary_tree1, 2), self.binary_tree1.left)
        self.assertNotEqual(Solution().find_node(self.binary_tree1, 2), self.binary_tree1.right)
        self.assertEqual(Solution().find_node(self.binary_tree1, 10), None)
        self.assertEqual(Solution().find_node(None, 10), None)

    def test_find_ancestors(self):
        self.assertEqual(Solution().find_ancestors(self.binary_tree3, 6), [2, 3, 7])
        self.assertNotEqual(Solution().find_ancestors(self.binary_tree3, 6), [2, 3, 10])
        self.assertEqual(Solution().find_ancestors(self.binary_tree3, 7), [])
"""
    def test_common_ancestor(self):
        self.assertEqual(Solution().common_ancestor(self.binary_tree3, self.binary_tree3.left.right, self.binary_tree3.left.left.right), self.binary_tree3.left)
"""