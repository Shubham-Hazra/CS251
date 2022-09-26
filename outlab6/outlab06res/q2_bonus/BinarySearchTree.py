from BSTNode import *

class BinarySearchTree:
    """Implementation of a Binary Search Tree

    :param root: This is a pointer to the root node, defaults to None
    :type root: BSTNode
    """
    def __init__(self):
        """Constructor method

        >>> tree = BinarySearchTree()
        >>> tree.traverse("IN")
        >>> tree.traverse("PRE")

        """
        self.root = None
    
    def insert(self, val):
        """Object method to insert a new node into the tree

        :param val: The value to be inserted into the tree 
        :type val: int

        >>> tree = BinarySearchTree()
        >>> tree.insert(43)
        >>> tree.insert(34)
        >>> tree.insert(78)
        >>> tree.insert(18)
        >>> tree.insert(69)
        >>> tree.traverse("IN")
        18 34 43 69 78 

        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """Object method to traverse the tree in the order given and printing the elements

        :param order: The order in which to traverse the tree. Can be "PRE" for preorder, "POST" for postorder or "IN" for inorder.
        :type order: str

        >>> tree = BinarySearchTree()
        >>> tree.insert(43)
        >>> tree.insert(34)
        >>> tree.insert(78)
        >>> tree.insert(18)
        >>> tree.insert(69)
        >>> tree.traverse("IN")
        18 34 43 69 78 
        >>> tree.traverse("PRE")
        43 34 18 78 69 
        >>> tree.traverse("POST")
        18 34 69 78 43 

        """
        if self.root == None:
            return
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
            print()
        elif order == 'IN':
            inOrder(self.root)
            print()
        elif order == 'POST':
            postOrder(self.root)
            print()
    
    def height(self, root):
        """Object method to get the height of the tree below a certain node

        :param root: The node from which to find the height
        :type root: DoublyLinkedListNode
        :return: The height below  that node
        :rtype: int

        >>> tree = BinarySearchTree()
        >>> tree.insert(43)
        >>> tree.insert(34)
        >>> tree.insert(78)
        >>> tree.insert(18)
        >>> tree.insert(69)
        >>> tree.traverse("IN")
        18 34 43 69 78 
        >>> tree.height(tree.root)
        2

        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))