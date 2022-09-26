from SinglyLinkedListNode import *

class SinglyLinkedList:
    """This is a simple implementation of a singly linked list

       :param head: This is the pointer to the head of the linked list, defaults to None
       :type head: SinglyLinkedListNode, defaults to None 

       :param tail: This is the pointer to the tail of the linked list
       :type tail: SinglyLinkedListNode, defaults to None 

       Object Methods:

       * __init__(self)
       * insert(self,data)
       * find(self,data)
       * deleteVal(self,data)
       * printer(self, sep = ', ')
       * reverse(self)

    """
    
    def __init__(self):
        """Constructor method

        >>> L = SinglyLinkedList()
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """Object method to insert a new node into the linked list

        :param data: Data to be inserted
        :type data: int

        >>> L = SinglyLinkedList()
        >>> L.insert(4)
        >>> L.insert(7)
        >>> L.insert(1)
        >>> L.printer()
        [4, 7, 1]
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """Object method to find the node with the given data

        :param data: The value to search for 
        :type data: int 
        :return: The pointer to the node containing the data if found else None
        :rtype: SinglyLinkedListNode

        >>> L = SinglyLinkedList()
        >>> L.insert(4)
        >>> L.insert(7)
        >>> L.insert(1)
        >>> L.printer()
        [4, 7, 1]
        >>> node = L.find(7)
        >>> print(node)
        7
        >>> node = L.find(10)
        >>> print(node)
        None
        >>> node = L.find(4)
        >>> print(node)
        4
        >>> node = L.find(1)
        >>> print(node)
        1
        >>> node = L.find(11)
        >>> print(node)
        None

        """
        head = self.head
        while head != None:
            if(head.data == data):
                break
            head = head.next
        return head
    
    def deleteVal(self, data):
        """Object method to delete a node with the given data 

        :param data: The value to be deleted from the list
        :type data: int
        :return: True if deleted successfully else False 
        :rtype: Bool

        >>> L = SinglyLinkedList()
        >>> L.insert(4)
        >>> L.insert(7)
        >>> L.insert(1)
        >>> L.printer()
        [4, 7, 1]
        >>> L.deleteVal(4)
        True
        >>> L.printer()
        [7, 1]
        >>> L.deleteVal(7)
        True
        >>> L.printer()
        [1]
        >>> L.deleteVal(1)
        True
        >>> L.printer()
        []
        >>> L.insert(7)
        >>> L.insert(1)
        >>> L.deleteVal(4)
        False
        >>> L.printer()
        [7, 1]
        >>> L.insert(4)
        >>> L.printer()
        [7, 1, 4]
        >>> L.deleteVal(4)
        True
        >>> L.printer()
        [7, 1]
        """
        head = self.head
        prevPos = None
        while head != None:
            if(head.data == data):
                break
            prevPos = head
            head = head.next
        if head == None:
            return False
        if head.next == None and prevPos == None:
            self.head = None
            self.tail = None
        if head.next == None and prevPos != None:
            prevPos.next = head.next
            self.tail = prevPos
            return True
        if prevPos == None:
            self.head = head.next
            return True
        prevPos.next = head.next
        return True
    
    def printer(self, sep = ', '):
        """Object method to print the linked list

        :param sep: The separator to put in between two values of the linked list, defaults to ', '
        :type sep: str, optional

        >>> L = SinglyLinkedList()
        >>> L.insert(4)
        >>> L.insert(7)
        >>> L.insert(1)
        >>> L.printer()
        [4, 7, 1]

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

        >>> L = SinglyLinkedList()
        >>> L.insert(30)
        >>> L.insert(23)
        >>> L.insert(3)
        >>> L.printer()
        [30, 23, 3]
        >>> L.reverse()
        >>> L.printer()
        [3, 23, 30]

        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """Class method to merge to singly linked list into one

    :param list1: The first list to merge
    :type list1: SinglyLinkedList
    :param list2: The second list to merge
    :type list2: SinglyLinkedList
    :return: The merged list
    :rtype: SinglyLinkedList

    >>> L1 = SinglyLinkedList()
    >>> L1.insert(3)
    >>> L1.insert(5)
    >>> L1.insert(7)
    >>> L2 = SinglyLinkedList()
    >>> L2.insert(2)
    >>> L2.insert(4)
    >>> L2.insert(6)
    >>> L=merge(L1,L2)
    >>> L.printer()
    [2, 3, 4, 5, 6, 7]

    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged
