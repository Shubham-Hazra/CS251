
################################## Data Structures ################################
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

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """This is a node in the implementation of a doubly linked list

    :param data: The data to be stored in the node
    :type data: int

    :param next: The pointer to the next node, defaults to None
    :type next: DoublyLinkedListNode

    :param prev: The pointer to the previous node, defaults to None
    :type prev: DoublyLinkedListNode

    Object Methods:

    * __init__(self)
    * __str__(str)

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

class DoublyLinkedList:
    """This is a simple implementation of a singly linked list

    :param head: This is the pointer to the head of the linked list, defaults to None
    :type head: DoublyLinkedListNode, defaults to None 

    :param tail: This is the pointer to the tail of the linked list
    :type tail: DoublyLinkedListNode, defaults to None 
    
    Object Methods:

    * __init__(self)
    * insert(self, data)
    * printer(self, sep = ', ')
    * reverse(self)

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

    Object methods:

    * __init__(self, info)
    * __str__(self)

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

class BinarySearchTree:
    """Implementation of a Binary Search Tree

    :param root: This is a pointer to the root node, defaults to None
    :type root: BSTNode

    Object methods:

    * __init__(self)
    * insert(self, val)
    * traverse(self, order)
    * height(self, root)

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

# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """Impelementation of a trie

    :param T: Dictionary containg the prefixes
    :type T: Dictionary

    Object methods:

    * __init__(self)
    * find(self, root, c)
    * insert(self, s)
    * checkPrefix(self, s)
    * countPrefix(self, s)

    """
    def __init__(self):
        """Constructor method

        >>> t = Trie()
        >>> print(t.T)
        {}

        """
        self.T = {}
    
    def find(self, root, c):
        """Object method to check if a character is present in the Trie

        :param root: The node to search for in 
        :type root: Dictionary
        :param c: The character to search for
        :type c: str
        :return: True if the character is found in the trie
        :rtype: Bool

        >>> t = Trie()
        >>> t.insert("CAT")
        >>> t.insert("BAT")
        >>> t.insert("BALL")
        >>> t.insert("BALLADS")
        >>> t.insert("CATACOMBS")
        >>> t.insert("CATASTROPHE")
        >>> t.insert("BANTER")
        >>> t.find(t.T,"B")
        True
        >>> t.find(t.T,"C")
        True
        >>> t.find(t.T,"D")
        False
        >>> t.insert("APPLE")
        >>> t.find(t.T,"A")
        True
        >>> t.find((t.T)["A"],"P")
        True
        

        """
        return (c in root)
    
    def insert(self, s):
        """Object method to insert a string into the trie

        :param s: The string to insert
        :type s: str

        >>> t = Trie()
        >>> t.insert("CAT")
        >>> t.insert("BAT")
        >>> t.insert("BALL")
        >>> t.insert("BALLADS")
        >>> t.insert("CATACOMBS")
        >>> t.insert("CATASTROPHE")
        >>> t.insert("BANTER")

        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """Object method to check is a prefix is preset or not

        :param s: The prefix to search for
        :type s: str
        :return: True if the prefix is found else False
        :rtype: Bool
        
        >>> t = Trie()
        >>> t.insert("CAT")
        >>> t.insert("BAT")
        >>> t.insert("BALL")
        >>> t.insert("BALLADS")
        >>> t.insert("CATACOMBS")
        >>> t.insert("CATASTROPHE")
        >>> t.insert("BANTER")
        >>> t.insert("APPLE")
        >>> t.checkPrefix("BA")
        True
        >>> t.checkPrefix("BAL")
        True
        >>> t.checkPrefix("BALL")
        True
        >>> t.checkPrefix("BALLS")
        False
        >>> t.checkPrefix("BALLADS")
        True
        >>> t.checkPrefix("BAT")
        True
        >>> t.checkPrefix("CAT")
        True
        >>> t.checkPrefix("CA")
        True
        >>> t.checkPrefix("APP")
        True
        >>> t.checkPrefix("CE")
        False


        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """Object method to count the number of strings in th trie which have the given string as prefix

        :param s: The prefix to count for
        :type s: str
        :return: The count of strings which have the given prefix
        :rtype: int

        >>> t = Trie()
        >>> t.insert("CAT")
        >>> t.insert("BAT")
        >>> t.insert("BALL")
        >>> t.insert("BALLADS")
        >>> t.insert("CATACOMBS")
        >>> t.insert("CATASTROPHE")
        >>> t.insert("BANTER")
        >>> t.insert("APPLE")
        >>> t.countPrefix("C")
        3
        >>> t.countPrefix("B")
        4
        >>> t.countPrefix("CA")
        3
        >>> t.countPrefix("CAT")
        3
        >>> t.countPrefix("CATA")
        2
        >>> t.countPrefix("A")
        1
        >>> t.countPrefix("BALL")
        2
        >>> t.countPrefix("C")
        3
        >>> t.countPrefix("K")
        0
        >>> t.countPrefix("KB")
        0

        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0

# --------------------------------- Heap --------------------------------

class Heap:
    """
    This is the implementation of the data structure of a heap. A heap data structure has
    a structural property and a heap property. The structural property states that only the
    last level of the heap may be incomplete and all the nodes must be flushed towards the left i.e.
    the new nodes must always be added in the left most free space.
    The heap property states that the parent must be smaller than both its children.
    
    Object methods:

    * __init__(self, cap)
    * parent(self, i)
    * left(self, i)
    * right(self, i)
    * insert(self, val)
    * min(self)
    * Heapify(self, root)
    * deleteMin(self)
    
    """
    def __init__(self, cap):
        """
        This the constructor for the heap class.
        
        :param cap: This is the maximum number of elements in the heap

        :type cap: int

        >>> h = Heap(32)
        >>> print(h.min())
        -1

        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """
        This returns the parent of an element with index i
        
        :param i: This is the index of the element whose parent we need

        :type i: int

        :return: Returns the index of the parent

        :rtype: int

        >>> h = Heap(32)
        >>> h.insert(5)
        >>> h.insert(13)
        >>> h.insert(17)
        >>> h.insert(6)
        >>> h.insert(9)
        >>> print(h.parent(3))
        1
        >>> print(h.H[h.parent(3)])
        6
        >>> print(h.H[h.parent(2)])
        5
        >>> print(h.H[h.parent(1)])
        5
        >>> print(h.H[h.parent(4)])
        6
        >>> print(h.min())
        5

        """
        return (i - 1) // 2
    
    def left(self, i):
        """
        This returns the left child of an element with index i
        
        :param i: This is the index of the element whose parent we need

        :type i: int

        :return: Returns the index of the left child

        :rtype: int

        >>> h = Heap(32)
        >>> h.insert(5)
        >>> h.insert(13)
        >>> h.insert(17)
        >>> h.insert(6)
        >>> h.insert(9)
        >>> print(h.H[h.left(1)])
        13
        >>> print(h.H[h.left(0)])
        6

        """
        return (2 * i) + 1
    
    def right(self, i):
        """
        This returns the right child of an element with index i
        
        :param i: This is the index of the element whose parent we need

        :type i: int

        :return: Returns the index of the right child

        :rtype: int

        >>> h = Heap(32)
        >>> h.insert(5)
        >>> h.insert(13)
        >>> h.insert(17)
        >>> h.insert(6)
        >>> h.insert(9)
        >>> print(h.H[h.right(0)])
        17
        >>> print(h.H[h.right(1)])
        9

        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """
        This inserts a new element with the value as val into the heap as long as it does not exceed the heap capacity
        
        :param val: This is the value of the new element

        :type val: int

        >>> h = Heap(32)
        >>> h.insert(5)
        >>> h.insert(13)
        >>> h.insert(17)
        >>> h.insert(6)
        >>> h.insert(9)
        >>> print(h.min())
        5

        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """
        This returns the minimum value in the heap i.e. the first element

        :return: Returns the minimum element

        :rtype: int

        >>> h = Heap(32)
        >>> h.insert(5)
        >>> h.insert(13)
        >>> h.insert(17)
        >>> h.insert(6)
        >>> h.insert(9)
        >>> print(h.min())
        5


        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """
        This is to make it into a heap when both the left and right subheaps satisfy the heap property but not the whole heap.
        
        :param root: The element from which to start the heapify

        :type root: int
        
        >>> h = Heap(32)
        >>> h.insert(32)
        >>> h.insert(21)
        >>> h.insert(5)
        >>> h.insert(3)
        >>> print(h.min())
        3
        >>> h.deleteMin()
        >>> print(h.min())
        5
        >>> h.insert(2)
        >>> print(h.min())
        2

        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """
        This is to delete the minimum element i.e. delete the first element.

        >>> h = Heap(32)
        >>> h.insert(5)
        >>> h.insert(13)
        >>> h.insert(17)
        >>> h.insert(6)
        >>> h.insert(9)
        >>> print(h.min())
        5
        >>> h.deleteMin()
        >>> print(h.min())
        6
        >>> h.deleteMin()
        >>> print(h.min())
        9

        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.H.pop()
                self.Heapify(0)

