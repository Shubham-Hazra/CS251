# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """This is a node in the implementation of a Binary search tree

    :param info: The data to be stored in the node
    :type info: int

    :param left: This is the pointer to the left child of the node, defaults to None
    :type left: BSTNode, defaults to None 

    :param right: This is the pointer to the right child of the node, defaults to None
    :type right: BSTNode, defaults to None 

    :param level: This keeps track of the level at which the node is present
    :type level: int
    """
    
    def __init__(self, info):
        """Constructor method

        :param info: The data to be stored in the node
        :type info: int

        >>> node = BSTNode(76)
        >>> print(node)
        76

        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """Convertor method

        :return: The value in the node as a string
        :rtype: str

        >>> node = BSTNode(76)
        >>> print(node)
        76
        >>> str(node)
        '76'

        """
        return str(self.info)