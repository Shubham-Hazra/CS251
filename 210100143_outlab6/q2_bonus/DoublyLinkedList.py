from DoublyLinkedListNode import *

class DoublyLinkedList:
    """This is a simple implementation of a singly linked list

    :param head: This is the pointer to the head of the linked list, defaults to None
    :type head: DoublyLinkedListNode, defaults to None 

    :param tail: This is the pointer to the tail of the linked list
    :type tail: DoublyLinkedListNode, defaults to None 
    """
    def __init__(self):
        """Constructor method

        >>> L = DoublyLinkedList()
        >>> L.printer()
        []

        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """Object method to insert a new node into the linked list

        :param data: Data to be inserted
        :type data: int

        >>> L = DoublyLinkedList()
        >>> L.insert(40)
        >>> L.insert(4)
        >>> L.insert(44)
        >>> L.printer()
        [40, 4, 44]

        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """Object method to print the linked list

        :param sep: The separator to put in between two values of the linked list, defaults to ', '
        :type sep: str, optional

        >>> L = DoublyLinkedList()
        >>> L.insert(12)
        >>> L.insert(1)
        >>> L.insert(23)
        >>> L.printer()
        [12, 1, 23]

        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """Object method to reverse the order of elements in the list

        >>> L = DoublyLinkedList()
        >>> L.insert(12)
        >>> L.insert(1)
        >>> L.insert(23)
        >>> L.insert(44)
        >>> L.reverse()
        >>> L.printer()
        [44, 23, 1, 12]

        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev