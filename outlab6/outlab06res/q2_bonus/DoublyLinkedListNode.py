# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """This is a node in the implementation of a doubly linked list

    :param data: The data to be stored in the node
    :type data: int

    :param next: The pointer to the next node, defaults to None
    :type next: DoublyLinkedListNode

    :param prev: The pointer to the previous node, defaults to None
    :type prev: DoublyLinkedListNode
    """
    
    def __init__(self, data):
        """Constructor method

        :param data: The data to be stored in the node
        :type data: int

        >>> L = DoublyLinkedListNode(23)
        >>> print(L)
        23
        >>> L = DoublyLinkedListNode(82)
        >>> print(L)
        82

        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """Convertor method

        :return: The value of the data stored in the node as a string
        :rtype: str

        >>> L = DoublyLinkedListNode(23)
        >>> print(L)
        23
        >>> str(L)
        '23'

        """
        return str(self.data) 
