class Heap:
    """
    This is the implementation of the data structure of a heap. A heap data structure has
    a structural property and a heap property. The structural property states that only the
    last level of the heap may be incomplete and all the nodes must be flushed towards the left i.e.
    the new nodes must always be added in the left most free space.
    The heap property states that the parent must be smaller than both its children.
    """
    def __init__(self, cap):
        """
        This the constructor for the heap class.
        
        :param cap: This is the maximum number of elements in the heap

        :type cap: int
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
        """
        return (i - 1) // 2
    
    def left(self, i):
        """
        This returns the left child of an element with index i
        
        :param i: This is the index of the element whose parent we need

        :type i: int

        :return: Returns the index of the left child

        :rtype: int
        """
        return (2 * i) + 1
    
    def right(self, i):
        """
        This returns the right child of an element with index i
        
        :param i: This is the index of the element whose parent we need

        :type i: int

        :return: Returns the index of the right child

        :rtype: int
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """
        This inserts a new element with the value as val into the heap as long as it does not exceed the heap capacity
        
        :param val: This is the value of the new element

        :type val: int
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
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """
        This is to make it into a heap when both the left and right subheaps satisfy the heap property but not the whole heap.
        
        :param root: The element from which to start the heapify

        :type root: int
        
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

        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.Heapify(0)


