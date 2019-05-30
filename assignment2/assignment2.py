class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

class Solution:
    def __init__(self):
        pass

    def find_node(self, root, key):
        """given a binary tree and a key, returns the reference to 
        the node with that key in the tree

        Args:
            root: BinaryTree
            key: int

        Returns:
            Node / None

            If there is no node in the tree with that key return None
        """
        if not root:
            return None

        if root.value == key:
            return root

        left = self.find_node(root.left, key)
        if left:
            return left

        right = self.find_node(root.right, key)
        if right:
            return right

        return None


    def _find_ancestors_helper(self, root, key):
        """Given a binary tree and a key, returns all the ancestors of 
         the node with that key (including the node)

        Args:
            root: BinaryTree
            key: int

        Returns:
            list of ints

            If there is no node in the tree with that key returns None
        """
        if not root:
            return None

        if root.value == key:
            return [root.value]

        left = self._find_ancestors_helper(root.left, key)
        if left:
            left.append(root.value)
            return left

        right = self._find_ancestors_helper(root.right, key)
        if right:
            right.append(root.value)
            return right

        return None
    
    def find_ancestors(self, root, key):
        """See _find_ancestors_helper 

        Given a binary tree and a key, returns all the ancestors of 
        the node with that key 

        Args:
            root: BinaryTree
            key: int

        Returns:
            list of ints

            If there is no node in the tree with that key returns None
        """
        if not self._find_ancestors_helper(root, key):
            return None
        else:
            return self._find_ancestors_helper(root, key)[1:]
"""
    def _common_ancestor_helper(self, root, node1, node2):
        #given two references to two nodes in a binary tree,
        #returns the lowest common ancestor and a boolean flag
        
        if not root:
            return None, False
        
        if root == node1 or root == node2:
            return root, False

        left, found_common_ancestor_l = self._common_ancestor_helper(root.left, node1, node2)
        right, found_common_ancestor_r = self._common_ancestor_helper(root.right, node1, node2)

        if found_common_ancestor_l:
            return left, True
        
        if found_common_ancestor_r:
            return right, False

        if left and right:
            return root, True

        return None, False

    def common_ancestor(self, root, node1, node2):
        #See _common_ancestor_helper 
        #given two references to two nodes in a binary tree,
        #returns the lowest common ancestor 
        
        node, found = self._common_ancestor_helper(root, node1, node2) 

        return node

"""