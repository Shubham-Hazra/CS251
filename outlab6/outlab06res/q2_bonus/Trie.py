# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """Impelementation of a trie

    :param T: Dictionary containg the prefixes
    :type T: Dictionary
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