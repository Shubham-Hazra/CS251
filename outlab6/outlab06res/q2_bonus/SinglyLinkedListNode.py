# ------------------------------- Singly Linked List -----------------------------

class SinglyLinkedListNode:
    """This is a node in the implementation of a singly linked list

    :param data: The data to be stored in the node
    :type data: int 

    :param next: The pointer to the next node, defaults to None
    :type next: SinglyLinkedListNode

    Object Methods:

    * __init__(self)
    * __str__(str)

    """
    def __init__(self, data):
        """Constructor method

        >>> L = SinglyLinkedListNode(5)
        >>> print(L)
        5
        >>> L = SinglyLinkedListNode(-1)
        >>> print(L)
        -1
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """Convertor method

        :return: The value of the data stored in the node as a string
        :rtype: str

        >>> L = SinglyLinkedListNode(5)
        >>> str(L)
        '5'
        >>> L = SinglyLinkedListNode(-1)
        >>> str(L)
        '-1'
        """
        return str(self.data)
